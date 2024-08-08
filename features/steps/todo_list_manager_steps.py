from behave import given, when, then
from todo_list_manager import ToDoListManager

@given('the to-do list is empty')
def step_impl(context):
    context.manager = ToDoListManager()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    context.manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = context.manager.list_tasks()
    assert task in tasks

@when('the user lists all tasks')
def step_impl(context):
    context.output = context.manager.list_tasks()

@then('the output should contain:')
def step_impl(context):
    expected_output = {}
    for row in context.table:
        expected_output[row['Task']] = 'Pending'
    assert context.output == expected_output

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    context.manager.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    tasks = context.manager.list_tasks()
    assert tasks[task] == 'Completed'

@when('the user clears the to-do list')
def step_impl(context):
    context.manager.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert not context.manager.list_tasks()

@when('the user adds a task "{task}" with priority "{priority}"')
def step_impl(context, task, priority):
    # Assuming ToDoListManager has been updated to handle priorities
    context.manager.add_task_with_priority(task, priority)

@then('the to-do list should contain "{task}" with priority "{priority}"')
def step_impl(context, task, priority):
    tasks = context.manager.list_tasks()
    assert tasks[task] == priority

@when('the user lists completed tasks')
def step_impl(context):
    context.output = context.manager.list_completed_tasks()

@then('the output should contain:')
def step_impl(context):
    expected_tasks = [row['Task'] for row in context.table]
    actual_tasks = list(context.output.keys())
    assert set(expected_tasks) == set(actual_tasks)