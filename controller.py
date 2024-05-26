"""
    Author: José De La Cruz
    Created: 2024-05-26
"""
from model import TaskModel
from view import TaskView

class TaskController:
	"""Class that works as the application controller"""

	def __init__(self, model, view):
		self.model = model
		self.view = view
	
	def add_task(self, task):
		self.model.add_task(task)

	def show_tasks(self):
		tasks = self.model.get_tasks()
		self.view.show_tasks(tasks)

	def update_view(self):
		self.view.show_view()