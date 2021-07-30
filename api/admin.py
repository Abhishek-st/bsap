from django.contrib import admin
from django.db.models.fields.json import CaseInsensitiveMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Climate)
class ClimateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
