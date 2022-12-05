from django.contrib import admin
from .models import Email, Service, Password, Username, PasswordService

@admin.register(Email)
class EmailManager(admin.ModelAdmin):
    list_display = ["alias", "email", "created_on"]
    seaarch_field = ["alias", "email"]
    date_hierarchy = "created_on"
    ordering = ["-created_on"]
    show_full_result_count = True
    list_display_links = ["alias", "email", "created_on"]


@admin.register(Service)
class ServiceManager(admin.ModelAdmin):
    list_display = ["service", "created_on"]
    seaarch_field = ["service"]
    date_hierarchy = "created_on"
    ordering = ["-created_on"]
    show_full_result_count = True
    list_display_links = ["service", "created_on"]


@admin.register(Password)
class PasswordManager(admin.ModelAdmin):
    list_display = ["password", "created_on"]
    seaarch_field = ["password"]
    date_hierarchy = "created_on"
    ordering = ["-created_on"]
    show_full_result_count = True
    list_display_links = ["password", "created_on"]


@admin.register(Username)
class UsernameManager(admin.ModelAdmin):
    list_display = ["username", "created_on"]
    seaarch_field = ["username"]
    date_hierarchy = "created_on"
    ordering = ["-created_on"]
    show_full_result_count = True
    list_display_links = ["username", "created_on"]

@admin.register(PasswordService)
class PasswordServiceManager(admin.ModelAdmin):
    list_display = ["service", "email", "password", "username", "description", "created_on"]
    seaarch_field = ["email", "password", "service", "username"]
    date_hierarchy = "created_on"
    ordering = ["-created_on"]
    show_full_result_count = True
    list_display_links = ["email", "password", "service",]
    list_filter = ["service", "email"]