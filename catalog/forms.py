from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now & 4 weeks (3 default)")

    def clean_renewal_date(self):
        date = self.cleaned_data['renewal_date']

        if date < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past.'))

        if date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Cannot set renewal date of more than 4 weeks'))

        return date
