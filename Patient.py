class Patient:
    def __init__(self, **kwargs):
        if kwargs is None:
            print("Error: missing arguments.")
            return

        if 'pid' in kwargs: self.pid = kwargs['pid']
        else: raise ValueError('Pid cannot be empty') 

        if 'name' in kwargs: self.name = kwargs['name']
        else: raise ValueError('Name cannot be empty')

        if 'disease' in kwargs: self.disease = kwargs['disease']
        else: raise ValueError('Disease cannot be empty')

        if 'gender' in kwargs: self.gender = kwargs['gender']
        else: raise ValueError('Gender cannot be empty')

        if 'age' in kwargs: self.age = kwargs['age']
        else: raise ValueError('Age cannot be empty')

    def get_pid(self):
        return self.pid
    
    def get_name(self):
        return self.name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age
    
    def set_pid(self, new_pid):
        self.pid = new_pid
    
    def set_name(self, new_name):
        self.name = new_name

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f'{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}'
    


    
