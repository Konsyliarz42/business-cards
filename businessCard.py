#================================================================
class BusinessCard:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name     = first_name
        self.last_name      = last_name
        self.phone_number   = phone_number
        
        self.label_length   = 0
        
    @property
    def label_length(self):
        return self._label_length

    @label_length.setter
    def label_length(self, value):
        self._label_length = len(self.first_name) + len(self.last_name) + 1

    #----------------------------------------------------------------
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def contact(self):
        print("Wybieram numer ", self.phone_number, "i dzwonię do", self.first_name, self.last_name)

#================================================================
class BaseContact(BusinessCard):
    def __init__(self, email, *args):
        super().__init__(*args)

        self.email  = email

    def __repr__(self):
        return f"{self.first_name} {self.last_name} as BaseContact"

    def contact(self):
        super().contact()

#================================================================
class BusinessContact(BusinessCard):
    def __init__(self, company, job, *args):
        super().__init__(*args)

        self.company    = company
        self.job        = job
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} as BusinessContact"

    def contact(self):
        super().contact()