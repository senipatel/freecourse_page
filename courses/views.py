# # courses/views.py

# from django.shortcuts import render, get_object_or_404
# from .models import Course
# from django.contrib.auth.decorators import login_required
# from .models import Enrollment



# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'courses/course_list.html', {'courses': courses})

# def course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     return render(request, 'courses/course_detail.html', {'course': course})


# @login_required
# def enroll_in_course(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     Enrollment.objects.get_or_create(user=request.user, course=course)
#     return redirect('course_detail', course_id=course_id)



from django.shortcuts import render, get_object_or_404
from .models import Course, Video, Announcement, Question
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    videos = course.videos.all()
    announcements = Announcement.objects.filter(course=course)
    questions = Question.objects.filter(course=course)
    context = {
        'course': course,
        'videos': videos,
        'announcements': announcements,
        'questions': questions,
    }
    # return render(request, 'courses/course_detail.html', {'course': course, 'videos': videos})
    return render(request, 'courses/course_detail.html', context)



@login_required
def enroll_in_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    return redirect('course_detail', course_id=course.id)