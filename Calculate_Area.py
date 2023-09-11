def calculate_area(length,width):
    if length == width:
        return "This is a square!"
    else:
        return length * width
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

area = calculate_area(length,width)
print("Area of rectangle is :", area)
