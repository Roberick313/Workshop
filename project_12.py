#### compute the perimeter and the area of shapes


while True:                                                     #unlimited loop for input
    shape_input = str(input("enter your shape name: "))
    shape = shape_input.lower()
    
                                                                #checking the right input
    if shape == 'circle':
        R = int(input("enter the radius of Circle: "))
            
        circle_perimeter = 3.14*R*2
        circle_area = 3.14*R*R
        print("the perimeter of the circle is: {}{}the area of the circle is: {}".format(circle_perimeter,'\n',circle_area))
        #break
    elif shape == 'square':
        E = int(input("enter a edge of Square: "))
            
        square_perimeter = E*4
        square_area = E**2
        print("the perimeter of the Square is: {}{}the area of the Square is: {}".format(square_perimeter,'\n',square_area))
        #break
    elif shape == 'rectangle':
        L = int(input("enter the length of Rectangle: "))
        W = int(input("enter the width of Rectangle: "))
            
        Rectangle_perimeter = (L+W)*2
        Rectangle_area = L*W
        print("the perimeter of the Rectangle is: {}{}the area of the Rectangle is: {}".format(Rectangle_perimeter,'\n',Rectangle_area))
        #break   in case that u want to break the loop if the first shape name was correct :)
    else:
        print("Your entered name is wrong!")
     
