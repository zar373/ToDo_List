from django.test import SimpleTestCase
from todo.forms import TodoForm
from django.utils import timezone
class TestForms(SimpleTestCase):
    def test_todo_form_is_valid(self):
        form = TodoForm(data={'title': 'test', 'details': 'test','date': timezone.now()})
        self.assertTrue(form.is_valid())

    