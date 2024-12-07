from Patient import Patient

class PatientManager:
    '''
    PatientManager is responsible for reading from- and writing to a data file
    as well as managing a list of Patients at runtime.
    '''
    def __init__(self):
        '''
        Constructor initializes an empty list and fills it
        by reading the data file, parsing lines and appending
        each created Patient instance to the list.
        '''
        self.patients = []
        self.read_patients_file()

    def read_patients_file(self):
        '''
        Opens patients data file in read-mode,
        parses each line and creates a new Patient
        Instance which is appended to the patients list.
        '''
        with open('./Project Data/patients.txt') as f:
            for line in f:
                if line.startswith("id"):
                    continue

                raw_patient_data = line.split('_')
                patient = Patient (
                    pid = raw_patient_data[0],
                    name = raw_patient_data[1],
                    disease = raw_patient_data[2],
                    gender = raw_patient_data[3],
                    age = raw_patient_data[4],
                )

                self.patients.append(patient)

    def enter_patient_info(self):
        '''
        Asks the user for new patient's information,
        creates a new Patient instance with the given information
        and returns the created instance.
        '''
        patient_id = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")

        patient = Patient(
            pid = patient_id,
            name = name,
            disease = disease,
            gender = gender,
            age = age,
        )

        return patient
    
    def format_patient_info_for_file(self, patient):
       '''
        Formats and returns the patient information to be stored in data file.
       '''
       return f'{patient.get_pid()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}'
       
    def search_patient_by_id(self):
        '''
        Asks the user for the ID of a patient to search.
        When a user is found with the given ID, then their
        information is displayed in a table format.

        In case no such user exists, then an error message
        is shown
        '''
        patient_id = input("Enter the Patient Id: ")
        
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                print(f'{"ID":<5}{"Name":<16}{"Disease":<15}{"Gender":<14}Age')
                self.display_patient_info(patient)
                return
        
        print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient):
        '''
        Prints patient's information in a table-like format
        '''
        print(f'{patient.get_pid():<5}{patient.get_name():<16}{patient.get_disease():<15}{patient.get_gender():<14}{patient.get_age()}')

    def display_patients_list(self):
        '''
        Prints all patients' information in a table.
        '''
        print(f'{"ID":<5}{"Name":<16}{"Disease":<15}{"Gender":<14}Age')
        
        for patient in self.patients:
            self.display_patient_info(patient)

    def edit_patient_info_by_id(self):
        '''
        Asks the user for the ID of a patient whose data is
        to be modified.

        When the patient is found, new information is requested
        from the user such as name, disease, gender, age. The new
        information is then used in order to update the existing
        patient's information.

        If there is no patient with the given ID, then
        and error is printed.
        '''
        patient_id = input("Enter the Patient Id: ")
        
        for index in range(len(self.patients)):
            patient = self.patients[index]
            if patient.get_pid() == patient_id:
                new_name = input("Enter new Name: ")
                new_disease = input("Enter new Disease: ")
                new_gender = input("Enter new Gender: ")
                new_age = input("Enter new Age: ")

                self.patients[index].set_name(new_name)
                self.patients[index].set_disease(new_disease)
                self.patients[index].set_gender(new_gender)
                self.patients[index].set_age(new_age)

                self.write_list_of_patients_to_file()
                return
                    
        print("Can't find the Patient with the same id on the system")
    
    def write_list_of_patients_to_file(self):
        with open('./Project Data/patients.txt', 'w') as f:
            f.write("id_Name_Disease_Gender_Age"+"\n")
            for patient in self.patients:
                f.write(patient.__str__())

    def add_patient_to_file(self):
        '''
        Requests new patient's information by calling
        'enter_patient_info', which returns a new Patient
        instance.

        The new instance is then added to the patients list.

        And finally the data file for patients is opened in
        append-mode in order to write new lines at the end of the file
        without overriding existing data in the file.
        '''
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        with open('./Project Data/patients.txt', 'a') as f:    
            f.write("\n" + new_patient.__str__())

        print(f'Patient whose ID is {new_patient.get_pid()} has been added.')
