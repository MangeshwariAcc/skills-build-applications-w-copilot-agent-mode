from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from django.urls import reverse

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Test', duration=10, date='2025-01-01')
        self.assertEqual(str(activity), 'Test User - Test')

    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='All')
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Test Team - 100')
