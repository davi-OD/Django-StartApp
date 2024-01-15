from django.contrib import admin
from . import models

# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    # pass
    list_display = ('title',)


admin.site.register(models.Notes, NotesAdmin)
