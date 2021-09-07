from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

# Create your tests here.

class PostTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='admin',password='pass')
        test_user.save()

        test_post = Post.objects.create(
            author = test_user,
            title = 'Title',
            body = 'sentence'
        )
        test_post.save()

    def test_Blog(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post.author), 'admin')
        self.assertEqual(post.title, 'Title')
        self.assertEqual(post.body, 'sentence')  