from django.contrib import admin
from .models import Scoreboard,ScoreboardTags


class ScoreboardAdmin(admin.ModelAdmin): 
    list_display = ('machine_id', 'display', 'running', 'percentage', 'display_tags')
    ordering = ('machine_id',)

    def display_tags(self, obj):
        return obj.tag_id.tag


class ScoreboardTagsAdmin(admin.ModelAdmin): 
    list_display = ('tag', 'style')


admin.site.register(Scoreboard, ScoreboardAdmin)
admin.site.register(ScoreboardTags, ScoreboardTagsAdmin)
