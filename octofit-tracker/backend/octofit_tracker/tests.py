from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration_minutes=30, calories_burned=200)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity_workout(self):
        self.assertEqual(self.activity.workout.name, 'Pushups')

    def test_leaderboard_rank(self):
        self.assertEqual(self.leaderboard.rank, 1)
