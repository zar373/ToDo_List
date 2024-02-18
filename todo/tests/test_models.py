from django.test import TestCase
from todo.models import Todo


class  TestModels(TestCase):
    def test_todo_model(self):
        todo = Todo.objects.create(title='test', details='test')
        self.assertEqual(todo.title, 'test')
        self.assertEqual(todo.details, 'test')
  