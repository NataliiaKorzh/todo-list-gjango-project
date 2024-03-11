from django.test import TestCase
from django.urls import reverse

from app.models import Tag, Task


TASK_LIST_URL = reverse("app:task-list")
TAG_LIST_URL = reverse("app:tag-list")


class ModelTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            content="test content",
            datetime="2024-03-11 09:00:00",
            deadline="2024-03-20 10:00:00",
            status=False,
        )

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Test Tag")

    def test_task_list(self):
        response = self.client.get(TASK_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/task_list.html")

    def test_tag_list(self):
        response = self.client.get(TAG_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/tag_list.html")
