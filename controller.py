class TaskController:
	"""Class that works as the application controller"""

	def __init__(self, model, view):
		self.model = model
		self.view = view
	
	def add_task(self, task, status):
		self.model.add_task(task, status)

	def complete_task(self, pos_task):
		self.model.complete_task(pos_task)

	def show_tasks(self):
		tasks = self.model.get_tasks()
		self.view.show_task_list(tasks)

	def delete_task(self, pos_task):
		self.model.delete_task(pos_task)

	def show_view(self):
		self.view.show_view()
	
	def validate_indice_task(self, pos_task):
		tasks = self.model.get_tasks()
		tasks_final = []
		for indice, _ in enumerate(tasks):
			tasks_final.append(indice + 1)
		if pos_task in tasks_final:
			return True