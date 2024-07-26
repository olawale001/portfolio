from django.shortcuts import render
from projects.models import Project


def project_index(req):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(req, 'projects/project_index.html', context)


def project_detail(req, pk):
    project = Project.objects.get(pk=pk)
    return render(req, 'projects/project_detail.html', {'project': project})


