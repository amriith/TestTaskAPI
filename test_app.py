import unittest
import json
from app import app

class TestTaskAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_task(self):
        """Test creating a new task 1 for Sit707"""
        response = self.app.post('/tasks',
                               data=json.dumps({
                                   'title': 'Test Task',
                                   'description': 'This is a test task'
                               }),
                               content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Test Task')
        self.assertEqual(data['description'], 'This is a test task')
        self.assertFalse(data['completed'])

    def test_get_task(self):
        """Test getting a specific task"""
        # First create a task
        self.app.post('/tasks',
                     data=json.dumps({
                         'title': 'Get Task Test',
                         'description': 'Testing get task'
                     }),
                     content_type='application/json')
        
        # Then get the task
        response = self.app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Get Task Test')

    def test_update_task(self):
        """Test updating a task"""
        # First create a task
        self.app.post('/tasks',
                     data=json.dumps({
                         'title': 'Update Task Test',
                         'description': 'Testing update task'
                     }),
                     content_type='application/json')
        
        # Then update the task
        response = self.app.put('/tasks/1',
                              data=json.dumps({
                                  'title': 'Updated Task',
                                  'completed': True
                              }),
                              content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Updated Task')
        self.assertTrue(data['completed'])

    def test_intentionally_failing_test(self):
        """This test is intentionally failing to demonstrate CI/CD failure"""
        # Create a task
        self.app.post('/tasks',
                     data=json.dumps({
                         'title': 'Failing Test Task',
                         'description': 'This task should fail'
                     }),
                     content_type='application/json')
        
        # This assertion will fail because we're expecting a different title
        response = self.app.get('/tasks/1')
        data = json.loads(response.data)
        self.assertEqual(data['title'], 'Wrong Title')  # This will fail

if __name__ == '__main__':
    unittest.main() 