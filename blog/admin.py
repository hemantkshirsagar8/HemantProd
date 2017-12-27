from django.contrib import admin
from django import forms
from blog.models import *
from django.conf import settings
from fluent_contents.models import *
from fluent_contents.models.fields import PlaceholderField, PlaceholderRelation, ContentItemRelation
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class BlogForm(forms.ModelForm):
    Comments = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    list_display = ('BlogID', 'Heading', 'Comments', 'Status', 'CreateDate')
    search_fields = ('BlogID', 'Heading', 'Comments', 'Status', 'CreateDate')

admin.site.register(Blog, BlogAdmin)