class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def read_patients_file(self):
        with open('./patients.txt') as f:
            for line in f:
                if line.startswith("id"):
                    continue

                raw_patient_data = line.split('_')
                patient_data = {
                    "id":raw_patient_data[0],
                    "Name":raw_patient_data[1],
                    "Disease":raw_patient_data[2],
                    "Gender":raw_patient_data[3],
                    "Age":raw_patient_data[4],
                }

                self.patients.append(patient_data)

    def enter_patient_info(self):
        patient_id = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")

        patient_info = {
            "id":patient_id,
            "Name":name,
            "Disease":disease,
            "Gender":gender,
            "Age":age,
        }

        return patient_info
    
    def format_patient_info_for_file(self, patient):
       return f'{patient["id"]}_{patient["Name"]}_{patient["Disease"]}_{patient["Gender"]}_{patient["Age"]}'
       
    def search_patient_by_id(self):
        patient_id = input("Enter the Patient Id: ")
        
        for patient in self.patients:
            if patient["id"] == patient_id:
                print(self.format_patient_info_for_file(patient))
                return
        
        print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient):
        print(f'{patient["id"]:<5}{patient["Name"]:<16}{patient["Disease"]:<15}{patient["Gender"]:<14}{patient["Age"]}')

    def display_patients_list(self):
        print(f'{"ID":<5}{"Name":<16}{"Disease":<15}{"Gender":<14}Age')
        
        for patient in self.patients:
            self.display_patient_info(patient)

    def edit_patient_info_by_id(self):
        patient_id = input("Enter the Patient Id: ")
        
        for index in range(len(self.patients)):
            patient = self.patients[index]
            if patient["id"] == patient_id:
                new_name = input("Enter new Name: ")
                new_disease = input("Enter new Disease: ")
                new_gender = input("Enter new Gender: ")
                new_age = input("Enter new Age: ")

                self.patients[index] = {
                    "id": patient["id"],
                    "Name": new_name,
                    "Disease": new_disease,
                    "Gender": new_gender,
                    "Age": new_age
                }
                self.write_list_of_patients_to_file()
                return
                    
        print("Can't find the Patient with the same id on the system")
    
    def write_list_of_patients_to_file(self):
        with open('./patients.txt', 'w') as f:
            f.write("id_Name_Disease_Gender_Age"+"\n")
            for patient in self.patients:
                f.write(self.format_patient_info_for_file(patient))

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)

        with open('./patients.txt', 'a') as f:
            f.write("\n"+self.format_patient_info_for_file(new_patient))

        print(f'Patient whose ID is {new_patient["id"]} has been added.')
