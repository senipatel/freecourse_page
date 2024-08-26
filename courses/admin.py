from django.contrib import admin
from .models import Course, Section, Video, Enrollment, Announcement, Question

class VideoInline(admin.StackedInline):
    model = Video
    extra = 1

class SectionInline(admin.StackedInline):
    model = Section
    extra = 1
    inlines = [VideoInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'price', 'created_at')
    search_fields = ('title', 'instructor__username')
    inlines = [SectionInline]

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at')
    search_fields = ('user__username', 'course__title')

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'date')
    search_fields = ('title', 'content')
    list_filter = ('course', 'date')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'course', 'user', 'date')
    search_fields = ('question', 'answer')
    list_filter = ('course', 'date')

admin.site.register(Course, CourseAdmin)
admin.site.register(Section)
admin.site.register(Video)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Question, QuestionAdmin)
