# apart/admin.py

from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('nama', 'NIM', 'kelas', 'role', 'image')
    search_fields = ('nama', 'NIM', 'kelas', 'role')

# Alternatively, you can use:
# admin.site.register(TeamMember)
