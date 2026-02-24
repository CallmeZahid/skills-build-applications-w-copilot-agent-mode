from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        squats = Workout.objects.create(name='Squats', description='Lower body', difficulty='Medium')

        # Create activities
        Activity.objects.create(user=users[0], workout=pushups, duration_minutes=30, calories_burned=200)
        Activity.objects.create(user=users[1], workout=squats, duration_minutes=40, calories_burned=300)
        Activity.objects.create(user=users[2], workout=pushups, duration_minutes=25, calories_burned=180)
        Activity.objects.create(user=users[3], workout=squats, duration_minutes=35, calories_burned=250)

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[1], score=90, rank=2)
        Leaderboard.objects.create(user=users[2], score=80, rank=3)
        Leaderboard.objects.create(user=users[3], score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
