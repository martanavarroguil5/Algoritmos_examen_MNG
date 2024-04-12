from empType import EmpType

class Employee():
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.__salary = salary # El salrio es privado

    # Getters y Setters

    def get_employee_id(self):
        if isinstance(self.employee_id, int):
            return self.employee_id
        else:
            raise TypeError("El identificador del empeado debe estar asignado mediante un numero entero.")
        
    def get_name(self):
        if isinstance(self.name, str):
            return self.employee_id
        else:
            raise TypeError("El debe escribir el nombre del empeado.")
        
    def get_position(self):
        if isinstance(self.position, EmpType):
            return self.position
        else:
            raise TypeError("La posicion debe pertenecer al enumerado empType")
        
    def get_salary(self):
        if isinstance(self.__salary, float):
            return self.__salary
        else:
            raise TypeError("Salario debe ser un número con decimales.") 
        
    
    # La posicion puede camiar al ir ascendiendo.
    def set_position(self, position):
        self.position = position

    #El salario puede cambiar al recivir un aumento.
    def set_salary(self, salary):
        self.__salary = salary
    

        

    """Python class to implement a basic version of a hotel employee.

    This Python class implements the basic functionalities of a hotel employee in a 
    simple hotel management system.

    Syntax
    ------
    obj = Employee(emp_id, name, position, salary)

    Parameters
    ----------
    [in] emp_id : int
        Unique identifier for the employee.
    [in] name : str
        Name of the employee.
    [in] position : str
        The job position of the employee (e.g., 'Receptionist', 'Housekeeper', 'Manager').
    [in] salary : float
        The salary of the employee.

    Returns
    -------
    obj : Employee
        Python object output parameter that represents an instance of the class Employee.

    Attributes
    ----------
    """
    #Here you start your code.





def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_employee_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

if __name__ == "__main__":
    main()
