class BusinessCard:
    def __init__(self, first_name, last_name, company, job, email, phone_number):
        self.first_name     = first_name
        self.last_name      = last_name
        self.company        = company
        self.job            = job
        self.email          = email
        self.phone_number   = phone_number

        self.length_name   = 0
        
    @property
    def length_name(self):
        return self._length_name

    @length_name.setter
    def length_name(self, value):
        self._length_name = len(self.first_name) + len(self.last_name) + 1

    #----------------------------------------------------------------
    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def contact(self):
        print("Kontaktuję się z...", self.first_name, self.last_name, self.email)

