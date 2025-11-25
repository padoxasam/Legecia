from django.contrib import admin
from .models import AccessLog

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ("access_id", "ip_address", "login_start", "logout", "successful_log")
    list_filter = ("successful_log",)
    search_fields = ("ip_address", "device_info")
