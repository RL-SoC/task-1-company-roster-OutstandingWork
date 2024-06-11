"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""
from people import * # import everything!

if __name__ == "__main__":  # Equivalent to int main() {} in C++.
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number:"))

        if last_input == 1:
            name = input("Name:")
            age=int(input("Age:"))
            position=input("Position:")
            ID = int(input("ID:"))
            city = input("City:")
            branchcodes = input("Branch(es):")
            # How will you convert this to a list, given that
            # the user will always enter a comma separated list of branch codes?
            # eg>   2,5
            branchcodes=[int(x) for x in branchcodes.split(',')]

            salary = int(input("Salary: "))
            # Create a new Engineer with given details.
            engineer = Engineer(name,age,ID, city, branchcodes,position, salary) # Change this

            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson
            # Then add them to the roster
            name = input("Name:")
            age=int(input("Age:"))
            position=input("Position:")
            ID = int(input("ID:"))  # Convert ID to int
            city = input("City:")
            branchcodes = input("Branch(es):")
            # Convert the comma-separated string of branch codes to a list
            branchcodes = [int(code) for code in branchcodes.split(',')]
            salary = int(input("Salary: "))  # Convert salary to int
            # Create a new Salesperson with given details.
            salesperson = Salesman(name,age, ID, city, branchcodes,position=position, salary=salary)
            sales_roster.append(salesperson)  # Add him to the list!

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print Employee details for the given Employee ID that is given. 
            
            found_Employee = None
            for roster in [engineer_roster, sales_roster]:
                for Employee in roster:
                    if Employee.ID == ID:
                        found_Employee = Employee
                        break
                if found_Employee: break
            
            
            if not found_Employee:
                print("No such Employee")
            else:
                print(f"Name: {found_Employee.name} and Age: {found_Employee.age}")
                print(f"City of Work: {found_Employee.city}")

        ## Write code here to list the branch names to
        ## which the Employee reports as a comma separated list
        ## eg> Branches: Goregaon,Fort
                branch_names = ','.join(map(str, found_Employee.branches))
                print(f"Branches: {branch_names}")
                print(f"Salary: {found_Employee.salary}")

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change city to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("Enter Employee ID to change branch: "))
            new_city = int(input("Enter new branch code: "))
            # Find the Employee with the given ID
            Employee = next((e for e in engineer_roster + sales_roster if e.ID == ID), None) # If else only used to check if employee ID matches the input
            
            if Employee is not None:
                Employee.change_city(new_city)  

        #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:

             # promote Employee to next position
            ID = int(input("Enter Employee ID to promote: "))
            Employee = next((e for e in engineer_roster + sales_roster if e.ID == ID), None)
            post=input("Enter new position")
            if Employee is not None:
                check=Employee.promote(post)
                if check:
                    print(f"Employee {ID} has been promoted to {post}.")
                else:
                    print(f"Failed to promote Employee {ID}.")
                    


           

        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            salary = int(input("Enter salary of Employee: "))
            # Increment salary of Employee.
            Employee=next((e for e in engineer_roster + sales_roster if e.ID == ID), None)
            if Employee is not None:
                Employee.increment(salary)
                print(f"Salary of Employee {ID} has been incremented by {salary}.")
            else:
                print(f"Failed to increment salary of Employee {ID}.")        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            Employee = next((e for e in sales_roster if e.ID == ID), None)
            if Employee is not None:
                superior_id, superior_name = Employee.find_superior()
                if superior_id is not None:
                    print(f"The superior of Employee {ID} is {superior_name} with ID {superior_id}.")
                else:
                    print(f"Employee {ID} does not have a superior.")
            else:
                print("Employee not found.")

            # Print superior of the sales Employee.
        
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            # Add superior of a sales Employee
            ID_E.add_superior(ID_S)


        else:
            raise ValueError("No such query number defined")

            
            

            


            


        






