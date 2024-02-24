from django.urls import path
from . import views

# Define the namespace for the tasks app
app_name = "tasks"

# Define the URL patterns for the tasks app
urlpatterns = [
    # URL pattern for the index page
    path("", views.index, name="index"),
    # URL pattern for adding a new task
    path("add/", views.add, name="add"),
    # URL pattern for the weekend tasks page
    path("weekendTasks/", views.weekendTasks, name="weekendTasks"),
    # URL pattern for the special tasks page
    path("special/", views.specialTasks, name="special")
]