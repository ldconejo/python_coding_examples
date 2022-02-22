'''
Different examples of warning-triggering PEP8 issues
'''
# pydlint: disable=R0903
class PylintDemo():
    '''
    Demo of too-few-public-methods warning
    '''
    def __init__(self, name, last_name, age):
        '''
        Init method
        '''
        try:
            self.name = name
            self.last_name = last_name
            self.age = age
        except:
            print("There was an error during init")

    def introduce_person(self):
        '''
        Introduces person
        '''
        return f"This is the instance for {self.name} {self.last_name} who's {self.age} years old"

    # pylint: disable=W0702
    def __can_person_drive(self):
        '''
        Determines if the person is old enough to drive
        '''
        try:
            if self.age >= 16:
                return f"{self.name} {self.last_name} can drive in the US"
            return f"{self.name} {self.name} cannot drive in the US"
        except:
            return "There was an error while testing the age of the driver"
