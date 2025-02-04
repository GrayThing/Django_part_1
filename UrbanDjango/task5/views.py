from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

# Create your views here.


def sign_up_by_django(request):
    users = ['Archi', 'Jey', 'Great_warrior', 'Andrew557']
    info = {
        'error': '',
        'greet': '',
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and int(age) >= 18 and username not in users:
                info['greet'] = f'Приветствуем, {username}!'
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            if username in users:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    context = {
        'form': form,
        'info': info,
    }
    return render(request, 'fifth_task/registration_page.html', context=context)


def sign_up_by_html(request):
    users = ['Archi', 'Jey', 'Great_warrior', 'Andrew557']
    info = {
        'error': '',
        'greet': '',
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password == repeat_password and int(age) >= 18 and username not in users:
            info['greet'] = f'Приветствуем, {username}!'
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        if username in users:
            info['error'] = 'Пользователь уже существует'
    return render(request, 'fifth_task/registration_page.html', {'info': info})
