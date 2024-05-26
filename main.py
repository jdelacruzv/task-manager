"""
    Author: José De La Cruz
    Created: 2024-05-26
"""
from model import TaskModel
from view import TaskView
from controller import TaskController

# Create instances of Model, View, and Controller
model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

# Add tasks using the Controller
controller.update_view()


