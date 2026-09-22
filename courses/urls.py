from django.urls import path
from . import views

urlpatterns = [
    path("", views.course_list, name="course_list"),
    path("create/", views.create_course, name="create_course"),
    path("<int:course_id>/edit/", views.update_course, name="update_course"),
    path("<int:course_id>/delete/", views.delete_course, name="delete_course"),
    path("my-enrollments/", views.my_enrollments, name="my_enrollments"),
    path("<int:course_id>/enroll/", views.enroll_course, name="enroll_course"),
    path("<int:course_id>/", views.course_detail, name="course_detail"),
]