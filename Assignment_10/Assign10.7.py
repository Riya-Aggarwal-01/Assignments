import matplotlib.pyplot as plt

subjects = ['Maths', 'Physics', 'Chemistry', 'CS', 'English']
sem1_marks = [85, 78, 92, 88, 76]
sem2_marks = [80, 82, 89, 91, 74]

# Plotting with different line styles
plt.plot(subjects, sem1_marks, label='Semester 1', linestyle='--', marker='o', color='blue')
plt.plot(subjects, sem2_marks, label='Semester 2', linestyle='-.', marker='s', color='green')

# # Add labels and title
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Semester Marks Comparison Using Line Styles")
plt.grid(True)
plt.legend()
plt.show()
