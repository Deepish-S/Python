print("Select from"
      "\n(1 or A).add "
      "\n(2 or S).Sub"
      "\n(3 or M).Multiply"
      "\n(4 or D).Division")

user_inpt = input("Enter Your Selection : ")

if user_inpt == "1" or user_inpt == "A" or user_inpt == "a":
    fst_numb = int(input("Enter your 1st number : "))
    sec_numb = int(input("Enter your 2nd number : "))
    print(f"The sum of {fst_numb} and {sec_numb} is : ", fst_numb+sec_numb)

elif user_inpt == "2" or user_inpt == "S" or user_inpt == "s":
    fst_numb = int(input("Enter your 1st number : "))
    sec_numb = int(input("Enter your 2nd number : "))
    print(f"The Sub of {fst_numb} and {sec_numb} is : ", fst_numb-sec_numb)

elif user_inpt == "3" or user_inpt == "M" or user_inpt == "m":
    fst_numb = int(input("Enter your 1st number : "))
    sec_numb = int(input("Enter your 2nd number : "))
    print(f"The Multipliction of {fst_numb} and {sec_numb} is : ", fst_numb*sec_numb)

elif user_inpt == "4" or user_inpt == "D" or user_inpt == "d":
    fst_numb = int(input("Enter your 1st number : "))
    sec_numb = int(input("Enter your 2nd number : "))
    print(f"The Division of {fst_numb} and {sec_numb} is : ", fst_numb//sec_numb)
else:
    print('\033[1m'+"Enter The Correct Selection")