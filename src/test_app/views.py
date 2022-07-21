from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView

from test_app.models import Subject, Person


def index_template(request):
    return render(request, 'index.html')


class SubjectDjangoListView(ListView):
    model = Subject
    template_name = "subject_model/subject_list.html"


class SubjectDjangoUpdateView(UpdateView):
    model = Subject
    fields = ["name"]
    template_name = "subject_model/subject_update.html"
    success_url = reverse_lazy("subject_list")


class PersonDjangoListView(ListView):
    model = Person
    template_name = "person_model/person_list.html"


class TeacherDjangoUpdateView(UpdateView):
    model = Person
    fields = ["first_name", "last_name", "age", "type", "status"]
    template_name = "person_model/teacher_update.html"
    success_url = reverse_lazy("person_list")


class PersonDjangoDetailView(DetailView):
    model = Person
    template_name = "person_model/student_detail.html"
