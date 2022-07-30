"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from test_app.views import index_template, SubjectDjangoListView, SubjectDjangoUpdateView, \
    TeacherDjangoUpdateView, PersonDjangoListView, PersonDjangoDetailView, send_message, signin, signout, signup, \
    verify_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index_template),
    path('send_email', send_message),
    path('subjects_list', SubjectDjangoListView.as_view(), name="subject_list"),
    path('persons_list', PersonDjangoListView.as_view(), name="person_list"),
    path('subjects_update <int:pk>', SubjectDjangoUpdateView.as_view(), name="subject_update"),
    path('teacher_update <int:pk>', TeacherDjangoUpdateView.as_view(), name="teacher_update"),
    path('student_detail/<int:pk>', PersonDjangoDetailView.as_view(), name="student_detail"),
    path('login', signin, name="login"),
    path('logout', signout),
    path('signup', signup, name="signup"),
    path('verify_account/<str:uid>/<str:token>', verify_account, name="verify_account")

]
