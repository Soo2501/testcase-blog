from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post

class BlogTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username = "test",
            password = "testpassword"
        )

        self.model = Post.objects.create(
            title = "test",
            content = "test content",
            author = self.user,
        )

    def test_model(self):
        self.assertEqual(self.model.title, "test")
        self.assertEqual(self.model.content, "test content")
        self.assertEqual(self.model.author, self.user)