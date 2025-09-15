# add some numbers. what could possibly go wrong?
total = 0
for i in range(5):
    while True:
        try:
            temp = int(input("Enter an integer: "))
            break
        except ValueError:
            print("Invalid value. Please try again.")
            continue
        total += temp

print("Total: ", total)
