"""
    Author: José De La Cruz
    Created: 2024-05-26
"""
from view import TaskView

class TaskController:
	"""Class that works as the application controller"""

	def __init__(self, view):
		self.gui = view