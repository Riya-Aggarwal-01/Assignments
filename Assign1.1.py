
student_name=input("Enter your name")
student_class=input("Enter your class")
print("To find total marks and percentage you have to enter your marks in different subjects out of 100")
dccn=float(input("DCCN : "))
oops=float(input("Oops : "))
dsa=float(input("DSA : "))
mpi=float(input("MPI : "))
java=float(input("Java : "))

total_marks=dccn+oops+dsa+mpi+java
percentage=(total_marks/500)*100

print("\n--- Student Result ---")

print(f"Student Name : {student_name}")
print(f"Student Class : {student_class}")
print(f"Total Marks : {total_marks}/500")
print(f"Percentage : {percentage:.2f}%")
if (percentage>70) and (percentage<=100):
    print("Grade : A")
elif (percentage>40) and (percentage<=70):
    print("Grade : B")
elif (percentage>30) and (percentage<=40):
    print("Grade : C")
else:
    print("Grade : Fail")