from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .form import RecipeForm , CommentFrom
from .models import Recipe, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'recipe/signUp.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentRecipe')
            except IntegrityError:
                return render(request, 'recipe/signUp.html', {'form': UserCreationForm(), 'error': 'Your username is already signed up!'})
        else:
            return render(request, 'recipe/signUp.html', {'form': UserCreationForm(), 'error': 'Passwords did not match!'})


@login_required
def currentRecipe(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'recipe/currentRecipe.html', {'recipes': recipes})


@login_required
def logoutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/home.html', {'recipes': recipes})


def loginUser(request):
    if request.method == 'GET':
        return render(request, 'recipe/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'recipe/login.html', {'form': AuthenticationForm(), 'error': 'username and password did not match!'})
        else:
            login(request, user)
            return redirect('currentRecipe')


@login_required
def createRecipe(request):
    if request.method == 'GET':
        return render(request, 'recipe/createRecipe.html', {'form': RecipeForm()})
    else:
        try:
            form = RecipeForm(request.POST)
            newRecipe = form.save(commit=False)
            newRecipe.user = request.user
            newRecipe.save()
            return redirect('currentRecipe')
        except ValueError:
            return render(request, 'recipe/createRecipe.html', {'form': RecipeForm(), 'error': 'Bad data pass in!'})


def viewRecipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'GET':
        return render(request, 'recipe/viewRecipe.html', {'recipe': recipe , 'form':CommentFrom()})
    else: 
        try:
            form = CommentFrom(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.recipe = recipe
                comment.save()
                return redirect('viewRecipe' , pk=recipe.pk)
        except ValueError:
            return render(request, 'recipe/viewRecipe.html', {'recipe': recipe , 'form':CommentFrom() , 'error': 'Bad Data pass in!'})