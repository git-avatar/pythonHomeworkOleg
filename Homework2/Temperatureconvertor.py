Cur_unit_of_temp = str(input("Enter your current unit of temperature(C/F)"))

num = int(input("Enter the temperature in numbers"))
if Cur_unit_of_temp == "C" or "c":
    F = num*(9/5)+32
    print("F =", F, "Fahrenheit")

elif Cur_unit_of_temp == "F" or "f":
    C =(num-32)*5/9
    print("C =", C, "Celsius")