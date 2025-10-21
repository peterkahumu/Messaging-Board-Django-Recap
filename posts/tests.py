from django.test import TestCase
from django.urls import reverse
from .models import Post
import uuid


# Create your tests here.
class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is the first test")
        cls.post1 = Post.objects.create(text="This is the other test case.")

    def setUp(self):
        self.response = self.client.get("/")
        self.response_name = self.client.get(reverse("home"))

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is the first test")
        self.assertEqual(self.post1.text, "This is the other test case.")

    def test_post_id(self):
        self.assertIsNotNone(self.post.id)
        self.assertIsNotNone(self.post1.id)
        self.assertIsInstance(self.post.id, uuid.UUID)

    def test_homepage(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response_name.status_code, 200)
        self.assertTemplateUsed(self.response, "posts/post_list.html")
        self.assertContains(self.response_name, "This is the first test")
