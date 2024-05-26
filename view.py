"""
    Author: José De La Cruz
    Created: 2024-05-26
"""

class TaskView:
	"""Class that works as the application view"""

	def display_view(self):
		line = '=' * 29
		title = ' Gestor de Tareas Pendientes '
		print(line)
		print('{:^27}'.format(title))
		print(line)
		print('1. Agregar Tarea')
		print('2. Completar Tarea')
		print('3. Mostrar Tarea')
		print('4. Eliminar Tarea')
		print('5. Salir')