from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo.views import index, remove
class TestUrls(SimpleTestCase):
    def test_todo_url_is_resolved(self):
        url = reverse('todo')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
        
    def test_todo_url_is_resolved(self):
        url = reverse('del', args=['1'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, remove)