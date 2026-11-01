A = float(input("Enter angle value(A): "))
B = float(input("Enter angle value(B): "))
C = float(input("Enter angle value(C): "))

sum_of_angles = A + B + C

if A > 0 and B > 0 and C > 0 and sum_of_angles == 180:
    print("Yes, it forms a Triangle")
else:
    print("No, it does not form a Triangle")
