from datetime import datetime

from import_export import resources
from .models import Referral


class ReferralResource(resources.ModelResource):
    class Meta:
        model = Referral
        fields = ('id', 'generated_date', 'code')
