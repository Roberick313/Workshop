def my_student()->str:
    '''This function will return the second top person between the number of student\n
    \rthat it took'''

    My_dict = {}
    Student_Number = None
    Input_value = None
    Input_Mark = None
    Input_Number_of_student = None
    The_first_one = 0
    The_second_one = 0

    while True:

        Input_value = int(input("Pls enter the number of student: "))

        if Input_value:
            break

        else:
            continue
    
    for _ in range(Input_value):

        Input_Number_of_student = int(input("Enter the student number: "))
        Input_Mark = int(input("Enter the mark of that student: "))
        My_dict[Input_Number_of_student] = Input_Mark

        if Input_Mark > The_first_one:

            if The_first_one > The_second_one:
                The_second_one = The_first_one
                for ky,vl in My_dict.items():
                    if vl == The_second_one:
                        Student_Number = ky
            
            The_first_one = Input_Mark
                  
    return f"""The second top person of the class is: Student number: {Student_Number} got {The_second_one}
    \rHere is the list of All the Students{My_dict}"""
