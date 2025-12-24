from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin interface for User model"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Admin interface for Team model"""
    list_display = ['name', 'created_by', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name', 'description']
    filter_horizontal = ['members']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Admin interface for Activity model"""
    list_display = ['user', 'activity_type', 'date', 'duration_minutes', 'calories_burned']
    list_filter = ['activity_type', 'date', 'created_at']
    search_fields = ['user__username', 'description']
    ordering = ['-date', '-created_at']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    """Admin interface for Leaderboard model"""
    list_display = ['user', 'rank', 'total_calories', 'total_distance', 'total_activities']
    list_filter = ['team', 'updated_at']
    search_fields = ['user__username']
    ordering = ['rank', '-total_calories']
    readonly_fields = ['user', 'total_calories', 'total_distance', 'total_activities', 'updated_at']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """Admin interface for Workout model"""
    list_display = ['title', 'user', 'difficulty', 'scheduled_date', 'completed']
    list_filter = ['difficulty', 'completed', 'scheduled_date', 'created_at']
    search_fields = ['title', 'user__username', 'description']
    ordering = ['-created_at']
