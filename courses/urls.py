# # courses/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.course_list, name='course_list'),
#     path('<int:course_id>/', views.course_detail, name='course_detail'),
#     path('', views.course_list, name='course_list'),
#     path('<int:course_id>/', views.course_detail, name='course_detail'),
#     path('<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
# ]

# # # udemy_clone/urls.py

# # from django.contrib import admin
# # from django.urls import path, include

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('courses/', include('courses.urls')),
# # ]
# courses/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
]
