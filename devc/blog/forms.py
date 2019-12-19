from .models import Comment
from django import forms
from .models import Post
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    #Hidden value to get a child's parent
    content = forms.CharField(required=True, widget=CKEditorWidget(config_name='awesome_ckeditor'))
    parent = forms.CharField(widget=forms.HiddenInput(attrs={'class': 'parent'}), required=False)
    
    class Meta:
        model = Comment
        fields = ['content',]


class PostForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': ('full-width'), 'placeholder': ("Enter post's title")}))
    body = RichTextUploadingField()
    publish = forms.DateField()

    class Meta:
        model = Post
        fields = ['title', 'author', 'image', 'category',
                  'body', 'publish', 'status', 'tags', ]


class UpdatePostForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': ('full-width')}))
    body = RichTextUploadingField()
    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': ('full-width')}))

    class Meta:
        model = Post
        fields = ['title', 'image', 'body', 'status', 'tags', ]


class SearchForm(forms.Form):
    query = forms.CharField()
