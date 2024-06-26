import os
from model import TaskModel
from view import TaskView
from controller import TaskController

# Create instances of Model, View, and Controller
model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

# Show view using the Controller
controller.show_view()

# Show exit message when the task is finished
def print_message(message):
	print(f'<<< Tarea {message} >>>\n')

while True:
	try:
		option = int(input('Digite opción del menú: '))
		if option == 5:
			print('<<< Saliendo del programa >>>\n')
			os._exit(0)
		if option == 1:
			print('=== Agregar tarea ===')
			opt_add = input('Ingrese la tarea: ')
			controller.add_task(opt_add, status='Pendiente')
			print_message('agregada')
			controller.show_view()	
		if option == 2:
			print('=== Completar tarea ===')
			pos_task = int(input('Ingrese la posición: '))
			validate_indice = controller.validate_indice_task(pos_task)
			if validate_indice:
				controller.complete_task(pos_task)
				print_message('completada')
				controller.show_view()
			else:
				print('<<< Índice ingresado no existe >>>\n')			
		if option == 3:
			print('=== Mostrar tareas ===')
			controller.show_tasks()
			controller.show_view()	
		if option == 4:
			print('=== Eliminar tarea ===')
			pos_task = int(input('Ingrese la posición: '))
			validate_indice = controller.validate_indice_task(pos_task)
			if validate_indice:
				controller.delete_task(pos_task)
				print_message('eliminada')
				controller.show_view()
			else:
				print('<<< El índice ingresado no existe >>>\n')
	except:
		print('<<< Entrada no válida >>>\n')