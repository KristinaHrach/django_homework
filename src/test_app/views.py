from django.contrib.auth import authenticate, logout, login
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, DetailView
from test_app.email import send
from test_app.models import Subject, Person


def index_template(request):
    return render(request, 'index.html')


def send_message(request):
    send(
        "Greeting",
        "kristinahrach@gmail.com",
        "send_email/email_message",
    )

    return JsonResponse({
        "message": "Hello new world"

    })


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


def signin(request):

    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse(f"Hi {user.username}")
        else:
            return HttpResponse("Invalid credentials")


def signout(request):
    logout(request)
    return redirect(reverse_lazy("login"))
