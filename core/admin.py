from django.contrib import admin
from core.models import (Country, ProvinceState,
    Institute, Specialization, Badge, Encouragement,
    Feedback, Skill, SkillRating, WebFile)


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified_time',)
    list_filter = ('modified_time',)
    search_fields = ['name']


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified_time',)
    list_filter = ('modified_time',)
    search_fields = ['name']


admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Badge)
admin.site.register(Encouragement)
admin.site.register(Feedback)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillRating)
admin.site.register(Country)
admin.site.register(ProvinceState)
admin.site.register(Institute)
admin.site.register(WebFile)
