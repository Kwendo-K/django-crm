"""
creating a registration form
"""
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record


class RegisterUser(UserCreationForm):
    """creating form attributes"""

    # first_name = forms.CharField(max_length=100, widget=forms.TextInput())
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput())

    class Meta:
        """model user as the database"""
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(RegisterUser, self).__init__(*args, **kwargs)


class AddRecordForm(forms.ModelForm):
    """Form to add records to the database"""

    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
        label="",
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "last Name", "class": "form-control"}
        ),
        label="",
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "emailexample@gmail.com", "class": "form-control"}
        ),
        label="",
    )
    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "phone", "class": "form-control"}
        ),
        label="",
    )
    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "address", "class": "form-control"}
        ),
        label="",
    )
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "city", "class": "form-control"}
        ),
        label="",
    )
    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "state", "class": "form-control"}
        ),
        label="",
    )
    zip_code = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "zipcode", "class": "form-control"}
        ),
        label="",
    )

    class Meta:
        model = Record
        exclude = ("user",)
