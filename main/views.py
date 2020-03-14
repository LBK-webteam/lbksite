"""
Hier wordt de home pagina view gelinkt met een html script, rendered met python context, css en eventueel JavaScript.
"""

from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth import authenticate, login
#from .forms import RegisterForm

from .models import *


def home(request):
    posts = Post.objects.order_by('-post_creation_date')[:5]
    pages = Page.objects.all()
    context = {'posts': posts, 'pages': pages}
    return render(request, 'main/home.html', context)


def page(request, page_title):
    pages = Page.objects.all()
    current_page = get_object_or_404(Page, pk=page_title)
    context = {'pages': pages, 'page': current_page}
    return render(request, 'main/page.html', context)


def db(request):
    db_members = DBmember.objects.all()
    pages = Page.objects.all()
    context = {'db_members': db_members, 'pages': pages}
    return render(request, 'main/db.html', context)


"""
def galabal(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'main/galabal.html', context)
    """


def br_algemeen(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'main/br_algemeen.html', context)


def br_bedrijven(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'main/br_bedrijven.html', context)


def br_galerij(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'main/br_galerij.html', context)


def br_vacatures(request):
    pages = Page.objects.all()
    vacancies = Vacancy.objects.all()
    context = {'pages': pages, 'vacancies': vacancies}
    return render(request, 'main/br_vacatures.html', context)

"""
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')

    return render(request, 'main/register.html')
"""