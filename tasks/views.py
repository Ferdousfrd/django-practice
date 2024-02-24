from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Define a form for adding new tasks
class NewTaskForm(forms.Form):
    # Create a form field for entering a new task
    task = forms.CharField(label="New Task")

# Display the list of tasks on the index page
def index(request):
    # Check if tasks are stored in the session, if not, initialize an empty list
    if "tasks" not in request.session:
        request.session["tasks"] = []

    # Render the index page with the list of tasks
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]  # Pass the list of tasks to the template
    })

# Add a new task
def add(request):
    # If the form is submitted via POST method
    if request.method == "POST":
        # Create a form instance and populate it with data from the request
        form = NewTaskForm(request.POST)
        # If the form data is valid
        if form.is_valid():
            # Extract the cleaned data from the form
            task = form.cleaned_data["task"]
            # Add the new task to the session's task list
            request.session["tasks"] += [task]
            # Redirect to the index page
            return HttpResponseRedirect(reverse("tasks:index"))
        # If the form data is invalid
        else:
            # Render the add page again with the form and validation errors
            return render(request, "tasks/add.html", {
                "form": form  # Pass the form with validation errors to the template
            })

    # If the form is not submitted or there are GET requests
    return render(request, "tasks/add.html", {
        'form': NewTaskForm()  # Render the add page with an empty form
    })

# Display tasks for the weekend
def weekendTasks(request):
    return render(request, "tasks/weekendTasks.html")  # Render the weekend tasks page

# Display special tasks
def specialTasks(request):
    return render(request, "tasks/special.html")  # Render the special tasks page