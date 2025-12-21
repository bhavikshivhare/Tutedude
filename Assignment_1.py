
from tabulate import tabulate as t

employee = {}

def add_employee():
    empid = input("Enter Employee ID: ")
    
    if empid in employee:
        print('Employees already exist')
        return

    name = input('Enter the employee name : ')
    age = input('Enter the age : ')
    department = input('Enter the department : ')
    salary = input('Enter salary : ')

    employee[empid] = {"NAME": name, "AGE": age, "DEPARTMENT": department,"SALARY": salary}
    print ('employee added successfully')
    

def view_all_employee():
    if not employee:
        print('No Employees Available')
        return

    table = []
    for empid,i in employee.items():
        table.append([
            empid,
            i['NAME'],
            i['AGE'],
            i['DEPARTMENT'],
            i['SALARY']])
    
    header =["Emp_ID","Name","Age","Department","Salary"]
    print(t(table,headers=header,tablefmt="grid"))
        

def search_employee():
    i = input("Enter Employee ID: ")    
    if i not in employee:
           print ("Employee Not Found")
    else:
        print(f'Employee id :{i}')
        print(f"Employee Name :{employee[i]['NAME']}")
        print(f"Employee AGE :{employee[i]['AGE']}")
        print(f"Employee DEPARTMENT :{employee[i]['DEPARTMENT']}")
        print(f"Employee SALARY :{employee[i]['SALARY']}")

def delete_employee():
    x = input('Enter employee ID to delete : ')
    if x not in employee:
        print ("Employee Not Found")
    else:
        del employee[x]
        print ("Employee deleted successfully!")


def main_menu():
    while True:
        print ('*****Employee Management System*****')
        print ('1.Add Employee')
        print ('2.View All Employee')
        print ('3.Search for Employee')
        print ('4.Delete the Employee')
        print ('5.Exit')

        select = input('choice from 1 to 5:')

    
        if select == '1':
            add_employee() 
        elif select == '2':
            view_all_employee()
        elif select == '3':
            search_employee()
        elif select == '4':
            delete_employee()
        elif select =='5':
            print ('Thank you!!!')
            break
        else:
            print('Invalid menu selected')
   
main_menu()

