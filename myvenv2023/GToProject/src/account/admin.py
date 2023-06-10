from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from account.models import(CutomeAccountUser, FreeAccountUser)

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
   
    list_display = ['email','first_name','last_name','date_joined', 'last_login', 'is_active','free_user','custome_user','staff', 'admin']
    list_filter = [ 'is_active','free_user','custome_user','staff', 'admin']
    fieldsets = (
        (None, {'fields': ('email','first_name','last_name','phone_number' ,'password')}),
       
        ('Permissions', {'fields': ( 'is_active','free_user','custome_user','staff', 'admin')}),
    )
   
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name', 'password', 'password_2','profile_imag','is_active','free_user','custome_user','staff', 'admin')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    readonly_fields=('id', 'date_joined', 'last_login')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


class CutomeAccountUserAdmin(admin.ModelAdmin):
   

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email','first_name','last_name','custome_user',]
    list_filter = [ 'custome_user',]
    fieldsets = (
        (None, {'fields': ('email','first_name','last_name','phone_number' ,'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ( 'custome_user',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name', 'password', 'password_2','custome_user',)}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(CutomeAccountUser, CutomeAccountUserAdmin)

class FreeAccountUserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','free_user',]
    list_filter = [ 'free_user',]
    fieldsets = (
        (None, {'fields': ('email','first_name','last_name','phone_number' ,'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ( 'free_user',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name', 'password', 'password_2','free_user')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(FreeAccountUser, FreeAccountUserAdmin)


# Admin Site Text 

admin.site.site_header = 'Winner Project User'                   
admin.site.index_title = 'Winner Project Area'                
admin.site.site_title = 'Winner Project adminsitration' 