from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .forms import CourseCreateModelForm
from .models import Course, Section, Task
from users.models import User


class HomePage(generic.TemplateView):
    template_name = 'menu.html'


class AboutPage(generic.TemplateView):
    template_name = 'about.html'


class UpdatesPage(generic.TemplateView):
    template_name = 'updates.html'


class CourseListView(generic.list.ListView, LoginRequiredMixin):
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'
    model = Course


class CourseCreateView(generic.CreateView, LoginRequiredMixin):
    template_name = 'courses/create_course.html'
    form_class = CourseCreateModelForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.owner = self.request.user
        # if form.is_valid():
        instance.save()
        self.product = instance
        self.product.members.add(instance.owner)
        self.product.teachers.add(instance.owner)
        return HttpResponseRedirect(reverse('courses:course-detail', kwargs={'pk': self.product.pk}))


class CourseCreateSuccess(generic.TemplateView):
    template_name = 'courses/create_course_success.html'


class CourseDetailView(generic.detail.DetailView):
    template_name = 'courses/detail_course.html'
    context_object_name = 'course'
    model = Course


class CourseMembersDetailView(generic.detail.DetailView, LoginRequiredMixin):
    template_name = 'courses/course_members.html'
    context_object_name = 'course'
    model = Course


# class SectionDetailView(generic.detail.DetailView):
#     template_name = 'courses/task_article_detail.html'
#     context_object_name = 'section'
#     model = Section


def section_detail_view(request, pk, slug):
    course = Course.objects.get(id=pk)
    section = course.sections.get(slug=slug)
    print(request.path)
    return render(request, 'courses/section_detail.html', context={'section': section, 'course': course})


def task_detail_view(request, pk, slug):
    section = Section.objects.get(id=pk)
    task = section.tasks.get(slug=slug)
    return render(request, 'courses/task_article_detail.html', context={'task': task, 'section': section})


@login_required
def enroll_course(request, pk):
    course = Course.objects.get(pk=pk)
    user = request.user

    course.members.add(user)
    return HttpResponse("Done!")


@login_required
def leave_course(request, pk):
    course = Course.objects.get(pk=pk)
    user = request.user

    course.members.remove(user)
    return HttpResponse("Done!")


@login_required
def add_teacher(request, pk, tpk):
    course = Course.objects.get(pk=pk)
    teacher = User.objects.get(id=tpk)

    course.teachers.add(teacher)

    return HttpResponse(f"Teacher {teacher} was added")


@login_required
def remove_teacher(request, pk, tpk):
    course = Course.objects.get(pk=pk)
    teacher = User.objects.get(id=tpk)

    course.teachers.remove(teacher)

    return HttpResponse(f"Teacher {teacher} was removed")


@login_required
def remove_member(request, pk, mpk):
    course = Course.objects.get(pk=pk)
    member = User.objects.get(id=mpk)

    course.teachers.remove(member)
    course.members.remove(member)

    return HttpResponse(f"Student {member} was expelled")


# def ban_member(request, pk, spk):
#     course = Course.objects.get(pk=pk)
#     student = User.objects.get(id=spk)

#     course.members.remove(student)

#     return HttpResponse(f"Student {student} was expelled")

    # user = User.objects.get(id=pk)
