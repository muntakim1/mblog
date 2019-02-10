from django.shortcuts import render, get_object_or_404
from .models import Post, Category, AlgorithmPost, AlgorithmCategory,ContactEmail
from .forms import ContactForm
from django.core.mail import send_mail


def index(request):
    context = {
        'category': Category.objects.all(),
        'Post': Post.objects.all(),
        'Algocategory': AlgorithmCategory.objects.all(),
        'AlgoPost': AlgorithmPost.objects.all()
    }
    return render(request, 'index.html', context)


def PostView(request, pk):
    all_post = get_object_or_404(Post, pk=pk)
    context = {
        'category': Category.objects.all(),
        'Post': Post.objects.all(),
        'Algocategory': AlgorithmCategory.objects.all(),
        'AlgoPost': AlgorithmPost.objects.all(),
        'all_post': all_post
    }
    return render(request, 'pages/postview.html', context)


def About(request):
    context = {
        'category': Category.objects.all(),
        'Post': Post.objects.all(),
        'Algocategory': AlgorithmCategory.objects.all(),
        'AlgoPost': AlgorithmPost.objects.all()

    }
    return render(request, 'pages/about.html', context)


def Languages(request, pk):
    get_all = Post.objects.filter(category_id=pk)
    context = {
        'category': Category.objects.all(),
        'Post': Post.objects.all(),
        'Algocategory': AlgorithmCategory.objects.all(),
        'AlgoPost': AlgorithmPost.objects.all(),
        'post': get_all

    }
    return render(request, 'pages/languages.html', context)


def dataAL(request, pk):
    get_all = AlgorithmPost.objects.filter(category_id=pk)
    context = {
        'category': Category.objects.all(),
        'Post': Post.objects.all(),
        'Algocategory': AlgorithmCategory.objects.all(),
        'AlgoPost': AlgorithmPost.objects.all(),
        'post': get_all
    }
    return render(request, 'pages/datastructure.html', context)


def ContactUs(request):
    mail=ContactEmail()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
           mail.email=form.cleaned_data['sender']
           mail.message=form.cleaned_data['message']
           mail.name=form.cleaned_data['name']
           mail.subject=form.cleaned_data['subject']
           mail.save() 
    else:
        form = ContactForm()
    context = {
        'category': Category.objects.all(),
        'Post': Post.objects.all(),
        'Algocategory': AlgorithmCategory.objects.all(),
        'AlgoPost': AlgorithmPost.objects.all(),
        'form': form
    }
    return render(request, 'pages/contact.html', context)
