'''
    TECHDEGREE PROJECT 4
    FOR THIS PROJECT I WORKED WITH SQLITE3 INSTEAD OF USING PEEWEE
    YOUSSEF JOHN MOUSTAHIB
'''


import sys, datetime, sqlite3


def lookup_menu():
    """
    THIS FUNCTION IS PROMPTED EARLY WHEN THE USER CHOOSES TO LOOKUP DATA
    IT PRESENTS THEM WITH 5 PATHS.

    TESTED IN TESTS_FOR_COVERAGE

    """

    lookup_choice = input("Please pick a letter to make a choice of how to look up a file\n"
                          "A) Find by Employee\n"
                          "B) Find by Date\n"
                          "C) Find by Time spent\n"
                          "D) Find by Search term\n"
                          "E) Exit to main menu\n"
                          "> "
                          ).lower()

    return lookup_choice

def lookup():
    """
    LOOKUP WILL USE THE PATH SELECTED IN LOOKUP_MENU,
    IF THE USER SELECTED 'A' FOR EXAMPLE, THE USER IS
    PROMPTED FOR ANOTHER INPUT, THAT INPUT IS USED AS AN
    ARGUMENT IN THE LOOKUP_BY_NAME FUNCTION.

    TESTED IN TESTS_FOR_COVERAGE

    """

    lookup_choice = lookup_menu()

    if lookup_choice == "a":
        entry_by_name = input("Enter a name: ")
        lookup_by_name(entry_by_name)

    elif lookup_choice == "b":
        entry_by_date = input("Enter a date (dd/mm/yyyy): ")
        lookup_by_date(entry_by_date)

    elif lookup_choice == "c":
        entry_by_time = input("Enter a time: ")
        lookup_by_time(entry_by_time)

    elif lookup_choice == "d":
        entry_by_search_term = input("Enter a Search Term: ")
        entry_by_search_term = "%" + entry_by_search_term + "%"
        print(entry_by_search_term)
        lookup_by_search_term(entry_by_search_term, entry_by_search_term)

    elif lookup_choice == "e":
        main()

    return lookup_choice


def make_edit_question():
    """
    ASKS FOR INPUT AND RETURNS IT

    TESTED IN TESTS_FOR_COVERAGE

    """

    make_edit = input("Would you like to edit anything? y/n ").lower()

    return make_edit


def make_edits(row_to_edit):
    """
    HERE WE PROMPT THE USER TO MAKE A CHANGE, IF THEY
    SAY YES, WE THEN ASK THEM WHAT PART OF THE DATA THEY
    WOULD LIKE TO CHANGE. THEN WE ASK THEM FOR THE CHANGE,
    AND CHANGE THE DATA IN THE SQL DATABASE

    """

    make_edit = make_edit_question()
    if make_edit == "y":
        which_id = input("Which ID would you like to edit? \n")

        which_coloumn = input("Which coloumn would you like to edit?\n"
                              "A) Employee name\n"
                              "B) Date\n"
                              "C) Time\n"
                              "D) Notes "
                              ).lower()

        if which_coloumn == "a":
            new_name = input("enter your new name: ")
            row_to_edit.execute("UPDATE table_for_work_log SET name = '{}' WHERE id = '{}'".format(new_name, which_id))
        elif which_coloumn == "b":
            new_date = input("enter a new date: ")
            row_to_edit.execute("UPDATE table_for_work_log SET date = '{}' WHERE id = '{}'".format(new_date, which_id))
        elif which_coloumn == "c":
            while True:
                try:
                    new_time = int(input("enter a new time: "))
                    row_to_edit.execute("UPDATE table_for_work_log SET time = '{}' WHERE id = '{}'".format(new_time, which_id))
                except ValueError:
                    print("Please only enter numbers.")
                    continue
                else:
                    new_time = new_time
                    break
        elif which_coloumn == "d":
            new_notes = input("enter new notes: ")
            row_to_edit.execute("UPDATE table_for_work_log SET notes = '{}' WHERE id = '{}'".format(new_notes, which_id))

def add_to_sql(values_into_coloumn):
    """
    THIS FUNCTION ADDS DATA TO SQL. IN THE ADD.EXECUTE LINE,
    IT HAS 6 ?'S, THE VALUES_INTO_COLOUMN ARGUMENT IS A LIST,
    IT ALSO HAS 6 THINGS INSIDE. THE VALUES ARE PLACED INTO,
    THE ?'S.

    """

    conn = sqlite3.connect("work_log.db")
    add = conn.cursor()
    add.execute("insert into table_for_work_log values (?,?,?,?,?,?)", values_into_coloumn)
    conn.commit()
    conn.close()


def shorten_code(list_of_results):
    """
    THIS IS JUST A BIT OF HOUSEKEEPING. IT TAKES A LIST OF
    WHAT THE USER SEARCHED, THEN ADDS THE ITEMS TO A LIST.
    THE LIST IS THEN ITERATED THROUGH TO SHOW THE USER EACH BIT OF DATA

    """

    end = []
    for thing in list_of_results:
        thing = list(thing)
        end.append(thing)

    for thing in end:
        print("ID: ", thing[0])
        print("Name: ", thing[1])
        print("Task: ", thing[2])
        print("Time: ", thing[3])
        print("Notes: ", thing[4])
        print("Date: ", thing[5])
        a = input("Press Enter to see next result. ")
        print("")


def ask_user_for_time():
    """
    USED IN INPUTS_FROM_USER FUNCTION.
    ASKS USER FOR THE TIME TAKEN.

    TESTED IN TESTS_FOR_COVERAGE

    """

    while True:
        try:
            time = int(input("Enter time taken(minutes): "))

        except ValueError:
            print("Please only enter numbers.")
            #continue
        else:
            time = time
            break
    return time

def ask_user_for_name_task_notes():
    """
    USED IN INPUTS_FROM_USER FUNCTION
    ASKS USER FOR 3 INPUTS

    TESTED IN TESTS_FOR_COVERAGE

    """

    name = input("Enter your name: ")
    task = input("Enter your task: ")
    notes = input("Enter your notes: ")

    return name, task, notes

def inputs_from_user():
    """
    COLLECTS ALL OF THE USER INPUTS FOR ADDING A NEW
    FILE INTO THE SQL DATABASE, PUTS IT INTO A LIST,
    THEN PASSES IT INTO THE ADD_TO_SQL FUNCTION

    """
    name, task, notes = ask_user_for_name_task_notes()

    date = datetime.datetime.today().strftime("%d-%m-%Y")
    time = ask_user_for_time()

    list_of_answers = [None, name, task, time, notes, date]

    add_to_sql(list_of_answers)

    return name, task, notes


def lookup_by_name(name_from_sql):
    """
    OPENS THE SQL FILES ASSOCIATED WITH THE ARGUMENT
    NAME_FROM_SQL, WHICH WAS PASSED IN BY THE USER IN
    THE LOOKUP FUNCTION. THEN INCORPORATES OTHER FUNCTIONS
    TO MAKE EDITS TO THE FILES, THEN FINALLY CLOSES THE CONNECTION.

    """

    conn = sqlite3.connect("work_log.db")
    pointer = conn.cursor()
    pointer.execute("select id, name, task, time, notes, date from table_for_work_log where name is '{}';".format(name_from_sql))
    results = pointer.fetchall()

    shorten_code(results)

    make_edits(pointer)

    conn.commit()
    conn.close()

def lookup_by_date(date_from_sql):

    """
    OPENS THE SQL FILES ASSOCIATED WITH THE ARGUMENT
    NAME_FROM_SQL, WHICH WAS PASSED IN BY THE USER IN
    THE LOOKUP FUNCTION. THEN INCORPORATES OTHER FUNCTIONS
    TO MAKE EDITS TO THE FILES, THEN FINALLY CLOSES THE CONNECTION.

    """

    conn = sqlite3.connect("work_log.db")
    pointer = conn.cursor()
    pointer.execute("select id, name, task, time, notes, date from table_for_work_log where date is '{}';".format(date_from_sql))
    results = pointer.fetchall()

    shorten_code(results)

    make_edits(pointer)

    conn.commit()
    conn.close()

def lookup_by_time(time_from_sql):

    """
    OPENS THE SQL FILES ASSOCIATED WITH THE ARGUMENT
    NAME_FROM_SQL, WHICH WAS PASSED IN BY THE USER IN
    THE LOOKUP FUNCTION. THEN INCORPORATES OTHER FUNCTIONS
    TO MAKE EDITS TO THE FILES, THEN FINALLY CLOSES THE CONNECTION.

    """

    conn = sqlite3.connect("work_log.db")
    pointer = conn.cursor()
    pointer.execute("select id, name, task, time, notes, date from table_for_work_log where time is '{}';".format(time_from_sql))
    results = pointer.fetchall()

    shorten_code(results)

    make_edits(pointer)

    conn.commit()
    conn.close()

def lookup_by_search_term(task_from_sql, notes_from_sql):

    """
    OPENS THE SQL FILES ASSOCIATED WITH THE ARGUMENT
    NAME_FROM_SQL, WHICH WAS PASSED IN BY THE USER IN
    THE LOOKUP FUNCTION. THEN INCORPORATES OTHER FUNCTIONS
    TO MAKE EDITS TO THE FILES, THEN FINALLY CLOSES THE CONNECTION.

    """

    conn = sqlite3.connect("work_log.db")
    pointer = conn.cursor()
    pointer.execute("select id, name, task, time, notes, date from table_for_work_log where task like '{}' or notes like '{}';".format(task_from_sql, notes_from_sql))
    results = pointer.fetchall()

    shorten_code(results)

    make_edits(pointer)

    conn.commit()
    conn.close()


def main_menu():
    """
    THIS IS THE MAIN MENU, IT ASKS WHAT
    PATH THE USER WANTS TO TAKE.

    TESTED IN TESTS_FOR_COVERAGE

    """

    begin = input("Hello and welcome to the company Database\n"
                  "Please Pick the following:\n"
                  "A) Add a new entry\n"
                  "B) Lookup an existing entry\n"
                  "C) Quit the program\n"
                  "> ").lower()

    return begin

def main():
    """
    THIS IS THE MAIN PART OF THE CODE, IT OPENS OR
    CREATES A FILE IN SQLITE3. IT THEN TAKES THE INPUT
    FROM THE MAIN_MENU FUNCTION, AND USES IT TO
    SELECT THE CORRECT FUNCTIONS.

    """
    global c
    conn = sqlite3.connect("work_log.db")
    c = conn.cursor()
    c.execute("create table if not exists table_for_work_log(id integer primary key autoincrement, name text, task text, time integer, notes text,date text);")
    conn.commit()
    conn.close()

    while True:
        begin = main_menu()
        if len(begin) != 1:
            print("Please enter 'A', 'B', or 'C'")


        if begin == "c":
            sys.exit("Goodbye")
        elif begin == "a":
            inputs_from_user()

        elif begin == "b":
            lookup()
        else:
            print("Sorry the value you entered is not recognised\n"
                  "Please try again")


if __name__ == '__main__':
    main()