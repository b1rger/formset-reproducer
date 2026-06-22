from django.forms import fields, forms, models, widgets
from formset.widgets import Selectize
from testapp.models import County

class CountyForm(forms.Form):
    county = models.ModelChoiceField(
        queryset=County.objects.select_related('state'),
        widget=Selectize(
            search_lookup='name__icontains',
            placeholder="Select a county",
        ),
    )
