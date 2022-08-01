from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import UpdateView, ListView, DetailView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter

from test_app.email import send
from test_app.models import Subject, Person, Group
from test_app.pagination import PersonPagePagination, GroupPagePagination, SubjectPagePagination
from test_app.serializers import PersonSerializer, GroupSerializer, SubjectSerializer

USER_MODEL = get_user_model()


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


def signup(request):
    if request.method == "GET":
        return render(request, "registration/signup.html")

    elif request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = USER_MODEL.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False
        )

        send(
            subject='Verify your account',
            to_email=email,
            template_name='registration/verify_account',
            context={
                "username": username,
                "verify_url": reverse('verify_account', kwargs={
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user)
                }),
                "request": request
            }
        )

        return HttpResponse(f"Hello {user.username}. You need to verify your account")


def verify_account(request, uid, token):
    try:
        user = USER_MODEL.objects.get(pk=urlsafe_base64_decode(uid))
    except():
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse(f'Hello, {user.username}. Your account is verified')
    else:
        return HttpResponse('Invalid link')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PersonPagePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['first_name']
    ordering_fields = ['created_at']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = GroupPagePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['created_at']


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = SubjectPagePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name']
    ordering_fields = ['created_at']
