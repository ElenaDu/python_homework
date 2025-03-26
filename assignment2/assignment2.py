#Task 2: Read a CSV File
import csv
import os

def read_employees():
    rows_list =[]
    dict_employees = {}

    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            dict_employees["fields"]= next(reader)
            for row in reader:
                rows_list.append(row)
            dict_employees["rows"] = rows_list
        return dict_employees      
        

    except Exception as e:
        print(f'An error occurred while processing the file: {e}')
        exit()

employees = read_employees()
print(employees)

#Task 3: Find the Column Index
def column_index(column_header):
    try:
        return employees["fields"].index(column_header)
    except ValueError:
        print (f"There is no '{column_header}' in header list.")
        return None
employee_id_column = column_index("employee_id")
print(employee_id_column)

#Task 4: Find the Employee First Name
def first_name(row_number):
    try:
        index_number = column_index("first_name")
        return employees['rows'][row_number][index_number]
    except IndexError:
        print(f"Row {row_number} is out of range.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}.")
        return None
      
print(first_name(1))

#Task 5: Find the Employee: a Function in a Function
def employee_find(employee_id):
    def employee_match(row):
       return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))

    return matches
    
print(employee_find(3))

#Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches
print(employee_find(1000))

#Task 7: Sort the Rows by last_name Using a Lambda
def sort_by_last_name():
    last_name_index = column_index("last_name")   
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

sort_by_last_name()
print(employees)


#Task 8: Create a dict for an Employee
def employee_dict(record):
    new_dict={}
    for i, field in enumerate(employees['fields']):
        if field != "employee_id":
            new_dict[field] = record[i]        
    return new_dict

print(employee_dict(employees["rows"][0]))

#Task 9: A dict of dicts, for All Employees
def all_employees_dict():
    dict_of_dicts = {}
    employee_id_index = employees["fields"].index("employee_id") 
    for row in employees['rows']:
        employee_id = row[employee_id_index]
        dict_of_dicts[employee_id] = employee_dict(row)    
    return dict_of_dicts

print(all_employees_dict())

#Task 10: Use the os Module
def get_this_value():
    return os.environ.get("THISVALUE")

print(get_this_value())

#Task 11: Creating Your Own Module
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("AD_")
print(custom_module.secret)

#Task 12: Read minutes1.csv and minutes2.csv
def read_minutes():
    def csv_to_dict(file_name):
        dict_minutes = {}
        list_minutes = []
        try: 
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                dict_minutes["fields"] = next(reader)
                for row in reader:
                    list_minutes.append(tuple(row))
                dict_minutes["rows"] = list_minutes        
            return dict_minutes
        except Exception as e:
            print(f"An error occurred while reading '{file_name}': {e}")
            return None
    
    v1 = csv_to_dict("../csv/minutes1.csv")
    v2 = csv_to_dict("../csv/minutes2.csv")
    if v1 is None or v2 is None:
        print("There was an issue reading one or both of the files.")
        exit()
    return v1, v2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13: Create minutes_set
def create_minutes_set():
    set_1 = set(minutes1["rows"])
    set_2 = set(minutes2["rows"])
    resulting_set = set_1.union(set_2)    
    return resulting_set

minutes_set = create_minutes_set()
print(minutes_set)

#Task 14: Convert to datetime
from datetime import datetime

def create_minutes_list():
    resulting_list = list(minutes_set)
    resulting_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), resulting_list))
    return resulting_list

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key = lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list

test_list = write_sorted_list()
print(test_list)