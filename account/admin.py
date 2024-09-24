from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm
# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     list_display = ('username','email','age','is_staff')
#     fieldsets = UserAdmin.fieldsets + (
#         (None,{'fields':('age',)}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('age',)}),
#     )
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'age', 'is_staff']

    fieldsets = (
        (None, {"fields": ("username", "password")}),  # Corrected 'Fields' to 'fields'
        ("Personal info", {"fields": ("first_name", "last_name", "email", "age")}),
        ("Permissions", {
            "fields": (  # Corrected 'Fields' to 'fields'
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "age")
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)