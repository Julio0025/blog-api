from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from post.models import Post


class PostCrudTest(APITestCase):

    def setUp(self):
        self.user_tom = User.objects.create(username='Tom')
        self.user_ben = User.objects.create(username='Ben')
        self.tom_post = Post.objects.create(user=self.user_tom, title='title', content='test content')

    def test_post_creation(self):
        """
        Ensure we can create a new account object.
        """

        data = {'title': 'title', 'content': 'content test'}
        response = self.client.post('/api/post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(self.user_tom)
        response = self.client.post('/api/post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        """
        allow only owner of the post to modify
        :return:
        """
        data = {'title': 'title', 'content': 'content test'}

        response = self.client.put('/api/post/{0}/'.format(self.tom_post.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(self.user_ben)
        response = self.client.put('/api/post/{0}/'.format(self.tom_post.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(self.user_tom)
        response = self.client.put('/api/post/{0}/'.format(self.tom_post.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_delete(self):
        """
        allow only owner of the post to delete
        :return:
        """
        response = self.client.delete('/api/post/{0}/'.format(self.tom_post.id), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(self.user_ben)
        response = self.client.delete('/api/post/{0}/'.format(self.tom_post.id), format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.force_login(self.user_tom)
        response = self.client.delete('/api/post/{0}/'.format(self.tom_post.id), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

