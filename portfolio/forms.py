from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Introduction, Work, Education, Project, Service, Testimonial
#Education forms
class EducationForm(forms.ModelForm):
	commencement = forms.DateField(widget=forms.DateInput(attrs={'class': ('full-width'), 'placeholder': ("Enter Commencement date")}))
	end = forms.DateField(widget=forms.DateInput(attrs={'class': ('full-width'), 'placeholder': ("Enter End date")}))
	school_name = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ("Enter School name")}))
	# degree_type = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width')}))
	description = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
	class Meta:
		model = Education
		fields = ('commencement', 'end', 'school_name', 'degree_type', 'description')

#Work forms
class WorkForm(forms.ModelForm):
	commencement = forms.DateField(widget=forms.DateInput(attrs={'class': ('full-width'), 'placeholder': ("Enter Commencement date")}))
	end = forms.DateField(widget=forms.DateInput(attrs={'class': ('full-width'), 'placeholder': ("Enter End date")}))
	company_name = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ("Enter Company name")}))
	position = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ("Enter Position held")}))
	description = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
	class Meta:
		model = Work
		fields = ('commencement', 'end', 'company_name', 'position', 'description')
#Service forms
class ServiceForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ("Enter Service title")}))
	description = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
	class Meta:
		model = Service
		fields = ('title', 'description')

#Project forms
class ProjectForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ("Enter project title")}))
	category = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ("Enter project category")}))
	caption = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
	class Meta:
		model = Project
		fields = ('title', 'category', 'caption', 'project_pic')