
value1 = float(input("Type any value: "))
value2 = float(input("Type any value: "))
value3 = ""

if value1 > value2:
    value3 = f"Value {value1} greater than value {value2}"
elif value1 < value2:
    value3 = f"Value {value1} less than value {value2}"
else: 
    value3 = f"Value {value1} equals value {value2}"

print(value3)