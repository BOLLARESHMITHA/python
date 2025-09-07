# Function to calculate average marks of students
def calculate_averages(students):
    averages = {}
    for name, marks in students.items():
        avg = sum(marks) / len(marks)
        averages[name] = round(avg, 2)
    return averages
# Function to find top performer
def find_topper(students):
    averages = calculate_averages(students)
    topper = max(averages, key=averages.get)  # student with highest avg
    return topper

students = {"John": [85, 78, 92],"Alice": [88, 79, 95],"Bob": [70, 75, 80]}
averages = calculate_averages(students)
print("Average Marks:", averages)
top_student= find_topper(students)
print("Top Performer:", top_student)
