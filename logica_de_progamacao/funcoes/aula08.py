name = "kathau"
last_name = "kathin"
age = 17
height = 1.65

def check_idade(age):

    if(age >= 18):
        return "Adult"
    else:
        return "Adolescent"

print(f"Name: {name}")
print(f"Last name: {last_name}")
print(f"Age: {age} {check_idade(age)}")
print(f"Height; {height}")
