from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Post
from .forms import PostForm

from comments.forms import CommentForm


def post_list(request):

    posts = Post.objects.all()

    return render(
        request,
        'posts/post_list.html',
        {'posts': posts}
    )


def post_detail(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    comments = post.comments.all()

    form = CommentForm()

    if request.method == 'POST':

        if request.user.is_authenticated:

            form = CommentForm(request.POST)

            if form.is_valid():

                comment = form.save(commit=False)

                comment.post = post

                comment.author = request.user

                comment.save()

                return redirect(
                    'post_detail',
                    post_id=post.id
                )

    return render(
        request,
        'posts/post_detail.html',
        {
            'post': post,
            'comments': comments,
            'form': form
        }
    )


@login_required(login_url='login')
def post_create(request):

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.save()

            form.save_m2m()

            return redirect(
                'post_detail',
                post_id=post.id
            )

    else:

        form = PostForm()

    return render(
        request,
        'posts/post_form.html',
        {'form': form, 'action': 'Create'}
    )


@login_required(login_url='login')
def post_update(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    if post.author != request.user:

        return HttpResponseForbidden(
            'You can only edit your own posts.'
        )

    if request.method == 'POST':

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect(
                'post_detail',
                post_id=post.id
            )

    else:

        form = PostForm(instance=post)

    return render(
        request,
        'posts/post_form.html',
        {'form': form, 'action': 'Update', 'post': post}
    )


@login_required(login_url='login')
def post_delete(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id
    )

    if post.author != request.user:

        return HttpResponseForbidden(
            'You can only delete your own posts.'
        )

    if request.method == 'POST':

        post.delete()

        return redirect('post_list')

    return render(
        request,
        'posts/post_confirm_delete.html',
        {'post': post}
    )