from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Introduction, Work, Education, Project, Service, Testimonial
from django.contrib.auth.models import User
from .forms import *
from django.contrib import messages


def portfolio_index(request, username):
	# real_user = User.objects.filter()
	experiences = Work.objects.filter(user__username=username)
	intro = get_object_or_404(Introduction, user__username=username)
	educations = Education.objects.filter(user__username=username)
	projects = Project.objects.filter(user__username=username)
	services = Service.objects.filter(user__username=username)
	testimonals = Testimonial.objects.filter(user__username=username)

	return render(request, 'portfolio/index.html', locals())


'''
	Work Experience views - New addition(experience_new), Update(experience_update), and Delete(experience_delete)
'''
def experience_new(request, username):
	intro = get_object_or_404(Introduction, user__username=username)
	form = WorkForm(request.POST, request.FILES)
	if form.is_valid():
		new_experience = form.save(commit=False)
		new_experience.user = request.user
		new_experience.save()
		messages.success(request, "Work Experience Successfully created.")
		return HttpResponseRedirect(new_experience.get_absolute_url())
	return render(request, "portfolio/experience_form.html", locals())

def experience_update(request, username, id):
	intro = get_object_or_404(Introduction, user__username=username)
	experience = get_object_or_404(Work, user__username=username, id=id)
	form = WorkForm(request.POST or None, request.FILES or None, instance=experience)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Work Experience Successfully updated.")
		return HttpResponseRedirect(instance.get_absolute_url())
	return render(request, "portfolio/experience_form.html", locals())

def experience_delete(request, username, id):
	experience = get_object_or_404(Work, user__username=username, id=id)
	experience.delete()
	messages.success(request, "Successfully deleted")
	return redirect(experience.get_absolute_url())


'''
	Education views - New addition(education_new), Update(education_update), and Delete(education_delete)
'''

def education_new(request, username):
	intro = get_object_or_404(Introduction, user__username=username)
	form = EducationForm(request.POST, request.FILES)
	if form.is_valid():
		new_education = form.save(commit=False)
		new_education.user = request.user
		new_education.save()
		messages.success(request, "Education Successfully created.")
		return HttpResponseRedirect(new_education.get_absolute_url())
	return render(request, "portfolio/education_form.html", locals())

def education_update(request, username, id):
	intro = get_object_or_404(Introduction, user__username=username)
	education = get_object_or_404(Education, user__username=username, id=id)
	form = EducationForm(request.POST or None, request.FILES or None, instance=education)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Education Successfully updated.")
		return HttpResponseRedirect(instance.get_absolute_url())
	return render(request, "portfolio/education_form.html", locals())

def education_delete(request, username, id):
	education = get_object_or_404(Education, user__username=username, id=id)
	education.delete()
	messages.success(request, "Successfully deleted")
	return redirect(education.get_absolute_url())

'''
	Service views - New addition(service_new), Update(service_update), and Delete(service_delete)
'''

def service_new(request, username):
	intro = get_object_or_404(Introduction, user__username=username)
	form = ServiceForm(request.POST, request.FILES)
	if form.is_valid():
		new_service = form.save(commit=False)
		new_service.user = request.user
		new_service.save()
		messages.success(request, "Service Successfully created.")
		return HttpResponseRedirect(new_service.get_absolute_url())
	return render(request, "portfolio/service_form.html", locals())

def service_update(request, username, id):
	intro = get_object_or_404(Introduction, user__username=username)
	service = get_object_or_404(Service, user__username=username, id=id)
	form = ServiceForm(request.POST or None, request.FILES or None, instance=service)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Service Successfully updated.")
		return HttpResponseRedirect(instance.get_absolute_url())
	return render(request, "portfolio/service_form.html", locals())

def service_delete(request, username, id):
	service = get_object_or_404(Service, user__username=username, id=id)
	service.delete()
	messages.success(request, "Successfully deleted")
	return redirect(service.get_absolute_url())



'''
	Project views - New addition(project_new), Update(project_update), and Delete(project_delete)
'''

def project_new(request, username):
	intro = get_object_or_404(Introduction, user__username=username)
	form = ProjectForm(request.POST, request.FILES)
	if form.is_valid():
		new_project = form.save(commit=False)
		new_project.user = request.user
		new_project.save()
		messages.success(request, "Project Successfully created.")
		return HttpResponseRedirect(new_project.get_absolute_url())
	return render(request, "portfolio/project_form.html", locals())

def project_update(request, username, id):
	intro = get_object_or_404(Introduction, user__username=username)
	project = get_object_or_404(Project, user__username=username, id=id)
	form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Project Successfully updated.")
		return HttpResponseRedirect(instance.get_absolute_url())
	return render(request, "portfolio/project_form.html", locals())

def project_delete(request, username, id):
	project = get_object_or_404(Project, user__username=username, id=id)
	project.delete()
	messages.success(request, "Successfully deleted")
	return redirect(project.get_absolute_url())