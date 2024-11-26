from django.shortcuts import render


def home(request):
    return render(request, 'fourth_task/home.html')


def shop(request):
    return render(request, 'fourth_task/shop.html', {
        'Хозтовары': ["Молоток", "Пила", "Пассатижи"]
    })


def cart(request):
    return render(request, 'fourth_task/cart.html')