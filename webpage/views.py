from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def main(request):
    return render(request, 'main.html')

def form_valid(request):
    new_name = request.POST['user_name']
    new_id = request.POST['user_id']
    new_pw = request.POST['user_pw']

    if(len(new_name) > 15 or len(new_id) > 15 or len(new_pw) > 10):
        messages.error(request, 'name/id/pw length is over 10 words')
        return False
    if(len(new_name) == 0 or len(new_id) == 0 or len(new_pw) == 0):
        messages.error(request, 'name/id/pw를 입력하지 않았습니다.')
        return False
    if Users.objects.filter(id=new_id).exists():
        messages.error(request, 'ID already exists.') 
        return False
    return True

def signup(request):
    if(request.method == 'POST'):
        
        if not form_valid(request):
            return redirect('/signup')

        account = Users.objects.create(
            name = request.POST['user_name'],
            id = request.POST['user_id'],
            pw = request.POST['user_pw'],
        )
        return redirect('/login')
    return render(request, 'Account/signup.html')

def login_valid(request):
    login_id = request.POST["user_id"]
    login_pw = request.POST["user_pw"]
    if(len(login_id) == 0):
        messages.error(request, 'id를 입력해주세요')
        return False
    if(len(login_pw) == 0):
        messages.error(request, 'pw를 입력해주세요')
        return False
    if(Users.objects.filter(id = login_id).filter(pw = login_pw).exists()):
        return True
    else:
        messages.error(request, 'invalid id/pw')
        return False
    
def login(request):
    if request.method =="POST":
        if not login_valid(request):
            return redirect('/login')
        else:
            return redirect('/')
    return render(request, 'Account/login.html')

def userlist(request):
    user = Users.objects.all()
    if request.method == "POST":
        user = Users.objects.get(id = request.POST['drop_id'])
        user.delete()
        return redirect('/userlist')
    return render(request, 'Account/userlist.html', {'user_list':user})

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'Posting/blog.html', {'postlist':postlist})

def create_post(request):
    return render(request, 'Posting/create_post.html')