from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .resource import ReferralResource
from .models import Referral
from .utils import code_generator
from .forms import ReferralForm


class ReferralAdmin(ImportExportModelAdmin):
    resource_class = ReferralResource
    list_display = ['id', 'code', 'generated_date', 'inserted_date', 'expired_date', 'used']
    ordering = ['inserted_date']
    form = ReferralForm
    readonly_fields = ['code']

    def save_model(self, request, obj, form, change):
        # Set the value for the field you want to auto-generate
        obj.code = code_generator()  # Replace with your logic to generate the value
        super().save_model(request, obj, form, change)


admin.site.register(Referral, ReferralAdmin)
