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

	def update_view(self):
		self.view.show_view()