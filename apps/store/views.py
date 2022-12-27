from django.shortcuts import render


def store(request):
    context = {}
    return render(request, 'store/footer.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
