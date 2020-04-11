"""
Hier wordt de home pagina view gelinkt met een html script, rendered met python context, css en eventueel JavaScript.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from .models import *


def home(request):
    posts = Post.objects.order_by('-post_creation_date')[:5]
    pages = Page.objects.order_by('page_index')
    context = {'posts': posts, 'pages': pages}
    return render(request, 'main/home.html', context)


def page(request, page_title):
    pages = Page.objects.order_by('page_index')
    current_page = get_object_or_404(Page, pk=page_title)
    context = {'pages': pages, 'page': current_page}
    return render(request, 'main/page.html', context)


def db(request):
    db_members = DBmember.objects.all()
    pages = Page.objects.order_by('page_index')
    context = {'db_members': db_members, 'pages': pages}
    return render(request, 'main/db.html', context)


"""
def galabal(request):
    Page.objects.order_by('page_index')
    context = {'pages': pages}
    return render(request, 'main/galabal.html', context)
    """
<<<<<<< HEAD
=======


def success(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'main/success.html', context)
>>>>>>> c81f19b1e1ecb4992a02cddbb27603835b563af6


def br_algemeen(request):
    Page.objects.order_by('page_index')
    context = {'pages': pages}
    return render(request, 'main/br_algemeen.html', context)


def br_bedrijven(request):
    Page.objects.order_by('page_index')
    context = {'pages': pages}
    return render(request, 'main/br_bedrijven.html', context)


def br_galerij(request):
    Page.objects.order_by('page_index')
    context = {'pages': pages}
    return render(request, 'main/br_galerij.html', context)


def br_vacatures(request):
    Page.objects.order_by('page_index')
    vacancies = Vacancy.objects.all()
    context = {'pages': pages, 'vacancies': vacancies}
    return render(request, 'main/br_vacatures.html', context)


def opkomend_formulieren(request):
    pages = Page.objects.all()
    if request.method == 'POST':
        form = RunningForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    else:
        form = RunningForm()
    context = {'pages': pages, 'form': form}
    return render(request, 'main/opkomend_formulieren.html', context)


def opkomend_brieven(request):
    pages = Page.objects.all()
    runnings = Running.objects.filter(formtype='A')
    dbfuncties = ['Preses',
                  'Vice-preses',
                  'Penningmeester',
                  'Secretaris',
                  'Gnorgl verantwoordelijke',
                  'Gnorgl boekhouder',
                  'Baarr verantwoordelijke',
                  'Baarr boekhouder',
                  'Activiteiten verantwoordelijke',
                  'Sport verantwoordelijke',
                  'Cultuur verantwoordelijke',
                  'Internationaal verantwoordelijke',
                  'Bedrijvenrelaties verantwoordelijke',
                  'Onderwijs verantwoordelijke',
                  'Onderwijs secretaris',
                  'Logistiek verantwoordelijke',
                  'Cursusdienst verantwoordelijke',
                  'ICT verantwoordelijke']
    context = {'pages': pages, 'runnings': runnings, 'dbfuncties': dbfuncties}
    return render(request, 'main/opkomend_brieven.html', context)


def neucom(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'main/neucom.html', context)


def officiele_documenten(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'main/officiele_documenten.html', context)

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