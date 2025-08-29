try:
    horas = int(input("Enter the hour: "))

    if horas <= 11:
        print("Good Morning!")
    elif( horas <= 17):
        print("Good Afternoon!")
    elif horas <= 23:
        print("Good Evening")
except ValueError:
    print("Type a hour!")
    

