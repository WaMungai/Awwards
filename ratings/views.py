from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewProjectForm,NewRatingForm,NewProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .models import Profile,Project,Rating
# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    return HttpResponse('Advanced Projects ')


@login_required(login_url='/accounts/login')
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
    

@login_required(login_url='/accounts/login')
def search_by_title(request):
    if'title' in request.GET and request.GET["title"]:
        search_term=request.GET.get("title")
        searched_titles=Project.search_by_term(search_term)
        message=f"{search_term}"
        
        return render(request,"search.html",{"message":message,"titles":searched_titles})
    else:
        message="You haven't serached for any terms"
        return render(request,'search.html',{"message":message})

@login_required(login_url='/accounts/login')
def single_project(request,project_id):
    project_posted=Project.single_project(project_id)
    imageId=Project.get_image_id(project_id)
    rating=Rating.get_rating_byproject_id(project_id)
    
    design=Rating.design
    usability=Rating.usability
    content=Rating.content
    
    return render(request,'project.html',{"project":project_posted})


@login_required(login_url='/accounts/login')
def new_profile(request):
    current_user=request.user
    if request.method =='POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.editor=current_user
            profile.save()
        return redirect('home')
    
    else:
        form= NewProfileForm()
    return render(request,'new_profile.html',{"form":form})