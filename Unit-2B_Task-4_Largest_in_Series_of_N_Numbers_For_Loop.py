n = int(input("Enter how many numbers: "))

largest = int(input("Enter a number: "))

for i in range(1, n):
    num = int(input("Enter a number: "))

    if num > largest:
        largest = num

print(f"Largest number = {largest}")
