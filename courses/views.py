from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from django.views import generic

from users.models import User

from .forms import CourseCreateModelForm, CourseUpdateForm, SectionCreateForm, TaskForm
from .models import Course, Section, Task


class TestTemplate(generic.TemplateView):
    template_name = "courses/test.html"


class HomePage(generic.TemplateView):
    template_name = "menu.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"


class UpdatesPage(generic.TemplateView):
    template_name = "updates.html"


# COURSE #
class CourseListView(generic.list.ListView, LoginRequiredMixin):
    template_name = "courses/courses_list.html"
    context_object_name = "courses"
    model = Course


class CourseCreateView(generic.CreateView, LoginRequiredMixin):
    template_name = "courses/create_course.html"
    form_class = CourseCreateModelForm

    def form_valid(self, form):
        course = form.save(commit=False)
        course.owner = self.request.user
        course.save()
        course.members.add(course.owner)
        course.teachers.add(course.owner)
        return super().form_valid(form)


class CourseDetailView(generic.detail.DetailView):
    template_name = "courses/detail_course.html"
    context_object_name = "course"
    model = Course


class CourseUpdateView(generic.UpdateView):
    model = Course
    form_class = CourseUpdateForm
    template_name = "courses/course_update.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = get_object_or_404(Course, id=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("courses:course-update", kwargs={"pk": self.kwargs["pk"]})


class CourseDeleteView(generic.DeleteView):
    model = Course
    success_url = reverse_lazy("courses:courses")
    template_name = "courses/course_confirm_delete.html"


class CourseMembersDetailView(generic.detail.DetailView, LoginRequiredMixin):
    template_name = "courses/course_members.html"
    context_object_name = "course"
    model = Course


# SECTION #


class BaseSectionView:
    def get_course(self):
        if not hasattr(self, "_course"):
            self._course = get_object_or_404(Course, id=self.kwargs["pk"])
        return self._course


class SectionListView(BaseSectionView, generic.ListView):
    model = Section
    context_object_name = "sections"
    template_name = "courses/section/sections_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.get_course()
        return context

    def get_queryset(self):
        course = self.get_course()
        return course.sections.all()


class SectionDetailView(BaseSectionView, generic.DetailView):
    model = Section
    context_object_name = "section"
    template_name = "courses/section/section_detail.html"

    def get_object(self):
        return get_object_or_404(Section, course_id=self.kwargs["pk"], id=self.kwargs["spk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.get_course()
        return context


class SectionCreateView(BaseSectionView, generic.CreateView):
    model = Section
    form_class = SectionCreateForm
    template_name = "courses/section/section_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.get_course()
        return context

    def form_valid(self, form):
        form.instance.course = self.get_course()
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.cleaned_data["title"])
        return super().form_valid(form)


class SectionUpdateView(BaseSectionView, generic.UpdateView):
    model = Section
    form_class = SectionCreateForm
    template_name = "courses/section/section_update.html"

    def get_object(self):
        return get_object_or_404(Section, course_id=self.kwargs["pk"], id=self.kwargs["spk"])

    def form_valid(self, form):
        form.instance.course = self.get_course()
        form.instance.owner = self.request.user
        form.instance.slug = slugify(form.cleaned_data["title"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.get_course()
        return context


class SectionDeleteView(BaseSectionView, generic.DeleteView):
    model = Section
    template_name = "courses/section/section_confirm_delete.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Section, course_id=self.kwargs["pk"], id=self.kwargs["spk"])

    # link 'cancel' button in template with a detail view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["course"] = self.get_course()
        return context

    def get_success_url(self):
        return reverse_lazy("courses:sections", kwargs={"pk": self.kwargs["pk"]})


# Task #


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "courses/task/task_list.html"

    def get_section(self):
        return get_object_or_404(Section, id=self.kwargs["spk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = self.get_section()
        return context

    def get_queryset(self):
        section = self.get_section()
        return section.tasks.all()


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "courses/task/task_create.html"
    success_message = "Task created successfully"

    def get_section(self):
        if not hasattr(self, "_section"):
            self._section = get_object_or_404(Section, id=self.kwargs["spk"])
        return self._section

    def form_valid(self, form):
        form.instance.owner = self.request.user
        print(form.cleaned_data)
        # make in model and call through model
        task = form.save(commit=False)
        task.slug = slugify(task.title + "-" + str(task.pk))
        task.save()
        section = self.get_section()
        section.tasks.add(task)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = self.get_section()
        return context

    def get_success_url(self):
        return reverse_lazy("courses:section-detail", kwargs={"pk": self.kwargs["pk"], "spk": self.kwargs["spk"]})


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "courses/task/task_update.html"
    success_message = "Task updated successfully"

    def get_object(self, queryset=None):
        section_pk = self.kwargs.get("spk")
        task_slug = self.kwargs.get("slug")
        section = get_object_or_404(Section, id=section_pk)
        task = get_object_or_404(section.tasks, slug=task_slug)
        return task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section_pk = self.kwargs.get("spk")
        section = get_object_or_404(Section, id=section_pk)
        context["section"] = section
        return context

    def get_success_url(self):
        return reverse_lazy(
            "courses:task-detail",
            kwargs={"pk": self.kwargs["pk"], "spk": self.kwargs["spk"], "slug": self.kwargs["slug"]},
        )


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "courses/task/task_confirm_delete.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Task, slug=self.kwargs["slug"])

    def get_section(self, queryset=None):
        return get_object_or_404(Section, id=self.kwargs["spk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["section"] = self.get_section()
        return context

    def get_success_url(self):
        return reverse_lazy("courses:section-detail", kwargs={"pk": self.kwargs["pk"], "spk": self.kwargs["spk"]})

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        response = super().dispatch(request, *args, **kwargs)
        if request.method == "POST":
            messages.success(request, 'Task "{}" deleted successfully'.format(task.title))
            return redirect(self.get_success_url())
        return response


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = "task"
    template_name = "courses/task/task_article_detail.html"

    def get_object(self, queryset=None):
        section_pk = self.kwargs.get("spk")
        task_slug = self.kwargs.get("slug")
        section = get_object_or_404(Section, id=section_pk)
        task = get_object_or_404(section.tasks, slug=task_slug)
        return task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section_pk = self.kwargs.get("spk")
        section = get_object_or_404(Section, id=section_pk)
        context["section"] = section
        return context


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
