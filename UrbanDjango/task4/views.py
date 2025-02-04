from django.shortcuts import render

# Create your views here.


def main(request):
    title = 'Gphones'
    pagename = 'Главная страница'
    content = []
    context = {
        'title': title,
        'pagename': pagename,
        'content': content,
    }
    return render(request, 'fourth_task/main.html', context)


def buy(request):
    title = 'Купить'
    product_type = 'Телефоны'
    pagename = 'Купить'
    content = ['Gphone S5 PG', 'Gphone 4K LTE', 'Gphone Ultra FD']
    context = {
        'title': title,
        'product_type': product_type,
        'pagename': pagename,
        'content': content,
    }
    return render(request, 'fourth_task/shop.html', context)


def bag(request):
    title = 'Корзина'
    pagename = 'Корзина'
    content = ['Извините, ваша корзина пуста', ]
    context = {
        'title': title,
        'pagename': pagename,
        'content': content,
    }
    return render(request, 'fourth_task/bag.html', context=context)

