"""
    Author: José De La Cruz
    Created: 2024-05-26
"""

class TaskModel:
	"""Class that works as the application model"""

	def __init__(self):
		self.pending = []
		self.completed = []
	
	def add_task(self, task):
		self.pending.append(task)
	
	def get_tasks(self):
		return self.pending

	def show_tasks(self):
		self.get_tasks()

	def complete_task(self):
		pass

	def delete_task(self):
		pass
