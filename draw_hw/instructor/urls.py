from . import views
from django.urls import path

app_name = 'instructor'

urlpatterns = [
    path('', views.create_course, name='instructor'), 
    path('detail/<slug:pk>/', views.course_detail, name='course_detail'),
    path('detail/<slug:pk>/hw', views.create_assignment, name='assignment')
]