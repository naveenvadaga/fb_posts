# your django admin
from django.contrib import admin
from .models.models import *


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, AuthorAdmin)
admin.site.register(Post, AuthorAdmin)
admin.site.register(Comment, AuthorAdmin)
admin.site.register(Reaction, AuthorAdmin)
