from .models import Comment, SearchTerm
from django import forms
from .models import Post
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    # Hidden value to get a child's parent
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'full-width', 'placeholder': ("Enter comment's content...")}))
    parent = forms.CharField(widget=forms.HiddenInput(
        attrs={'class': 'parent'}), required=False)

    class Meta:
        model = Comment
        fields = ['content', ]


class PostForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': ('full-width'), 'placeholder': ("Enter post's title")}))
    body = RichTextUploadingField()
    publish = forms.DateField(widget=forms.DateInput(
        attrs={'placeholder': 'Date e.g. 2020-07-29', 'type': 'date'}))

    class Meta:
        model = Post
        fields = ['title', 'image', 'category',
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


class SearchForm(forms.ModelForm):
    """ form class for accepting search terms """
    query = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'search', 'class': ('header__search-field')}))

    class Meta:
        model = SearchTerm
        fields = ('query',)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        default_text = 'Search sirneijblog.com'
        self.fields['query'].widget.attrs['placeholder'] = default_text
        self.fields['query'].widget.attrs['title'] = 'Search for:'
    include = ('query',)
