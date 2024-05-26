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

# Add tasks using the Controller
controller.update_view()

# Defines the output of the program
# def leave_sys():
# 	while True:
# 		leave = input('¿Desea continuar? (S / N): ').lower()
# 		if leave == 's':
# 			controller.update_view()
# 		elif leave == 'n':
# 			print('Saliendo del programa...')
# 			os._exit(0)
# 		else:
# 			print('Entrada no válida')


while True:
	try:
		option = int(input('Digite número según la opción: '))
		if option == 5:
			print('Saliendo del programa...')
			os._exit(0)
		elif option == 1:
			print('Agregar tarea: ')
		elif option == 2:
			print('Completar tarea')
		elif option == 3:
			print('Mostrar tareas')
		elif option == 4:
			print('Eliminar tarea')
	except:
		print('Entrada no válida...')
