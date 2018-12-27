from peewee import *
from collections import OrderedDict
import datetime, sys


db = SqliteDatabase("project.db")

class Employee(Model):
    name = CharField(max_length=30, unique=True)
    task = TextField()
    time = TextField()
    notes = TextField()
    date = DateTimeField()

    class Meta:
        database = db

def instantiate():
    db.connect()
    db.create_tables([Employee], safe = True)


def add_employees():
    """Add some data"""
    print("add what you want")
    name = input("name: ")
    task = input("task: ")
    time = input("time taken: ")
    notes = input("notes: ")

    a = OrderedDict([
        ('name', name),
        ('task', task),
        ('time', time),
        ('notes', notes),
        ('date', datetime.datetime.today().strftime("%d-%m-%Y"))
    ])

    save_data = input("Would you like to save this data? y/n").lower()
    if save_data == 'y':
        try:
            Employee.create(name = a['name'], task = a['task'], time = a['time'], notes = a['notes'], date = a['date'])
        except IntegrityError:
            duplicate = Employee.get(name = a['name'])
            duplicate.task = a['task']
            duplicate.time = a['time']
            duplicate.notes = a['notes']
            duplicate.date = a['date']
            duplicate.save()
        else:
            print("Data saved!")
    else:
        print("data was not saved")


def view_employees():
    """View some data"""


    print("Please tell us which path you would like to take")
    print("A) Name\n"
          "B) Task\n"
          "C) Time\n"
          "D) Notes\n"
          "E) Date\n"
          "F) Date Range"
          )

    path_choice = input("Action: ").lower().strip()

    if path_choice == "a":
        path = search_employee_name(input("input name: "))
    elif path_choice == "b":
        path = search_employee_task(input("input task: "))
    elif path_choice == "c":
        path = search_employee_time(input("input time: "))
    elif path_choice == "d":
        path = search_employee_notes(input("input notes: "))
    elif path_choice == "e":
        path = search_employee_date(input("Input data: "))
    elif path_choice == "f":
        path = search_employee_date_range()



    for thing in path:
        print(" Employee name: ",thing.name,"\n",
              "Task: ",thing.task,"\n",
              "Time: ", thing.time,"\n",
              "Notes: ", thing.notes,"\n",
              "Date Recorded: ", thing.date
              )

        print("")
        print('N) for next entry')
        print('d) to delete entry')
        print('q) return to the main menu')
        print("")

        next_action = input("Action: [Ndq] ").lower().strip()

        if next_action == "q":
            break
        elif next_action == "d":
            delete_employees(thing)


def delete_employees(thing_to_delete):
    thing_to_delete.delete_instance()


def main_menu():
    while True:
        choice = None

        if choice != 'q':
            print("Please pick a path")
            for key, value in menu.items():
                print("{}) {}".format(key,value.__doc__))
            choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()


def search_employee_name(search_query):
    """Search for some data"""
    search = Employee.select().where(Employee.name.contains(search_query))

    return search


def search_employee_task(search_query):
    search = Employee.select().where(Employee.task.contains(search_query))

    return search


def search_employee_time(search_query):
    search = Employee.select().where(Employee.time.contains(search_query))

    return search


def search_employee_notes(search_query):
    search = Employee.select().where(Employee.notes.contains(search_query))

    return search


def search_employee_date(search_query):
    search = Employee.select().where(Employee.date.contains(search_query))

    return search

def search_employee_date_range():
    date_entry = input('Enter a date (i.e. 2017,7,1)')
    day, month, year = map(int, date_entry.split(','))
    date1 = datetime.date(year, month, day)

    date_entry = input('Enter a date (i.e. 2017,7,1)')
    day, month, year = map(int, date_entry.split(','))
    date2 = datetime.date(year, month, day)

    search = Employee.select().where(Employee.date.between(date1,date2))
    return search



menu= OrderedDict([
    ('a', add_employees),
    ("b", view_employees),
])



if __name__ == '__main__':
    instantiate()
    main_menu()