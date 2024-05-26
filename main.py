"""
    Author: José De La Cruz
    Created: 2024-05-26
"""
import os
from model import TaskModel
from view import TaskView
from controller import TaskController

# Create instances of Model, View, and Controller
model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

# Show view using the Controller
controller.update_view()

while True:
	try:
		option = int(input('Digite número según la opción: '))
		if option == 5:
			print('Saliendo del programa...')
			os._exit(0)
		if option == 1:
			print('--- Agregar tarea ---')
			opt_add = input('Ingrese la tarea: ')
			controller.add_task(opt_add)
			print('...Tarea agregada...')
			controller.update_view()
		if option == 2:
			print('--- Completar tarea ---')
		if option == 3:
			print('--- Mostrar tareas ---')
			controller.show_tasks()
			controller.update_view()
		if option == 4:
			print('--- Eliminar tarea ---')
	except:
		print('Entrada no válida...')
