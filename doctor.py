class Doctor:
    def __init__(self, **kwargs):
        if kwargs is None:
            print("Error: missing arguments.")
            return

        if 'doctor_id' in kwargs: self.id = kwargs['doctor_id']
        else: raise ValueError('Doctor ID cannot be empty') 

        if 'name' in kwargs: self.name = kwargs['name']
        else: raise ValueError('Name cannot be empty')

        if 'speciality' in kwargs: self.speciality = kwargs['speciality']
        else: raise ValueError('Speciality cannot be empty')

        if 'timing' in kwargs: self.timing = kwargs['timing']
        else: raise ValueError('Timing cannot be empty')

        if 'qualification' in kwargs: self.qualification = kwargs['qualification']
        else: raise ValueError('Qualification cannot be empty')

        if 'room_number' in kwargs: self.room_number = kwargs['room_number']
        else: raise ValueError('Room number cannot be empty')


    def get_doc_id(self):
        return self.id


    def set_doc_id(self, new_id):
        self.id = new_id


    def get_doc_name(self):
        return self.name


    def set_doc_name(self, new_name):
        self.name = new_name


    def get_doc_speciality(self):
        return self.speciality


    def set_doc_speciality(self, new_speciality):
        self.speciality = new_speciality


    def get_doc_timing(self):
        return self.timing


    def set_doc_timing(self, new_timing):
        self.timing = new_timing


    def get_doc_qualification(self):
        return self.qualification


    def set_doc_qualification(self, new_qualification):
        self.qualification = new_qualification


    def get_doc_room_num(self):
        return self.room_number


    def set_doc_room_num(self, new_room):
        self.room_number = new_room


    def __str__(self):
        return f"{self.get_doc_id()}_{self.get_doc_name()}_{self.get_doc_speciality()}_{self.get_doc_timing()}_{self.get_doc_qualification()}_{self.get_doc_room_num()}"
