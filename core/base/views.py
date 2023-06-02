from django.shortcuts import render,redirect 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .forms import MyUserCreationForm
from .models import  User

# Create your views here.

def home(request):
    context = {
         'user': request.user
        }

    return render(request,'home.html',context)


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email:
            email = email.lower()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page': page}
    return render(request, 'home.html', context)



def registerPage(request):
    form = MyUserCreationForm()


    if request.method == 'POST' : 
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else :
            messages.error(request, 'An error occurred during registration')

    return render(request, 'creating_account/login_register.html', {'form': form})




def logoutUser(request):
    logout(request)
    return redirect('home')