#GPA Calc
C1 = float(input("Course 1 hours: "))
G1 = float(input("Grade for course 1: "))
TQ1 = C1 * G1
C2 = float(input("Course 2 hours: "))
G2 = float(input("Grade for course 2: "))
TQ2 = C2 * G2
C3 = float(input("Course 3 hours: "))
G3 = float(input("Grade for course 3: "))
TQ3 = C3 * G3
C4 = float(input("Course 4 hours: "))
G4 = float(input("Grade for course 4: "))
TQ4 = C4 * G4
TH = C1 + C2 + C3 + C4
print(f"Total hours: {int(TH)}")
Points = int(TQ1 + TQ2 + TQ3 + TQ4)
print(f"Total quality points: {Points}")
GPA = Points / TH
GPA = round(GPA,2)
print(f"Your GPA for this semester is {GPA}")


