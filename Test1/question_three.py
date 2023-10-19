#3. 

student_marks = [78, 83, 90, 88, 75]

# (i) Calculate and print the sum of all items in the list

def calculate_sum(student_marks):
    total = sum(student_marks)
    return total
student_marks = [78, 83, 90, 88, 75]
sum_of_marks = calculate_sum(student_marks)
print(f"The sum of the items in the student marks list is {sum_of_marks}")


# (ii) Display the first and last marks

first_student_mark = student_marks[0] 
last_student_mark = student_marks[-1]
print(f"First mark: {first_student_mark}, Last mark: {last_student_mark}")

# (iii) Adding 96 to the list

student_marks.append(96)
print("Adding 96 to the student marks list:", student_marks)

# (iv) Update the student mark of 78 to 87

index_to_update = student_marks.index(78)  # indexing 78
student_marks[index_to_update] = 87
print("The updated students' marks list is", student_marks)
