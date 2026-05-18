from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Account created successfully! You can now log in.'
            )
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegistrationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )
