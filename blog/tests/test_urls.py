from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User
from django.urls import reverse

class BlogUrlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = "test",
            password = "testpassword"
        )

        self.post = Post.objects.create(
            id = 1,
            title = "Test",
            content = "test content",
            author = self.user
        )
    def test_post_list(self):
        url = reverse("post_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        url = reverse("post_detail", args={self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_create(self):
        self.client.force_login(self.user)
        url = reverse('post_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_update(self):
        self.client.force_login(self.user)
        url = reverse("post_update", args={self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_delete(self):
        self.client.force_login(self.user)
        url = reverse("post_delete", args={self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)