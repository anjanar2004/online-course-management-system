from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course, Enrollment


@login_required
def dashboard_view(request):
    total_courses = Course.objects.count()

    my_enrollments = Enrollment.objects.filter(
        student=request.user
    ).count()

    if request.user.is_superuser:
        role = "Admin"
    elif hasattr(request.user, "userprofile"):
        role = request.user.userprofile.get_role_display()
    else:
        role = "User"

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "total_courses": total_courses,
            "my_enrollments": my_enrollments,
            "role": role,
        }
    )