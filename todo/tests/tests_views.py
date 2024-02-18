# # from django.test import TestCase, Client
# # from django.urls import reverse
# # from todo.models import Todo
# # import json

# # class TestViews(TestCase):

# #     def setUp(self):
# #         self.client= Client()
# #         self.todo_url = reverse('todo')
# #         self.del_url = reverse('del', args=['1'])
# #         self.Test1 = Todo.objects.create(title='test',
# #         description='test',
# #         status='test')


# #     def test_todo_GET(self):
# #         # # setup code 
# #         # client= Client()
# #         # testing code
# #         response= self.client.get(self.todo_url)
        
# #         self.assertEquals(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'todo/index.html')

# #     def test_del_GET(self):
# #         category1 = 

# from django.test import TestCase
# from django.urls import reverse
# from todo.models import Todo

# class TodoViewsTest(TestCase):

#     def test_index_view_with_no_items(self):
#         response = self.client.get(reverse('todo'))
#         self.assertEqual(response.status_code, 200)
#         self.assertQuerysetEqual(response.context['list'], [])

#     def test_index_view_with_items(self):
#         # Create a Todo item
#         Todo.objects.create(title='Test Item')

#         response = self.client.get(reverse('todo'))
#         self.assertEqual(response.status_code, 200)
#         # self.assertQuerysetEqual(response.context['list'], ['<Todo: Test Item>'])

#     def test_add_item(self):
#         response = self.client.post(reverse('todo'), {'title': 'New Item'})
#         self.assertEqual(response.status_code, 302)  # Redirect status
#         self.assertEqual(Todo.objects.count(), 1)
#         self.assertEqual(Todo.objects.first().title, 'New Item')

#     def test_remove_item(self):
#         # Create a Todo item
#         todo_item = Todo.objects.create(title='Test Item')

#         response = self.client.post(reverse('remove', args=['1']))
#         self.assertEqual(response.status_code, 302)  # Redirect status
#         self.assertEqual(Todo.objects.count(), 0)



