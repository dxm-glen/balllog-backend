from django.contrib import admin
from .models import Match

@admin.register(Match) # match 모델에 대해서 다룰 거라는 데코레이터
class MatchAdmin(admin.ModelAdmin):
    
    list_display = (
        "type", "host_point", "guest_point", "start_time", "end_time",
    )
    list_filter = (
        "type", "end_time",
    )
    search_fields = ("type",)