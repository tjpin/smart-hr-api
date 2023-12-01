from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import StaffUser
from .staff import Staff


class StaffUserCreationForm(UserCreationForm):
    class Meta:
        model = StaffUser
        fields = "__all__"


class StaffUserChangeForm(UserChangeForm):
    class Meta:
        model = StaffUser
        fields = "__all__"


class StaffCreateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"
