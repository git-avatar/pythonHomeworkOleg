import json
file_path = "data.json"

# Load existing data
with open(file_path, "r") as f:
    existing_data = json.load(f)

# Create a list to hold new student data
new_student = {"name": None, "age": None}

# Prompt for adding a student
question = str(input("Do you want to add a student(yes/no)? ")).lower()

while question == "yes":
    # Validate input
    if question != "yes" and question != "no":
        print("You can only answer this question with yes or no")
        question = str(input("Do you want to add a student(yes/no)? ")).lower()

    elif question == "yes":
        name = str(input("Enter the name of the student: "))
        new_student["name"] = name
        age = int(input("Enter the age of the student: "))
        new_student["age"] = age

        # Check if student is already registered
        if new_student not in existing_data["students"]:
            existing_data["students"].append(new_student)
            print("Student added successfully!")
        else:
            print("This student is already registered")

    # Prompt for adding another student
    question2 = str(input("Would you like to add another student(yes/no)? ")).lower()
    if question2 != "yes" and question2 != "no":
        print("You can only answer this question with yes or no")
        question2 = str(input("Would you like to add another student(yes/no)? ")).lower()

    elif question2 == "yes":
        continue

    else:
        break
all_students = []

with open(file_path, "w") as f:
    # Dump the merged data to the file
    json.dump(existing_data, f, indent = 4)

total_names = len(existing_data["students"])

combined_age = 0
for student in existing_data["students"]:
    combined_age += student["age"]

average_age = combined_age/total_names

def all_students():
    return [student["name"] for student in existing_data["students"]]


all_students = all_students()

output_string = f"The average age from the students: {', '.join(all_students)}, is: {average_age}"

print(output_string)