from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Associate


@admin.register(Associate)
class AssociateAdmin(ImportExportModelAdmin):
    model = Associate
    # list_filter = ('device_type', 'platform', 'vendor')
    list_display = [f.name for f in Associate._meta.fields]
