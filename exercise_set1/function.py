def bmi_calculator(weight, height):
    bmi = weight / (height*height)
    return bmi




name = input("What is your name?")
weight = input("What is your weitght?")
height = input("what is your height?")

weight_int = int(weight)
height_float = float(height)

bmi = bmi_calculator(weight_int, height_float)
print("your bmi is: "+ str(bmi))
print("{}, your bmi is: {}".format(name, bmi))