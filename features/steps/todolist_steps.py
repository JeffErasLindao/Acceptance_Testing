from behave import given, when, then
from todolist import ToDoListManager

# Create an instance of ToDoListManager for use in steps
manager = ToDoListManager()

@given('the to-do list is empty')
def step_impl(context):
    # Ensure the to-do list is empty
    manager.clear_tasks()

@given('the to-do list contains tasks')
def step_impl(context):
    # Clear the list and add tasks from the table
    manager.clear_tasks()
    for row in context.table.rows:
        task = row['Task']
        manager.add_task(task)

@given('the to-do list contains tasks with status')
def step_impl(context):
    # Clear the list and add tasks with status from the table
    manager.clear_tasks()
    for row in context.table.rows:
        task = row['Task']
        status = row['Status']
        manager.add_task(task)
        # Directly manipulate the internal structure
        for t in manager.tasks:
            if t['task'] == task:
                t['status'] = status

@when('the user adds a task "{task}"')
def step_impl(context, task):
    # Add a task to the list
    manager.add_task(task)

@when('the user lists all tasks')
def step_impl(context):
    # Store the output in context for verification
    context.output = "Tasks:\n" + "\n".join([f"- {t['task']}" for t in manager.list_tasks()])

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    # Mark the specified task as completed
    manager.mark_task_as_completed(task)

@when('the user clears the to-do list')
def step_impl(context):
    # Clear the to-do list
    manager.clear_tasks()

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    # Check if the task is in the list
    tasks = manager.list_tasks()
    assert any(t['task'] == task for t in tasks), f'Task "{task}" not found in the to-do list'

@then('the output should contain')
def step_impl(context):
    # Normalize the output and expected output
    expected_output = context.text.strip().replace('\r\n', '\n')
    actual_output = context.output.strip().replace('\r\n', '\n')
    
    # Normalize line endings and compare
    assert actual_output == expected_output, f'Expected "{expected_output}" but got "{actual_output}"'
    

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    # Check if the task's status is completed
    tasks = manager.list_tasks()
    for t in tasks:
        if t['task'] == task:
            assert t['status'] == 'Completed', f'Task "{task}" is not completed'
            return
    assert False, f'Task "{task}" not found in the to-do list'

@then('the to-do list should be empty')
def step_impl(context):
    # Verify that the to-do list is empty
    assert not manager.list_tasks(), 'The to-do list is not empty'
