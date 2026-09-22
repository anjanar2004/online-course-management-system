from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Course, Enrollment


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(
        request,
        "courses/course_list.html",
        {"courses": courses}
    )


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(
        request,
        "courses/course_detail.html",
        {"course": course}
    )


def is_staff(user):
    return user.is_authenticated and (
        user.is_superuser
        or (
            hasattr(user, "userprofile")
            and user.userprofile.role == "staff"
        )
    )


@login_required
@user_passes_test(is_staff)
def create_course(request):
    if request.method == "POST":
        Course.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            instructor=request.POST["instructor"],
            price=request.POST["price"],
        )

        return redirect("course_list")

    return render(request, "courses/course_form.html")


@login_required
@user_passes_test(is_staff)
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        course.title = request.POST["title"]
        course.description = request.POST["description"]
        course.instructor = request.POST["instructor"]
        course.price = request.POST["price"]
        course.save()

        return redirect("course_detail", course_id=course.id)

    return render(
        request,
        "courses/course_form.html",
        {"course": course}
    )


@login_required
@user_passes_test(is_staff)
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        course.delete()
        return redirect("course_list")

    return render(
        request,
        "courses/course_confirm_delete.html",
        {"course": course}
    )


@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    return redirect("my_enrollments")

@login_required
def my_enrollments(request):
    enrollments = Enrollment.objects.filter(student=request.user)

    return render(
        request,
        "courses/my_enrollments.html",
        {"enrollments": enrollments}
    )