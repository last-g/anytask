from invites.models import Invite
from django.contrib import admin

class InviteAdmin(admin.ModelAdmin):
    list_display = ('generated_by', 'group', 'key', 'invited_user')
    list_filter = ('group',)
    search_fields = ('generated_by__username', 'group__name', 'key', 'invited_user__username')

admin.site.register(Invite, InviteAdmin)

