from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Post

class ViewTest(TestCase):
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
        url = reverse('post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail(self):
        response  = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)
        self.assertContains(response, self.post.author.username)

    def test_post_create_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('post_create'), {'title': 'New Post', 'content':'New Content'})
        self.assertEqual(response.status_code, 302)
        new_post = Post.objects.get(title="New Post")
        self.assertEqual(new_post.author, self.user)

    def test_post_update_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('post_update', args ={self.post.id}), {'title': 'update post'})
        self.assertEqual(response.status_code, 200)
        updated_post = Post.objects.get(pk=self.post.id)
        self.assertEqual(updated_post.author, self.user)

    def test_post_delete_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("post_delete", args={self.post.id}))
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(pk=self.post.id)
