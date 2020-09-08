from django import forms
from django.utils import timezone

class AvailabilityForms(forms.Form):
    start_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    end_time = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])

    def form_valid(self):
        return self.start_time > timezone.now()