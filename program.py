n = []

while True:
    k = input("Input a numerical value or simply hit Enter to exit: ")
    if k == "":
        break
    n.append(int(k))

n.sort(reverse=True)

print("five greatest numbers in descending order are:")
for number in n [:5]:
 print(number)