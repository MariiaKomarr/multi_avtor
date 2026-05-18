from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete
from .rss import LatestPostsFeed


urlpatterns = [
    path('', post_list, name='post_list'),

    path(
        'post/<int:post_id>/',
        post_detail,
        name='post_detail'
    ),

    path(
        'post/create/',
        post_create,
        name='post_create'
    ),

    path(
        'post/<int:post_id>/update/',
        post_update,
        name='post_update'
    ),

    path(
        'post/<int:post_id>/delete/',
        post_delete,
        name='post_delete'
    ),

    path('rss/', LatestPostsFeed(), name='post_rss'),
]