from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from bson import ObjectId
class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(
            _id=ObjectId(),
            title="Test Task",
            description="Test description",
            completed=False
        )
        
    # Test case to get all tasks from To Do
    
    def test_get_all_tasks(self):
        response = self.client.get('/api/tasks/')
        tasks = response.json() 
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(tasks), 1)
        task_titles = [task['title'] for task in tasks]
        self.assertIn('Test Task', task_titles)
    
    # Test case to create a new task
    
    def test_create_task(self):
       
        task_data = {
            "_id": str(ObjectId()), 
            "title": "New Task",
            "description": "Description for the new task"
        }
    
        # Send POST request to create a new task
        response = self.client.post('/api/tasks/', task_data, format='json')
        # print(response.json())
     
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        
        task = Task.objects.get(title='New Task')
        self.assertEqual(task.title, 'New Task')
        self.assertEqual(task.description, 'Description for the new task')

        
        self.assertEqual(response.json()['title'], task_data['title'])
        self.assertEqual(response.json()['description'], task_data['description'])
    
    # Test case for updating a particular task from To Do
    
    def test_update_task(self):
        new_title = "Updated Task Title"
        new_description = "Updated Task Description"
        task_id = str(self.task._id)  

        updated_data = {
            "title": new_title,
            "description": new_description
        }

        response = self.client.put(f'/api/tasks/{task_id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], new_title)
        self.assertEqual(response.json()['description'], new_description)
        self.assertTrue(ObjectId.is_valid(response.json().get('_id'))) 
    
    
    # Test case for deleting all the tasks from To Do
    def test_delete_all_tasks(self):
        response = self.client.delete('/api/tasks/delete-all/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.count(), 0)
    
    
    # Test case for deleting a particular task from To Do
    def test_delete_task(self):
        task_id = str(self.task._id) 

        response = self.client.delete(f'/api/tasks/delete/{task_id}/')
        self.assertEqual(response.status_code, 204)


        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(_id=ObjectId(task_id))