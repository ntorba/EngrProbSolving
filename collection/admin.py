from django.contrib import admin

# Register your models here.
from collection.models import Thing
from collection.models import Project

# and register it
#admin.site.register(Thing)
#admin.site.register(Projects)

class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Thing, ThingAdmin)
admin.site.register(Project, ProjectAdmin)
