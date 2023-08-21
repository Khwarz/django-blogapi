from django.contrib.auth import get_user_model, models
from django.test import TestCase

from .models import Post


# Create your tests here.
class BlogTests(TestCase):
    user: type[models.AbstractUser]
    post: Post

    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(  # type: ignore
            username="testuser",
            email="testuser@email.com",
            password="secretpassword",
        )
        cls.post = Post.objects.create(
            title="test title",
            body="test content",
            author=cls.user,
        )

    def test_post_model(self) -> None:
        self.assertEqual(self.post.title, "test title")
        self.assertEqual(self.post.body, "test content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "test title")
