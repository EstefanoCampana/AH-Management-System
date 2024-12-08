class Patient:
    def __init__(self, **kwargs):
        if kwargs is None:
            print("Error: missing arguments.")
            return

        # Make sure that pid, name, disease, gender and age parameters are given
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
        '''Returns patient\'s Id'''
        return self.pid
    
    def get_name(self):
        '''Returns patient\'s name'''
        return self.name

    def get_disease(self):
        '''Returns patient\'s disease'''
        return self.disease

    def get_gender(self):
        '''Returns patient\'s gender'''
        return self.gender

    def get_age(self):
        '''Returns patient\'s age'''
        return self.age

    def set_pid(self, new_pid):
        '''
        Sets patient\'s Id

        new_pid - Patient's new id
        '''
        self.pid = new_pid
    
    def set_name(self, new_name):
        '''
        Sets patient\'s name

        new_name - Patient's new name
        '''
        self.name = new_name

    def set_disease(self, new_disease):
        '''
        Sets patient\'s disease

        new_disease - Patient's new disease
        '''
        self.disease = new_disease

    def set_gender(self, new_gender):
        '''
        Sets patient\'s gender

        new_gender - Patient's new gender
        '''
        self.gender = new_gender

    def set_age(self, new_age):
        '''
        Sets patient\'s age

        new_age - Patient's new age
        '''
        self.age = new_age

    def __str__(self):
        '''Provides a string representation of the Patient instance'''
        return f'{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}'
