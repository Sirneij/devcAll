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

#Education forms
class WorkForm(forms.ModelForm):
	commencement = forms.DateField(widget=forms.DateInput(attrs={'class': ('full-width'), 'placeholder': ("Enter Commencement date")}))
	end = forms.DateField(widget=forms.DateInput(attrs={'class': ('full-width'), 'placeholder': ("Enter End date")}))
	company_name = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ("Enter Company name")}))
	position = forms.CharField(widget=forms.TextInput(attrs={'class': ('full-width'), 'placeholder': ("Enter Position held")}))
	description = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))
	class Meta:
		model = Work
		fields = ('commencement', 'end', 'company_name', 'position', 'description')