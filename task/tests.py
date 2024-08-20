from django.test import TestCase
from django.urls import reverse

from task.models import Tag
from task.forms import TaskForm


class TagTest(TestCase):
    def setUp(self):
        self.model_instance = Tag.objects.create(name='Cleaning')

    def test_model_creation(self):
        self.assertTrue(isinstance(self.model_instance, Tag))
        self.assertEqual(self.model_instance.__str__(), 'Cleaning')

    def test_model_field(self):
        self.assertEqual(self.model_instance.name, 'Cleaning')


class ViewsTest(TestCase):
    def test_view_url_exists(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('task-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_form.html')

class TaskFormTest(TestCase):

    def test_view_returns_correct_context(self):
        response = self.client.get(reverse('task-add'))
        self.assertIsInstance(response.context['form'], TaskForm)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_form.html')
