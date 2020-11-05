from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["id"] = "email"
        self.fields["username"].widget.attrs["placeholder"] = "Enter email"
        self.fields["password"].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["id"] = "pwd"
        self.fields["password"].widget.attrs["placeholder"] = "Enter password"

class UserCreationForm2(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:
        model =Account
        fields = "__all__"

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Account
        fields = ("email","f_name","m_name","l_name","address_line_1","address_line_2","pin_code")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields["f_name"].widget.attrs["class"] = "form-control"
        self.fields["f_name"].widget.attrs["id"] = "fname"
        self.fields["f_name"].widget.attrs["placeholder"] = "Enter your firstname"
        self.fields["m_name"].widget.attrs["class"] = "form-control"
        self.fields["m_name"].widget.attrs["id"] = "mname"
        self.fields["m_name"].widget.attrs["placeholder"] = "Enter your middlename"
        self.fields["l_name"].widget.attrs["class"] = "form-control"
        self.fields["l_name"].widget.attrs["id"] = "lname"
        self.fields["l_name"].widget.attrs["placeholder"] = "Enter your lastname"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["id"] = "email"
        self.fields["email"].widget.attrs["placeholder"] = "Enter your email"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["id"] = "fname"
        self.fields["password1"].widget.attrs["placeholder"] = "Enter your password"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["id"] = "fname"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm your password"
        self.fields["address_line_1"].widget.attrs["class"] = "form-control"
        self.fields["address_line_1"].widget.attrs["id"] = "address1"
        self.fields["address_line_1"].widget.attrs["placeholder"] = "Address line 1"
        self.fields["address_line_2"].widget.attrs["class"] = "form-control"
        self.fields["address_line_2"].widget.attrs["id"] = "address2"
        self.fields["address_line_2"].widget.attrs["placeholder"] = "Address line 2"
        self.fields["pin_code"].widget.attrs["class"] = "form-control"
        self.fields["pin_code"].widget.attrs["id"] = "address1"
        self.fields["pin_code"].widget.attrs["placeholder"] = "Enter your pincode"


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            'using <a href="../password/">this form</a>.'
        ),
    )
    class Meta:
        model = Account
        fields = "__all__"

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class CustomerChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            'using <a href="../password/">this form</a>.'
        ),
    )

    class Meta:
        model = Customer
        fields = "__all__"

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class OwnerChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    password = ReadOnlyPasswordHashField(
        label=("Password"),
        help_text=(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            'using <a href="../password/">this form</a>.'
        ),
    )

    class Meta:
        model = Owner
        fields = "__all__"

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class CustomerSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ["email", "password"]
        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_customer = True
            if commit:
                user.save()
            return user


class RestuarantSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ["email", "password"]
        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_restaurant = True
            if commit:
                user.save()
            return user

class CustomerForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )
    class Meta:
        model = Customer
        fields = ['email','f_name','m_name','l_name','address_line_1','address_line_2','City','pin_code','profile_image']
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields["f_name"].widget.attrs["class"] = "form-control"
        self.fields["f_name"].widget.attrs["id"] = "fname"
        self.fields["f_name"].widget.attrs["placeholder"] = "Enter your firstname"
        self.fields["m_name"].widget.attrs["class"] = "form-control"
        self.fields["m_name"].widget.attrs["id"] = "mname"
        self.fields["m_name"].widget.attrs["placeholder"] = "Enter your middlename"
        self.fields["l_name"].widget.attrs["class"] = "form-control"
        self.fields["l_name"].widget.attrs["id"] = "lname"
        self.fields["l_name"].widget.attrs["placeholder"] = "Enter your lastname"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["id"] = "email"
        self.fields["email"].widget.attrs["placeholder"] = "Enter your email"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["id"] = "fname"
        self.fields["password1"].widget.attrs["placeholder"] = "Enter your password"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["id"] = "fname"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm your password"
        self.fields["address_line_1"].widget.attrs["class"] = "form-control"
        self.fields["address_line_1"].widget.attrs["id"] = "address1"
        self.fields["address_line_1"].widget.attrs["placeholder"] = "Address line 1"
        self.fields["address_line_2"].widget.attrs["class"] = "form-control"
        self.fields["address_line_2"].widget.attrs["id"] = "address2"
        self.fields["address_line_2"].widget.attrs["placeholder"] = "Address line 2"
        self.fields["pin_code"].widget.attrs["class"] = "form-control"
        self.fields["pin_code"].widget.attrs["id"] = "address1"
        self.fields["pin_code"].widget.attrs["placeholder"] = "Enter your pincode"
        self.fields["profile_image"].widget.attrs["class"] = "form-control"
        self.fields["profile_image"].widget.attrs["id"] = "profile_image"
        self.fields["profile_image"].widget.attrs["placeholder"] = "Your Profile Image"

class RestuarantForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )
    class Meta:
        model = Owner
        fields = ['email','f_name','m_name','l_name','address_line_1','address_line_2','City','pin_code','Registration_Number','pan_no','logo']
    def __init__(self, *args, **kwargs):
        super(RestuarantForm, self).__init__(*args, **kwargs)
        self.fields["f_name"].widget.attrs["class"] = "form-control"
        self.fields["f_name"].widget.attrs["id"] = "fname"
        self.fields["f_name"].widget.attrs["placeholder"] = "Enter your firstname"
        self.fields["m_name"].widget.attrs["class"] = "form-control"
        self.fields["m_name"].widget.attrs["id"] = "mname"
        self.fields["m_name"].widget.attrs["placeholder"] = "Enter your middlename"
        self.fields["l_name"].widget.attrs["class"] = "form-control"
        self.fields["l_name"].widget.attrs["id"] = "lname"
        self.fields["l_name"].widget.attrs["placeholder"] = "Enter your lastname"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["id"] = "email"
        self.fields["email"].widget.attrs["placeholder"] = "Enter your email"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["id"] = "fname"
        self.fields["password1"].widget.attrs["placeholder"] = "Enter your password"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["id"] = "fname"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm your password"
        self.fields["address_line_1"].widget.attrs["class"] = "form-control"
        self.fields["address_line_1"].widget.attrs["id"] = "address1"
        self.fields["address_line_1"].widget.attrs["placeholder"] = "Address line 1"
        self.fields["address_line_2"].widget.attrs["class"] = "form-control"
        self.fields["address_line_2"].widget.attrs["id"] = "address2"
        self.fields["address_line_2"].widget.attrs["placeholder"] = "Address line 2"
        self.fields["pin_code"].widget.attrs["class"] = "form-control"
        self.fields["pin_code"].widget.attrs["id"] = "address1"
        self.fields["pin_code"].widget.attrs["placeholder"] = "Enter your pincode"
        self.fields["Registration_Number"].widget.attrs["class"] = "form-control"
        self.fields["Registration_Number"].widget.attrs["id"] = "Registration_Number"
        self.fields["Registration_Number"].widget.attrs["placeholder"] = "Registration Number Of restaurant"
        self.fields["pan_no"].widget.attrs["class"] = "form-control"
        self.fields["pan_no"].widget.attrs["id"] = "pan_number"
        self.fields["pan_no"].widget.attrs["placeholder"] = "Pan Number"
        self.fields["logo"].widget.attrs["class"] = "form-control"
        self.fields["logo"].widget.attrs["id"] = "logo"
        self.fields["logo"].widget.attrs["placeholder"] = "Logo"
