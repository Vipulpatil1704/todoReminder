from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from bson import ObjectId
class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create some sample tasks
        self.task = Task.objects.create(
            _id=ObjectId(),
            title="Test Task",
            description="Test description",
            completed=False
        )
        
    # Test case to get all tasks from To Do
    
    def test_get_all_tasks(self):
        # Send GET request to fetch all tasks
        response = self.client.get('/api/tasks/')
        tasks = response.json()  # Convert response to JSON

        # Check if the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the number of tasks returned matches the number of tasks created
        self.assertEqual(len(tasks), 1)
        
        # Check if the tasks returned match the tasks created
        
        task_titles = [task['title'] for task in tasks]
        self.assertIn('Test Task', task_titles)
    
    # Test case to create a new task
    
    def test_create_task(self):
        # Data for the new task
        task_data = {
            "_id": str(ObjectId()), 
            "title": "New Task",
            "description": "Description for the new task"
        }
    
        # Send POST request to create a new task
        response = self.client.post('/api/tasks/', task_data, format='json')
        # print(response.json())
        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the task was created in the database
        task = Task.objects.get(title='New Task')
        self.assertEqual(task.title, 'New Task')
        self.assertEqual(task.description, 'Description for the new task')

        # Check if the response data matches the data sent in the request
        self.assertEqual(response.json()['title'], task_data['title'])
        self.assertEqual(response.json()['description'], task_data['description'])
    
    # Test case for updating a particular task from To Do
    
    def test_update_task(self):
        new_title = "Updated Task Title"
        new_description = "Updated Task Description"
        task_id = str(self.task._id)  # Get the ID of the task to update

        updated_data = {
            "title": new_title,
            "description": new_description
        }

        response = self.client.put(f'/api/tasks/{task_id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], new_title)
        self.assertEqual(response.json()['description'], new_description)
        self.assertTrue(ObjectId.is_valid(response.json().get('_id')))  # Ensure _id is still a valid ObjectId
    
    
    # Test case for deleting all the tasks from To Do
    def test_delete_all_tasks(self):
        response = self.client.delete('/api/tasks/delete-all/')
        self.assertEqual(response.status_code, 204)
        # Ensure all tasks have been deleted
        self.assertEqual(Task.objects.count(), 0)
    
    
    # Test case for deleting a particular task from To Do
    def test_delete_task(self):
        task_id = str(self.task._id)  # Get the ID of the task to delete

        response = self.client.delete(f'/api/tasks/delete/{task_id}/')
        self.assertEqual(response.status_code, 204)

        # Ensure task is deleted from the database
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(_id=ObjectId(task_id))