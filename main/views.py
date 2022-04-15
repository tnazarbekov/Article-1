from django.shortcuts import render


def home(request):
    data = {

    }
    return render(request, 'main/index.html', context=data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
