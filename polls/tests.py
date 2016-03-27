from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question

class QuestionMethodTests(TestCase):
    def test_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.published_recently(), False)

    def test_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.published_recently(), False)

    def test_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.published_recently(), True)
