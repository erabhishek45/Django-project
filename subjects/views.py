from django.shortcuts import render
from django.views.generic import ListView, CreateView


from .models import Subject
from .forms import SubjectForm



class SubjectList(ListView):
	queryset = Subject.objects.all()
	template_name = 'subjects/index.html'


class SubjectCreate(CreateView):
	queryset = Subject.objects.all()
	form_class = SubjectForm
	template_name = 'subjects/create.html'