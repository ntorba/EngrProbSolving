from django.shortcuts import render, redirect
from collection.forms import ProjectForm
from collection.models import Project

#Views holds all of the logic for displaying in templates

# Create your views here.
def index_engr1102(request):
    projects = Project.objects.all()
    return render(request, 'index_engr1102.html', {'projects': projects})

def our_projects(request):
    projects = Project.objects.all()
    return render(request, 'our_projects.html', {'projects': projects})

def project_detail(request, slug):
    #grab the object
    project = Project.objects.get(slug=slug)
    # and pass to the template
    return render(request, 'projects/project_detail.html', {
        'project': project,
    })

def edit_project(request, slug):
    #grab the object...
    project = Project.objects.get(slug=slug)
    # set the form we are using
    form_class = ProjectForm
    #if we're coming to this view from a submitted form,
    if request.method == 'POST':
        #grab the data from the submitted form
        form = form_class(data=request.POST, instance=project)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('project_detail', slug=project.slug)
        
    # otherwise just create the form
    else:
        form = form_class(instance=project)
            
    #and render the template
    return render(request, 'projects/edit_project.html', {
        'project': project,
        'form': form,
        })
