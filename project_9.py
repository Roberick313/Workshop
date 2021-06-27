###### Salary of a employee

def salary_of_employee():
    Salary = [700000,2000000,1400000,1100000,1500000,450000,870000,700000,2000000,1400000,1100000,1500000]
    a = 0

    f = open('SalaryOfEmployee.txt','w')
    f.write('')
    f.write('the list of salaryis: '+str(Salary)+'\n'+'\n')
    f.close()
    
    for a_for in Salary:
        a += a_for

    b = a/12
    
    f = open('SalaryOfEmployee.txt','a')
    f.write("Salary is: {}".format(a) + '\n')
    f.write("Average salary is: %7.4f" %b + '\n')
    f.close()
    
    return open('SalaryOfEmployee.txt').read()

print(salary_of_employee())