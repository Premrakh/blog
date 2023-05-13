from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def index(request):
    all_post=Post.objects.all()
    return render(request,'index.html',{'all_post':all_post})
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def blog_post(request):
    return render(request,'blog_post.html')


def add_contact(request):
    if request.method=="GET":
        return render(request,'contact.html')
    else:
        Contact.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        message=request.POST['message'],
        )
        return render(request,'contact.html',{'msg':'Add Details Successfully !!'})

def blog_single(request,pk):
    global single_blog
    single_blog=Post.objects.get(id=pk)
    if request.method=="GET":
        try:
            post_com=Comment.objects.filter(post=single_blog)
            count =len(post_com)
            return render(request, 'blog_single.html',{'single_blog':single_blog,'post_com':post_com,'count':count})
        except:
            return render(request, 'blog_single.html',{'single_blog':single_blog})
    else:
        Comment.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        comment=request.POST['comment'],
        post=single_blog
    )
        post_com=Comment.objects.filter(post=single_blog)
        count =len(post_com)
        return render(request,'blog_single.html',{'single_blog':single_blog,'post_com':post_com,'count':count})

def option(request):
    all_blog= Post.objects.all()
    sub_blog=[]
    l1=[]
    for i in all_blog:
        if i.subject not in l1:
            l1.append(i.subject)
            sub_blog.append(i)

    return render(request,'option.html',{'sub_blog':sub_blog})

def subject(request,pk):
    filter_blog=Post.objects.filter(subject=pk)
    obj=filter_blog[0]
    return render(request,'subject.html',{'filter_blog':filter_blog, 'obj':obj})

def search(request):
    filter_blog=Post.objects.filter(subject=request.POST['search'].lower())
    if len(filter_blog)==0:
        return render(request,'subject.html',{'msg':'No search found'})
    return render(request,'subject.html',{'filter_blog':filter_blog})

        
    




