from django.urls import path
from studentapp import views

urlpatterns = [
    path('student_list/', views.student_list, name='student_list'),
    path('register/', views.captcha_submit, name='register'),
    path('submit/', views.submit, name="submit"),
]
