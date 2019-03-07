from django.shortcuts import render, HttpResponseRedirect, render_to_response
from authapp.forms import UsersLoginForm, UsersRegisterForm
from django.contrib import auth
from django.urls import reverse
from authapp.forms import UsersEditForm


def login(request):
    title = 'вход'

    login_form = UsersLoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    print('next', next)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('all_toys'))

    content = {
        'title': title,
        'login_form': login_form,
        'next': next
    }

    return render(request, 'authapp/login.html', content)


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = UsersRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = UsersRegisterForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = UsersEditForm(request.POST, request.FILES,
                                  instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = UsersEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'authapp/edit.html', content)


def handler404(request, template_name="authapp/404.html"):
    response = render_to_response("authapp/404.html")
    response.status_code = 404
    return response
