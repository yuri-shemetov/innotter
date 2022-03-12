from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['subscriber', 'follower', 'follow_requests', ]


admin.site.register(Subscriber, SubscriberAdmin)
