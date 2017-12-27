
from pioneer.models import *
from django.contrib import admin


class MemberAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'flat_no', 'wing', 'phase')
	search_fields = ('flat_no','last_name')

admin.site.register(Member, MemberAdmin)
