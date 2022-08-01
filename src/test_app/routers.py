from rest_framework import routers

from test_app import views

router = routers.DefaultRouter()
router.register('Persons', views.PersonViewSet, basename='person')
router.register('Groups', views.GroupViewSet)
router.register('Subjects', views.SubjectViewSet)
