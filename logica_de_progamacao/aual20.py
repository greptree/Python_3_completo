
def get_number(msg):
    while True:
        try:
            return float(input(msg))

        except ValueError:
            print("`Number invalid!!")

value1 = get_number("Type a number: ")
value2 = get_number("Type another number: ")

if value1 > value2:
    print(f"Value {value1} greater than value {value2}")
elif value1 < value2:
    print(f"Value {value1} less than value{value2}")
else: 
    print(f"Value {value1} equals value  {value2}")
919 Full Notes919 Full Notes