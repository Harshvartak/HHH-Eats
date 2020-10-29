from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *
from .forms import *
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

# Register your models here.
class BaseUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ("email", "f_name","m_name","l_name")
    search_fields = ("email",)
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    filter_horizontal = ()
    ordering = ('email',)
    list_filter = ()
    exclude = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('f_name', 'm_name' ,'l_name','address_line_1','address_line_2','City','pin_code')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_customer','is_owner')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

class CustomerAdmin(UserAdmin):
    form = CustomerChangeForm
    add_form = UserCreationForm

    list_display = ("email", "f_name","m_name","l_name")
    search_fields = ("email",)
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    filter_horizontal = ()
    ordering = ('email',)
    list_filter = ()
    exclude = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('f_name', 'm_name' ,'l_name','address_line_1','address_line_2','City','pin_code','profile_image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_customer','is_owner')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

class OwnerAdmin(UserAdmin):
    form = OwnerChangeForm
    add_form = UserCreationForm

    list_display = ("email", "f_name","m_name","l_name")
    search_fields = ("email",)
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    filter_horizontal = ()
    ordering = ('email',)
    list_filter = ()
    exclude = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('f_name', 'm_name' ,'l_name','address_line_1','address_line_2','City','pin_code','profile_image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_customer','is_owner')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.unregister(Group)
admin.site.register(Account,BaseUserAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Owner,OwnerAdmin)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(orderItem)
