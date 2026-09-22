from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from courses.models import Course, Enrollment


@login_required
def dashboard_view(request):

    total_courses = Course.objects.count()

    my_enrollments = Enrollment.objects.filter(
        student=request.user
    ).count()

    if request.user.is_superuser:

        role = "Admin"
        template = "dashboard/admin_dashboard.html"

    else:

        if hasattr(request.user, "userprofile"):
            role = request.user.userprofile.get_role_display()
        else:
            role = "User"

        template = "dashboard/dashboard.html"

    return render(
        request,
        template,
        {
            "total_courses": total_courses,
            "my_enrollments": my_enrollments,
            "role": role,
        }
    )


def is_admin(user):
    return user.is_authenticated and user.is_superuser


@login_required
@user_passes_test(is_admin)
def admin_management(request):

    return render(
        request,
        "dashboard/admin_management.html"
    )