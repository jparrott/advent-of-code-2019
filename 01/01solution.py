# M O D U L E S
import math # math.floor to round down

# F I L E
with open('01input.txt') as file:
    content = file.read().splitlines()

# P A R T  1
content = list(map(int, content)) # map the list of strings to integers
fuel = list(map(lambda x: math.floor(x/3)-2, content)) # calc the fuel
total = sum(fuel)

# S O L U T I O N
print(f"TOTAL FUEL NEEDED = {total}")
#3318804 is wrong (forgot to minus 2)
#3318604 is right

# P A R T  2

extra_fuel = []
# list of total extra fuel for each module
# (not including original calc from fuel list)

for module in fuel:
    doublef = [] # mini list for summing
    while True:
        module = math.floor(module/3)-2
        if module < 0 and len(doublef) > 0:
            extra_fuel.append(sum(doublef)) # <-- see, summing
            break
        elif module < 0 and len(doublef) < 0:
            # this means our math immediately produced a number <= 0
            # and we need to move on
            break
        else:
            doublef.append(module)

# S O L U T I O N
print(f"WITH EXTRA FUEL INCLUDED = {sum(extra_fuel)+total}")
#4975039 is right

# N O T E S

# for each module in the fuel list
# - start with an empty list to hold each module's extra fuel numbers (doublef)
# - while True loop (use BREAK to exit)
# -- do the math
# -- if the new number is less than zero AND doublef has at least 1 item
# --- append the sum of the doublef items to the main extra_fuel list
# --- break the while loop and go to the next module (for loop)
# -- else if the new number is less than zero but doublef has no items
# --- break the while loop and go to the next module (for loop)
# -- else append the new number to doublef
# -- while loop continues
