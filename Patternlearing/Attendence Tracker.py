attendance = list(map(int, input("Enter attendance (1/0) separated by space: ").split()))

# Attendance percentage
percentage = (sum(attendance) / len(attendance)) * 100
print("Attendance Percentage:", round(percentage, 2), "%")

# Below 75%
if percentage < 75:
    print("Student below 75% attendance")

# Replace consecutive absences with warning
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"
        attendance[i+1] = "Warning"

print("Updated Attendance:", attendance)

#output:
# Enter attendance (1/0) separated by space: 1 0 1 0 0 1
# Attendance Percentage: 50.0 %