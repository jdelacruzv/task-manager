class TaskView:
	"""Class that works as the application view"""

	def show_view(self):
		line = '=' * 29
		title = ' Gestor de Tareas Pendientes '
		print(line)
		print('{:^27}'.format(title))
		print(line)
		print('1. Agregar Tarea')
		print('2. Completar Tarea')
		print('3. Mostrar Tarea')
		print('4. Eliminar Tarea')
		print('5. Salir\n')

	def show_task_list(self, tasks):
		for indice, task in enumerate(tasks):
			print(f'{indice + 1} {task[0].capitalize()} --> {task[1]}')
		print()