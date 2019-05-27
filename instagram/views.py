from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
# from .email import send_welcome_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ImageForm, SignupForm, CommentForm, EditForm
from django.db import models
from .models import Image, Profile, Comments, Emma, Like

# Create your views here.
def home(request):
    photos = Image.objects.all()
    profiles = Profile.objects.all()   

    return render(request, 'home.html', {"photos":photos, "profiles":profiles})





def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can <a href="/accounts/login/">Login</a>  your account.')
    else:
        return HttpResponse('Activation link is invalid!')



def new_image(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
        return redirect('profile')

    else:
        form = ImageForm()
    return render(request, 'new_image.html', {"form": form})


def profile(request):
    current_user = request.user
    photos = Image.objects.filter(user=current_user).all()
    posts = Image.objects.filter(user=current_user)
    if request.method == 'POST':
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
           signup_form.save()
    else:        
        signup_form =EditForm() 
    
    return render(request, 'profiles.html', {"profile":profile, "photos":photos})

@login_required(login_url='/accounts/login/')
def comment(request,image_id):
    #Getting comment form data
    if request.method == 'POST':
        image = get_object_or_404(Image, pk = image_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image
            comment.save()
    return redirect('home')
    
@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )
        
        return render(request, 'search.html',{"message":message,"users": searched_users,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def profiles(request,id):
    profile = Profile.objects.get(user_id=id)
    post=Image.objects.filter(user_id=id)
                       
    return render(request,'profiles.html',{"profile":profile,"post":post,"photos":photos,"form":form}) 

