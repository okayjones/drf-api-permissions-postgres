from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Task


class TaskTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username='testuser1', password='pass')
        testuser1.save()

        test_task = Task.objects.create(
            owner=testuser1,
            name='Drink water',
            description='do this more'
        )
        test_task.save()

    def test_task_content(self):
        task = Task.objects.get(id=1)
        actual_owner = str(task.owner)
        actual_name = str(task.name)
        actual_description = str(task.description)
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_name, 'Drink water')
        self.assertEqual(actual_description, 'do this more')
