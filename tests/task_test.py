import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task_1 = Task("Wash Dishes", 30)

    def test_task_objects_discription(self):
        self.assertEqual("Wash Dishes", self.task_1.description)

    def test_task_objects_duration(self):
        self.assertEqual(30, self.task_1.duration)
