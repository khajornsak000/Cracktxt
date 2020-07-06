import random
atm_pass = "123"
result = ""
while result != atm_pass:
    result = ""
    for i in range(len(atm_pass)):
        list_number = random.choice("0123456789")
        result = "".join(list_number) + str(result)
        print("Search = ", result)
print("Crack Password is", result)