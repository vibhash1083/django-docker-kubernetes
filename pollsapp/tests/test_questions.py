from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, APIClient

class QuestionTest(TestCase):

    def setup(self):
        self.email = 'testuser@example.com'
        self.username = 'testuser'
        self.password = 'asdf1234'

        # Create User
        if len(User.objects.all())==0:
            self.user = User.objects.create_user(self.username, 
                self.email, self.password)
        # Check User
        self.assertEqual(len(User.objects.all()), 1)

        # Login User
        # user_login = self.client.login(username=self.username, 
        #     password=self.password)
        # # Check if user logged in
        # self.assertTrue(user_login)
        # response = self.client.get("/")
        # self.assertEqual(response.status_code, 200)


    def test_question(self):

        self.setup()
        question_url = "/auth/login/"
        cl = APIClient()
        response = cl.post(
            question_url,
            data={
                "username": 'testuser',
                "password": 'password123'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 1)
