from django.contrib import admin
from .models import Introduction, Work, Education, Project, Service, Testimonial

# Register your models here.
@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'school_name', 'degree_type')
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'caption')
@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('user', 'title',)
@admin.register(Testimonial)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('recommender_name', 'recommender_office')