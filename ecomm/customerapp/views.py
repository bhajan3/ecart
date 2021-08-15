from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User


# Create your views here.




def sinup(request):
    return render(request, 'account/login.html', {})


def loggg(request):
    return render(request, 'account/my-account.html', {})

def register(request):
    if request.method == 'POST':
        user_reg_form = UserRegistrationForm(request.POST)
        print(">>>>", user_reg_form)
        if user_reg_form.is_valid():
            user_reg_form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")

                # if request.GET and request.GET['next'] !='':
                #     next = request.GET['next']
                #     return HttpResponseRedirect(next)
                # else:
                #     return redirect('index')
            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_reg_form = UserRegistrationForm()

    args = {'user_reg_form': user_reg_form}
    return render(request, 'account/login.html', args)


def login(request):
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(username=request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect('index')
                # if request.GET and request.GET['next'] !='':
                #     next = request.GET['next']
                #     return HttpResponseRedirect(next)
                # else:
                #     return redirect(reverse('profile'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    # args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    args = {'user_form': user_form}
    return render(request, 'account/login.html', args)


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('index')









