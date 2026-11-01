n = int(input("Enter number of rows: "))
symbol = input("Enter a symbol (* or 0): ")

for i in range(n, 0, -1):
    for j in range(i):
        print(symbol, end=" ")
    print()
