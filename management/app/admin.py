from django.contrib import admin
from .models import Blog,Our_team,Feature,testimony,about_us,Slide,Service,Project,Package,Appointment,FormSubmission
# Register your models here.
admin.site.register(Blog)
admin.site.register(Our_team)
# admin.site.register(Feature)
admin.site.register(testimony)
admin.site.register(about_us)
admin.site.register(Slide)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Package)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_excel_file']

    def display_excel_file(self, obj):
        return obj.excel_file.url if obj.excel_file else ''

    display_excel_file.short_description = 'Excel File'

admin.site.register(FormSubmission, FormSubmissionAdmin)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email', 'phone', 'services', 'timestamp', )
    ordering = ('-timestamp', )
admin.site.register(Appointment, AppointmentAdmin)
