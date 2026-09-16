from django.contrib import admin
from .models import UserProfile, Project
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'get_role', 'is_staff')

    @admin.display(ordering='profile__role', description='Role')
    def get_role(self, user):
        try:
            return user.profile.role
        except:
            return "-"

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'title')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email', 'skills')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget', 'posted_by', 'status')