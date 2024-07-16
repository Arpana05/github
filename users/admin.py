from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from users.models import Profile

# Unregister the default User model and register it again
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)