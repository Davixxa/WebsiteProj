from django.contrib import admin
from .models import Project
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

admin.site.register(Project, MarkdownxModelAdmin)
