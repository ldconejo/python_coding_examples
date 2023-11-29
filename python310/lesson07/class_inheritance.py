class Person:

    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name
        self.ssn = None

    def configure_ssn(self, ssn):
        #if not self.ssn:
        if self.ssn is None:
            self.ssn = ssn
            return f"SSN for {self.name} {self.last_name} has been set"
        return f"ERROR: Cannot set a new SSN for {self.name} {self.last_name}"
    
    def introduce(self):
        return f"This person is {self.name} {self.last_name}"
    
    def __str__(self):
        return f"{self.name} {self.last_name}"

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name}"
    
class Employee(Person):

    def __init__(self, name, last_name, employee_id) -> None:
        super().__init__(name, last_name)
        self.employee_id = employee_id

    def introduce(self):
        original_string = super().introduce()
        return f"{self.name} {self.last_name} has employee number {self.employee_id}", original_string

if __name__ == "__main__":
    #new_person = Person("Paul", "Lockaby")
    #print(new_person.configure_ssn(1234))
    #print(new_person.configure_ssn(1235))
    #print(new_person.ssn)
    #print(new_person.introduce())
    #print(new_person)
    #new_string = f"This person is {new_person}"
    #print(new_string)
    new_employee = Employee("Luis", "Conejo", "1234")
    print(new_employee.introduce())
    new_employee.configure_ssn("9999")
    print(new_employee.ssn)