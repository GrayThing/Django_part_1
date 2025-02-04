from django.shortcuts import render

# Create your views here.


def main(request):
    title = 'Gphones'
    context = {
        'title': title,
    }
    return render(request, 'third_task/main.html', context)


def buy(request):
    title = 'Buy'
    product_type = 'Телефоны'
    product1 = 'Gphone S5 PG'
    product2 = 'Gphone 4K LTE'
    product3 = 'Gphone Ultra FD'
    context = {
        'title': title,
        'product_type': product_type,
        'product1': product1,
        'product2': product2,
        'product3': product3,
    }
    return render(request, 'third_task/shop.html', context)


def bag(request):
    return render(request, 'third_task/bag.html')
