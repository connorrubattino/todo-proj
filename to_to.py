


class Task:
    id_counter = 1

    def __init__(self, description, status):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.status = status

    def __str__(self):
        return f'Task {self.id}: {self.status} - {self.description}'
    

class ToDo:

    def __init__(self):
        self.tasks = []

    def add(self):
        description = input('Enter description of the task to be done: ')
        status = input('Is this task complete? Enter "y" or "n": ').lower()
        while status not in {'y', 'n'}:
            status = input('Invalid entry - Please enter "y" or "n": ').lower()
        if status == 'n':
            status = '[ ]'
        if status == 'y':
            status = '[x]'
        new_task = Task(description, status)
        self.tasks.append(new_task)
        print(f'Your new task:\n\t{new_task}\nhas been created')


    def view(self):
        if self.tasks:
            for task in self.tasks:
                print(task)
        else:
            print('This To-Do list is empty')

    def __get_task_from_id(self):
        task_id = input('What is the ID of the task you are looking for? ')
        while not task_id.isdigit():
            task_id = input('Invalid ID. Must be an integer. Please enter ID again: ')
        for task in self.tasks:
            if task.id == int(task_id):
                return task
        print(f"Task with an ID of {task_id} does not exist")



    def edit(self):
        task = self.__get_task_from_id()
        if task:
            print(task)
            # new_description = input('Enter a new description for your task! or type "skip" to keep it')
            # if new_description != 'skip':
            #     task.description = new_description
            
            new_status = input('Is this task now complete? Enter "y" or "n": ').lower()
            if new_status not in {'y', 'n'}:
                new_status = input('Invalid entry - Please enter "y" or "n": ').lower()
            elif new_status == 'y':
                task.status = '[x]'
            elif new_status == 'n':
                task.status = '[ ]'
            print(f'Your task:\n\t{task.status}\nhas been updated')
        else:
            print('No task found with that ID')


    def delete(self):
        task = self.__get_task_from_id()
        if task:
            print(task)
            you_sure = input('Are you sure you would like to delete this task? Enter "yes" or "y" to delete or anything else to keep: ').lower()
            if you_sure == 'yes' or you_sure == 'y':
                self.tasks.remove(task)
            else:
                print("Don't sweat it.. We didn't delete your task")
        else:
            print('No task found with that ID')


    def retrieve(self):
        task = self.__get_task_from_id()
        if task:
            print(task)


def todo_list():
    print('Welcome to your To-Do list - let\'s have a day!')
    todo_list = ToDo()
    while True:
        print('1. View Tasks\n2. Add Task\n3. Retrieve Single Task\n4. Edit Task\n5. Delete Task\n6. Quit')
        choice = input('Which option would you like to do? ')
        while choice not in {'1', '2', '3', '4', '5', '6'}:
            choice = input('Invalid option. Please enter 1, 2, 3, 4, 5, or 6: ')
        if choice == '1':
            todo_list.view()
        if choice == '2':
            todo_list.add()
        if choice == '3':
            todo_list.retrieve()
        if choice == '4':
            todo_list.edit()
        if choice == '5':
            todo_list.delete()
        if choice == '6':
            break
    print("Thank you for using the To-Do list - have a wonderful day!")

    

todo_list()
