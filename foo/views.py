from django.forms import forms, models
from formset.widgets import Selectize
from formset.views import FormView





class ConferenceForm(forms.Form):
    venue = models.ChoiceField(
        choices=[
            (2009, "Praha"),
            (2010, "Berlin"),
            (2011, "Amsterdam"),
            (2012, "Zürich"),
            (2013, "Warszawa"),
            (2014, "Île des Embiez"),
            (2015, "Cardiff"),
            (2016, "Budapest"),
            (2017, "Firenze"),
            (2018, "Heidelberg"),
            (2019, "København"),
            (2020, "Virtual"),
            (2022, "Porto"),
            (2023, "Edinburgh"),
            (2024, "Vigo"),
            (2025, "Dublin"),
        ],
        widget=Selectize(),
    )

class Index(FormView):
    form_class = ConferenceForm
    template_name = "index.html"

class Form(FormView):
    form_class = ConferenceForm
    template_name = "form.html"
