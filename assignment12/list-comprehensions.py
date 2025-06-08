#Task 3: List Comprehensions Practice
import pandas as pd

#Reads the contents of ../csv/employees.csv into a DataFrame
df = pd.read_csv("../csv/employees.csv")

#Using a list comprehension, create a list of the employee names, first_name + space + last_name.
full_names = [row["first_name"] + " " + row["last_name"] for _, row in df.iterrows()]
print("Employee Full Names:")
print(full_names)

#Create a list from the previous list of names. This list should include only those names that contain the letter "e".
names_e = [name for name in full_names if "e" in name.lower()]
print("\nNames with 'e':")
print(names_e)