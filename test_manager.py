import unittest
from manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task(1, "Fix auth bug", "high")
        self.assertEqual(task.title, "Fix auth bug")
        self.assertFalse(task.completed)

    def test_duplicate_task_raises_error(self):
        self.manager.add_task(1, "First task")
        with self.assertRaises(ValueError):
            self.manager.add_task(1, "Duplicate task")

if __name__ == '__main__':
    unittest.main()
