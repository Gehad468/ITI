pi = 3.14

def shape(name, val, width=1):
    f = open("shape.txt", "w")
    if name == "square":
       f.write("Area of square {} , length = {}\n".format(val * val, val))
    elif name == "rectangle":
        f.write("Area of rectangle = {} , height = {}, width = {}\n".format(val * width, height, width))
    elif name == "circle":
        f.write("Area of circle is {} radius = \n".format(pi * val * val,radius))
    elif name == "triangle":
        f.write("Area of triangle = {} ,height = {} ,width = {} \n".format(val * width * 0.5,height,width))
    else:
        print("not valid shape.")
    f.close()


name = input("Please enter name of shape: ")
if name == "square":
    val = int(input("enter value of square: "))
    shape(name, val)

elif name == "rectangle":
    height = int(input("enter height "))
    width = int(input("enter width "))
    shape(name, height, width)

elif name == "circle":
    radius = int(input("enter radius "))
    shape(name, radius)

elif name == "triangle":
    height = int(input("Please enter height of triangle: "))
    width = int(input("Please enter width of triangle: "))
    shape(name, height, width)
else:
    print("not valid shape.")



