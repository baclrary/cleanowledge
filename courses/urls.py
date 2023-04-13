from django.urls import path

from . import views

app_name = "courses"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="courses"),
    path("test/", views.TestTemplate.as_view(), name="test"),

    path("create/", views.CourseCreateView.as_view(), name="course-create"),
    path("<int:pk>/", views.CourseDetailView.as_view(), name="course-detail"),
    path("<int:pk>/update", views.CourseUpdateView.as_view(), name="course-update"),
    path("<int:pk>/delete", views.CourseDeleteView.as_view(), name="course-delete"),
    path("<int:pk>/members/", views.CourseMembersDetailView.as_view(), name="courses-members"),
    path("<int:pk>/enroll/", views.enroll_course, name="course-enroll"),
    path("<int:pk>/leave/", views.leave_course, name="course-leave"),
    path("<int:pk>/add_teacher/<int:tpk>/", views.add_teacher, name="course-add-teacher"),
    path("<int:pk>/remove_teacher/<int:tpk>/", views.remove_teacher, name="course-remove-teacher"),
    path("<int:pk>/remove_member/<int:mpk>/", views.remove_member, name="course-remove-member"),
    path("<int:pk>/sections/", views.SectionListView.as_view(), name="sections"),
    path("<int:pk>/sections/<int:spk>/", views.SectionDetailView.as_view(), name="section-detail"),
    path("<int:pk>/sections/create/", views.SectionCreateView.as_view(), name="section-create"),
    path("<int:pk>/sections/<int:spk>/update/", views.SectionUpdateView.as_view(), name="section-update"),
    path("<int:pk>/sections/<int:spk>/delete/", views.SectionDeleteView.as_view(), name="section-delete"),
    path("<int:pk>/tasks/<slug:slug>/", views.task_detail_view, name="course-task-detail"),
]
