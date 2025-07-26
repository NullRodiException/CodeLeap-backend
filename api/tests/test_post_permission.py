from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Post

class PostPermissionsTestCase(APITestCase):
    def setUp(self):
        self.user_author = User.objects.create_user(username='author')
        self.user_other = User.objects.create_user(username='other')

        self.post = Post.objects.create(
            title="Post do Autor",
            content="Conteúdo",
            author=self.user_author
        )

        self.client = APIClient()

    def test_author_can_update_post(self):
        self.client.force_authenticate(user=self.user_author)

        url = f'/careers/{self.post.id}/'
        response = self.client.patch(url, {'title': 'Novo Título'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Novo Título')

    def test_other_user_cannot_update_post(self):
        self.client.force_authenticate(user=self.user_other)

        url = f'/careers/{self.post.id}/'
        response = self.client.patch(url, {'title': 'Título Inválido'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_can_delete_post(self):
        self.client.force_authenticate(user=self.user_author)

        url = f'/careers/{self.post.id}/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_other_user_cannot_delete_post(self):
        self.client.force_authenticate(user=self.user_other)

        url = f'/careers/{self.post.id}/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Post.objects.filter(id=self.post.id).exists())