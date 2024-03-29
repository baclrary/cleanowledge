from django.contrib import admin

from .models import Course, Goal, Section, Task


class CourseAdmin(admin.ModelAdmin):
    readonly_fields = ("created_date", "updated_date")


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # new


class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created_date", "updated_date")


class GoalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Course, CourseAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Goal, GoalAdmin)
