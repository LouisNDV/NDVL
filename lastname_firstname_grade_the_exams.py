# Open and read a file
classname = input("Enter a class to grade: ")
filename = classname + '.txt'

# Give an error if the input name has some problems
try:
    opened_file = open(filename, "r")
except FileNotFoundError:
    print('Invalid filename, please input again')
except:
    print("There's something wrong")
else:
    print("File opened successfully\n")

# Give an error if the data is invalid
line_no = 0
opened_file.seek(0)
error_line = 0
print("*** ANALYZING ***")
for line in opened_file:
    line_no += 1
    line = line.strip()
    student_info = line.split(",")
    number_of_element = len(student_info)
    if number_of_element != 26:
        error_line += 1
        print("Invalid line of data: does not contain exactly 26 values")
        print(line)
    elif student_info[0][0] != 'N' or len(student_info[0][1:]) != 8 or not (student_info[0][1:]).isdigit():
        error_line += 1
        print("Invalid line of data: N# is invalid")
        print(line)
if error_line == 0:
    print("No errors found!")
valid_line = line_no - error_line

print("*** REPORT ***")
print(f"Total valid lines of data: {valid_line}")
print(f"Total invalid lines of data: {error_line}")

answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key_list = answer_key.split(",")
opened_file.seek(0)
mark_table = []
high_score_student_count = 0
mark_table_student_name = []

# Mark scores for each student
for line in opened_file:
    line = line.strip()
    student_info = line.split(",")
    student_mark = 0
    if len(student_info) != 26 or student_info[0][0] != 'N' or len(student_info[0][1:]) != 8 or not (
            student_info[0][1:]).isdigit():
        continue
    else:
        mark_table_student_name.append(student_info[0])

    for i in range(1, len(student_info)):
        if student_info[i] == answer_key_list[i - 1]:
            student_mark += 4
        elif student_info[i] == "":
            None
        else:
            student_mark -= 1
    mark_table.append(student_mark)
    if student_mark > 80:
        high_score_student_count += 1

# Print results
print("Total student of high scores:", high_score_student_count)
print("Highest score:", max(mark_table))
print("Lowest score:", min(mark_table))
print("Mean (average) score:", sum(mark_table) / len(mark_table))
print("Range of scores:", max(mark_table) - min(mark_table))
middle_point = len(mark_table) // 2
sorted_mark_table = sorted(mark_table)
res = (sorted_mark_table[middle_point] + sorted_mark_table[~middle_point]) / 2
print("Median score:", res)

# Write file
with open(classname + "_grades.txt", "w") as MarkFile:
    for i in range(valid_line):
        write_content = mark_table_student_name[i] + "," + str(mark_table[i])+"\n"
        MarkFile.write(str(write_content))
