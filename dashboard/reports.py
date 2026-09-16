from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Course, Enrollment


@login_required
def reports_view(request):
    total_courses = Course.objects.count()
    total_enrollments = Enrollment.objects.count()

    return render(
        request,
        "dashboard/reports.html",
        {
            "total_courses": total_courses,
            "total_enrollments": total_enrollments,
        }
    )