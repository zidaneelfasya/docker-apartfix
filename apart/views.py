# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import TeamMember

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
def team_list(request):
    members = TeamMember.objects.all()
    return render(request, 'team_list.html', {'members': members})

def team_detail(request, id_team):
    member = get_object_or_404(TeamMember, id=id_team)
    members = [member]
    return render(request, 'team_detail.html', {'members': members})
