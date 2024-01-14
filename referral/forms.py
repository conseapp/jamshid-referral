from django import forms
from .models import Referral


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ('generated_date',)