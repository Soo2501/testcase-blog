from django.test import TestCase
from blog.forms import PostForm

class PostFormTest(TestCase):
    def test_valid_form(self):
        data = {'title':'Test Title', 'content':'Test Content'}
        form = PostForm(data)
        self.assertTrue(form.is_valid())

    def test_post_form_missing_required_field(self):
        data = {'title': 'Test Title'}
        form = PostForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)

    def test_form_widgets(self):
        form = PostForm()
        self.assertEqual(form.fields['title'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['content'].widget.attrs['class'], 'form-control')
        self.assertEqual(form.fields['content'].widget.attrs['rows'], 5)

