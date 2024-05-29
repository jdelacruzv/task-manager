class TaskModel:
	"""Class that works as the application model"""

	def __init__(self):
		self.tasks = []
	
	def add_task(self, task, status):
		self.tasks.append([task, status])
	
	def get_tasks(self):
		return self.tasks

	def show_tasks(self):
		self.get_tasks()

	def complete_task(self, pos_task):
		for indice, _ in enumerate(self.tasks):
			if indice == pos_task - 1:
				self.tasks[indice][1] = 'Completada'
				
	def delete_task(self, pos_task):
		for indice, _ in enumerate(self.tasks):
			if indice == pos_task - 1:
				self.tasks.pop(indice)
