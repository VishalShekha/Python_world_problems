'''
Scenario:
Imagine you are managing a team in a company, and you want to implement a performance-based salary adjustment system. The salary of each employee will be adjusted based on the completion status and submission date of their tasks. This system aims to motivate employees to complete their tasks on time and ensure high performance.

Objective:
You want to develop a program that will calculate and adjust the total salary of each employee based on their task performance. The program should output the adjusted salary for each employee, considering the completion status and submission date of tasks.
'''

employees = [
    ["XXX", 5000, [["Task 1", "complete", "2023-08-15"], ("Task 2", "incomplete", "2023-08-12")]],
    ["YYY", 6000, [("Task 1", "complete", "2023-08-10"), ("Task 2", "complete", "2023-08-14")]],
    ["ZZZ", 4500, [("Task 1", "incomplete", "2023-08-12"), ("Task 2", "incomplete", "2023-08-14")]],
]

for employee in employees:
    name, base_salary, tasks = employee
    total_salary = base_salary
    
    tasks_complete = True
    task_incomplete = False
    deadline = "2023-08-14"
    
    for task, status, submit_date in tasks:
        if status == "incomplete":
            tasks_complete = False
            task_incomplete = True
        if status == "complete" and submit_date > deadline:
            total_salary *= 0.5
    
    if tasks_complete:
        print("{}'s total salary: {}".format(name, total_salary))
    elif task_incomplete:
        total_salary *= 0.5
        print(name,"\b's total salary:",total_salary)
    else:
        print(f"{name}'s total salary: {total_salary * 0.1}")