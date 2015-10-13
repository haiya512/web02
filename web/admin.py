from django.contrib import admin
from web.models import *
'''
class AuthorAdmin(admin.ModelAdmin):
        list_display = ("last_name","first_name","email")
        search_fields = ('email',)
class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'publisher', 'publication_date')
        list_filter = ('publication_date','title', 'publisher')
        search_fields = ('tile',)
        date_hierarchy = 'publication_date'
        filter_horizontal = ('authors',)
        raw_id_fields = ('publisher',)
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book)
'''
#class AuthIpAndRemoteUserAdmin(admin.ModelAdmin):
class OpsLogAdmin(admin.ModelAdmin):
    list_display = ('log_type','finish_date','log_type','tri_user','run_user','cmd','total_task','success_num','failed_num','track_mark','note')
class LogAdmin(admin.ModelAdmin):
	list_display = ('user','ip','event_type','cmd','event_log','result','track_mark')	
admin.site.register(IP)
admin.site.register(Group)
admin.site.register(RemoteUser)
admin.site.register(TriaquaeUser)
admin.site.register(AuthByIpAndRemoteUser)
admin.site.register(OpsLogTemp,LogAdmin)
admin.site.register(OpsLog,OpsLogAdmin)
