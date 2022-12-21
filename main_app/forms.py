from django.contrib.admin.widgets import AdminDateWidget
from django.db.models import DateField
from django.forms import ModelForm
from django import forms
from main_app.models import Associate
from django.forms.widgets import NumberInput


class AddAssociateForm(ModelForm):
    date_of_joining = forms.DateTimeField(label="Date", required=True, widget=NumberInput(attrs={'type':'date'}))

    class Meta:
        model = Associate
        fields = '__all__'
