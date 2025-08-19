while True:
    value1 = input("type the number: ")
    value2 = input("type another number: ")
    operator = input("chose the operator -+/*: ")

    number_valit = None
    operator_check = '+-/*'
    try:
        value1_float = float(value1)
        value2_float = float(value2)
        number_valit = True
    except:
        number_valit = None

    if number_valit is None:
        print("one number is invalid!")
        continue

    if operator not in operator_check:
        print("operator is invalid")
        continue

    if len(operator) > 1:
        print("one operator")
        continue

        ###
    if operator == "+":
        print(f"{value1_float + value2_float}")
    if operator == "-":
        print(f"{value1_float - value2_float}")
    if operator == "/":
        print(f"{value1_float / value2_float}")
    if operator == "*":
        print(f"{value1_float * value2_float}")
    ###
    saida = input("you want exit ? [y]es or [n]o: ").lower().startswith("y")

    if saida is True:
        break
