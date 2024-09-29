# admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Coach, Player, Team, Schedule  # Import your models

# Coach Resource
class CoachResource(resources.ModelResource):
    class Meta:
        model = Coach

class CoachAdmin(ImportExportModelAdmin):
    resource_class = CoachResource
    list_display = ('user','phone')

# Player Resource
class PlayerResource(resources.ModelResource):
    class Meta:
        model = Player

class PlayerAdmin(ImportExportModelAdmin):
    resource_class = PlayerResource
    list_display = ('name', 'age', 'sport')
    list_filter = ('age', 'sport')

# Team Resource
class TeamResource(resources.ModelResource):
    class Meta:
        model = Team

class TeamAdmin(ImportExportModelAdmin):
    resource_class = TeamResource
    list_display = ('name', 'coach')
    list_filter = ('coach',)

# Schedule Resource
class ScheduleResource(resources.ModelResource):
    class Meta:
        model = Schedule

class ScheduleAdmin(ImportExportModelAdmin):
    resource_class = ScheduleResource
    list_display = ('team', 'date', 'event_type','location')
    list_filter = ('location',)

# Register models to the admin site
admin.site.register(Coach, CoachAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Schedule, ScheduleAdmin)
