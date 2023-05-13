from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
import random
from django.core.mail import send_mail
from blog.models import Post,Contact   
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    else:
        try:
            my_obj=Admin.objects.get(email=request.POST['email'])
            return render(request,'register.html',{'msg':'email Already Exists'})
        except:
            global user_list,comp_otp
            user_list=[request.POST['full_name'],request.POST['email'],request.POST['password']]
            comp_otp=random.randint(1000,9999)
            subject='CoderBlog'
            message=f'{user_list[0]} your otp is {comp_otp}'
            from_mail=settings.EMAIL_HOST_USER
            to_mail=[request.POST['email']]
            send_mail(subject,message,from_mail,to_mail)
            return render(request,'otp.html')

def otp(request):
    if request.method=="GET":
        return render(request,'otp,html')
    else:
        if comp_otp==int(request.POST['u_otp']):
            Admin.objects.create(
                full_name=user_list[0],
                email=user_list[1],
                password=user_list[2]
            )
            return render(request,'register.html',{'msg':'Create Admin Sucessfully!!'})
        else:
            return render(request,'otp.html',{'msg':'Invalid Password'})

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        try:
            my_obj=Admin.objects.get(email=request.POST['email'])
            if request.POST['password']==my_obj.password:
                request.session['bloger_email']=my_obj.email
                return redirect('bloger_index')
            else:
                return render(request,'login.html',{'msg':'Password Wrong !!!'})
        except:
            return render(request,'login.html',{'msg':'Email Not register !!!'})

def logout(request):
    del request.session['bloger_email']
    return render(request,'login.html')

def bloger_index(request):
    try:
        my_obj=Admin.objects.get(email=request.session['bloger_email'])
        all_blog=Post.objects.all()
        return render(request,'bloger_index.html',{'my_obj':my_obj,'all_data':all_blog})
    except:
        return redirect('login')

def add_blog(request):
    my_obj=Admin.objects.get(email=request.session['bloger_email'])
    if request.method=='GET':
        return render(request,'add_blog.html',{'my_obj':my_obj})
    else:
        Post.objects.create(
            title=request.POST['title'],
            subject=request.POST['subject'].lower(),
            details=request.POST['details'],
            pic=request.FILES['pic']
        )
        return render(request,'add_blog.html',{'msg':'Create Blog Sucessfully !!','my_obj':my_obj})

def edit_blog(request,pk):
    my_obj=Admin.objects.get(email=request.session['bloger_email'])
    edit_blog=Post.objects.get(id=pk)
    if request.method=='GET':
        return render(request, 'edit_blog.html',{'edit_blog':edit_blog,'my_obj':my_obj})
    else:
       edit_blog.title=request.POST['title']
       edit_blog.subject=request.POST['subject']
       edit_blog.details=request.POST['details']
       edit_blog.pic=request.FILES.get('pic')
       edit_blog.save()
       return render(request,'edit_blog.html',{'msg':'Edit Blog Done !!','edit_blog':edit_blog,'my_obj':my_obj})

def del_blog(request,pk):
    del_blog=Post.objects.get(id=pk)
    del_blog.delete()
    return redirect('bloger_index')

def connect(request):
    data=Contact.objects.all()
    return render(request,'connected.html',{'data':data})