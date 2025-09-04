# backend/companies/admin.py
from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display   = ("name", "industry", "size", "location")
    search_fields  = ("name",)
    list_filter    = ("industry", "size")
