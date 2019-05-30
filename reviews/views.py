from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Profile,Project
from .forms import NewProjectForm
from django.contrib.auth.decorators import login_required 
# Create your views here.
def home(request):
    posts= Project.objects.all()
    return render(request, 'index.html',{"posts":posts})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_project})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def project(request, project_id):
    try:
        project = Project.obects.get(id=project_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "project.html",{"project":project})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

def profile(request):
    posts= Project.objects.all()
    return render(request, 'index.html',{"posts":posts})
