while True:

    age = int(input("Type your age: "))
    name = input("What's your name? ")

    validate_age = age > 0
    validate_name = name != ""
    if validate_age and validate_name:
            
        print(f"your name is: {name}")
        print(f"your name reversed: {name[::-1]}")

        if "" in name:
            print("your name contains spaces")
        else:
            print("your name has no space")
        
        print(f"You name have {len(name)} letter")
        print(f"first letter of your name: {name[0]}")
        print(f"last letter of your name: {name[-1]}")
        
        break
    else:
        print("nao digitou algum campo")
        continue

