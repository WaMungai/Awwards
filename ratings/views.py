from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewProjectForm,NewRatingForm,NewProfileForm

# Create your views here.
def home(request):
    return HttpResponse('Advanced Projects ')

def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST. request.FILES)
        if form.is_valid():
            project =form.save(commit=False)
            project.editor =current_user
            project.save()
            return redirect('home')
        else:
            form = NewProjectForm()
        return render(request,'new_project.html',{"form":form})
    

