from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()


class UserModelTests(TestCase):
    """Tests for User model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_create_user(self):
        """Test user creation"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
    
    def test_user_email_unique(self):
        """Test that user email must be unique"""
        with self.assertRaises(Exception):
            User.objects.create_user(
                username='another',
                email='test@example.com',
                password='testpass123'
            )


class TeamModelTests(TestCase):
    """Tests for Team model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.team = Team.objects.create(
            name='Team Marvel',
            description='Marvel Superheroes',
            created_by=self.user
        )
    
    def test_create_team(self):
        """Test team creation"""
        self.assertEqual(self.team.name, 'Team Marvel')
        self.assertEqual(self.team.created_by, self.user)
    
    def test_add_team_member(self):
        """Test adding members to team"""
        user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpass123'
        )
        self.team.members.add(user2)
        self.assertIn(user2, self.team.members.all())


class ActivityModelTests(TestCase):
    """Tests for Activity model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            duration_minutes=30,
            calories_burned=300.5,
            distance_km=5.0,
            date='2025-01-01'
        )
    
    def test_create_activity(self):
        """Test activity creation"""
        self.assertEqual(self.activity.activity_type, 'running')
        self.assertEqual(self.activity.calories_burned, 300.5)


class WorkoutModelTests(TestCase):
    """Tests for Workout model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.workout = Workout.objects.create(
            user=self.user,
            title='Upper Body Strength',
            description='Full upper body workout',
            duration_minutes=45,
            difficulty='medium',
            exercises=['pushups', 'pull-ups', 'rows']
        )
    
    def test_create_workout(self):
        """Test workout creation"""
        self.assertEqual(self.workout.title, 'Upper Body Strength')
        self.assertEqual(self.workout.difficulty, 'medium')
        self.assertFalse(self.workout.completed)


class UserAPITests(APITestCase):
    """API tests for User endpoints"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_create_user_via_api(self):
        """Test creating user via API"""
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123'
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_user_profile(self):
        """Test getting current user profile"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/api/users/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITests(APITestCase):
    """API tests for Activity endpoints"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
    
    def test_create_activity(self):
        """Test creating an activity"""
        data = {
            'activity_type': 'running',
            'duration_minutes': 30,
            'calories_burned': 300,
            'distance_km': 5.0,
            'date': '2025-01-01'
        }
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_user_activities(self):
        """Test retrieving user's activities"""
        Activity.objects.create(
            user=self.user,
            activity_type='running',
            duration_minutes=30,
            calories_burned=300,
            date='2025-01-01'
        )
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITests(APITestCase):
    """API tests for Workout endpoints"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
    
    def test_create_workout(self):
        """Test creating a workout"""
        data = {
            'title': 'Upper Body Strength',
            'description': 'Full upper body workout',
            'duration_minutes': 45,
            'difficulty': 'medium',
            'exercises': ['pushups', 'pull-ups']
        }
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_mark_workout_completed(self):
        """Test marking workout as completed"""
        workout = Workout.objects.create(
            user=self.user,
            title='Test Workout',
            description='Test',
            duration_minutes=30,
            difficulty='easy'
        )
        response = self.client.post(f'/api/workouts/{workout.id}/mark_completed/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        workout.refresh_from_db()
        self.assertTrue(workout.completed)
