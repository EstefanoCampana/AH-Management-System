class Doctor:
    def __init__(self, id, name, speciality, timing, qualification, room_number):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number
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
    
class DoctorManager:
    def constructor():
        global list_doctors
        list_doctors = []
        DoctorManager.read_doc_file()

#read file
    def read_doc_file():
        global list_id
        global list_name
        global dic_doctors
        global objects_doc
        list_id = []
        list_name = []
        dic_doctors = {}
        objects_doc = []
        with open("doctors.txt" ,"r") as d: #missing folder path
            for line in d:
                d2 = line.rstrip()
                d3 = d2.replace(" ","")
                d4 = d3.replace("_"," ")
                d5 = d4.split()
            
                id = d5[0]
                name = d5[1]
                spec = d5[2]
                timing = d5[3]
                qual = d5[4]
                room = d5[5]

                docs = Doctor(id, name, spec, timing, qual, room)

                objects_doc.append(docs)
            

                dic_doctors[id] = name

                list_id.append(id)
                list_name.append(name)

        
            for item in objects_doc:
                list_doctors.append(item.__str__())

#enter info
    def enter_doc_info():
        id = input("Enter new doctor's ID: ")
        name = input("Enter new doctor's name: ")
        spec = input("Enter new doctor's speciality: ")
        timing = input("Enter new doctor's timing (e.g., 7am-10pm): ")
        qual = input("Enter new doctor's qualification: ")
        room = input("Enter new doctor's room number: ")
        doctor = Doctor(id, name, spec, timing, qual, room)
        return doctor


#format
    def format_doc_info(doctor):
        doctor = f"{doctor.get_doc_id()}_{doctor.get_doc_name()}_{doctor.get_doc_speciality()}_{doctor.get_doc_timing()}_{doctor.get_doc_qualification()}_{doctor.get_doc_room_num()}"
        return doctor

#display info
    def display_doc_info(doctor):
        print("\nId{:>10s}".format("Name"),"{:>30s}".format("Speciality"),"{:>10s}".format("Timing"),"{:>20s}".format("Qualification"),"{:>15s}".format("Room Number"))
        print(f"\n{doctor.get_doc_id():8s}{doctor.get_doc_name():25s}{doctor.get_doc_speciality():15s}{doctor.get_doc_timing():14s}{doctor.get_doc_qualification():18s}{doctor.get_doc_room_num()}")

#display list
    def display_doc_list():
    
        print("\nId{:>10s}".format("Name"),"{:>30s}".format("Speciality"),"{:>10s}".format("Timing"),"{:>20s}".format("Qualification"),"{:>15s}".format("Room Number"))
    
        for doctor in objects_doc[1:]:
            print(f"\n{doctor.get_doc_id():8s}{doctor.get_doc_name():25s}{doctor.get_doc_speciality():15s}{doctor.get_doc_timing():14s}{doctor.get_doc_qualification():18s}{doctor.get_doc_room_num()}")

#search by id
    def search_by_id():
        search_id = input("\nEnter doctor's ID: ")

        search_checker = search_id.isnumeric()
        if search_checker == True:
    
            for id in dic_doctors: 
                found_id = dic_doctors.get(search_id)

            if found_id in dic_doctors.get(search_id, []):
                index_id = list_id.index(search_id)
                doctor_found = objects_doc[index_id]
                return DoctorManager.display_doc_info(doctor_found)

            elif found_id not in dic_doctors.get(search_id, []):
                doctor_not_found = print(f"Doctor with ID {search_id} could not be found.")
                return doctor_not_found
            
        else:
            print("Invalid Input, please type a number.")

#search name
    def search_by_name():
        global index_name
        inverse_dic = {id: name for name, id in dic_doctors.items()}
        search_name = str(input("\nEnter doctor's name: "))
        search_checker = search_name.isascii()

        if search_checker == True:
            for name in inverse_dic:
                found_name = inverse_dic.get(search_name)

            if found_name in inverse_dic.get(search_name, []):
                index_name = list_name.index(search_name) 
                doctor_found = objects_doc[index_name]
                return DoctorManager.display_doc_info(doctor_found)

            elif found_name not in inverse_dic.get(search_name, []):
                doctor_not_found = print(f"{search_name} could not be found.")
                return doctor_not_found
        else:
            print("Invalid Input, please type alphabetic characters.")


#Write to file
    def write_list_of_doctors_to_file():
        with open("doctors.txt","w") as w: #missing folder path
            for line in objects_doc:
                w.write(DoctorManager.format_doc_info(line))
                w.write("\n")


#edit info
    def edit_info():
    
        search_id = input("\nEnter doctor's ID to edit their information: ")

        search_checker = search_id.isnumeric()
        if search_checker == True:
    
            for id in dic_doctors: 
                found_id = dic_doctors.get(search_id)

            if found_id in dic_doctors.get(search_id, []):
                index_id = list_id.index(search_id)

                doctor = objects_doc[index_id]
            
                doctor.set_doc_name(input("Enter new name: "))
                doctor.set_doc_speciality(input("Enter new speciality: "))
                doctor.set_doc_timing(input("Enter new timing: "))
                doctor.set_doc_qualification(input("Enter new qualification: "))
                doctor.set_doc_room_num(input("Enter new room number: "))
            
                objects_doc[index_id] = doctor
                list_doctors[index_id] = doctor.__str__()

                DoctorManager.write_list_of_doctors_to_file()
                DoctorManager.read_doc_file()

                print(f"\n{doctor.get_doc_name()} has been edited.")

            elif found_id not in dic_doctors.get(search_id, []):
                doctor_not_found = print(f"Doctor with ID {search_id} could not be found.")
                return doctor_not_found
            
        else:
            print("Invalid Input, please type a number.")

#add to file
    def add_doc_to_file():
        doctor = DoctorManager.enter_doc_info()
        objects_doc.append(doctor)
        DoctorManager.format_doc_info(doctor)
        DoctorManager.write_list_of_doctors_to_file()
        DoctorManager.read_doc_file()
        print(f"\n{doctor.get_doc_name()} has been succesfully added")

class Patient:
    def __init__(self, **kwargs):
        if kwargs is None:
            print("Error: missing arguments.")
            return

        if "pid" in kwargs: self.pid = kwargs["pid"]
        else: raise ValueError("Pid cannot be empty") 

        if "name" in kwargs: self.name = kwargs["name"]
        else: raise ValueError("Name cannot be empty")

        if "disease" in kwargs: self.disease = kwargs["disease"]
        else: raise ValueError("Disease cannot be empty")

        if "gender" in kwargs: self.gender = kwargs["gender"]
        else: raise ValueError("Gender cannot be empty")

        if "age" in kwargs: self.age = kwargs["age"]
        else: raise ValueError("Age cannot be empty")

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
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"
    

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def read_patients_file(self):
        with open("./patients.txt") as f:
            for line in f:
                if line.startswith("id"):
                    continue

                raw_patient_data = line.split("_")
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
       return f"{patient["id"]}_{patient["Name"]}_{patient["Disease"]}_{patient["Gender"]}_{patient["Age"]}"
       
    def search_patient_by_id(self):
        patient_id = input("Enter the Patient Id: ")
        
        for patient in self.patients:
            if patient["id"] == patient_id:
                print(self.format_patient_info_for_file(patient))
                return
        
        print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient):
        print(f"{patient["id"]:<5}{patient["Name"]:<16}{patient["Disease"]:<15}{patient["Gender"]:<14}{patient["Age"]}")

    def display_patients_list(self):
        print(f"\n{"ID":<5}{"Name":<16}{"Disease":<15}{"Gender":<14}Age\n")
        
        for patient in self.patients:
            self.display_patient_info(patient)

    def edit_patient_info_by_id(self):
        patient_id = input("\nEnter the Patient Id: ")
        
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
        with open("./patients.txt", "w") as f:
            f.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                f.write(self.format_patient_info_for_file(patient))

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)

        with open("./patients.txt", "a") as f:
            f.write("\n"+self.format_patient_info_for_file(new_patient))

        print(f"\nPatient whose ID is {new_patient["id"]} has been added.\n")

#main managment function
class Managment:
    def display_menu():
        while True:
            print("\nWelcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 3 to stop: \n ")
            main_menu = input("1 - Doctors\n2 - Patients\n3 - Exit Program\n>>> ")
            #nested while loops to keep the menu up each input
            #when invalid entry put in program simply ignores and keeps running
            if main_menu == "1":
                while True:
                    DoctorManager.constructor()
                    print("\nDoctors Menu:")
                    doctor_menu = input("1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n>>> ")
                    if doctor_menu == "1":
                        DoctorManager.display_doc_list()
                    elif doctor_menu == "2":
                        DoctorManager.search_by_id()
                    elif doctor_menu == "3":
                        DoctorManager.search_by_name()
                    elif doctor_menu == "4":
                        DoctorManager.add_doc_to_file()
                    elif doctor_menu == "5":
                        DoctorManager.edit_info()
                    elif doctor_menu == "6":
                        break

            elif main_menu == "2":
                while True:
                    print("\nPatients Menu:")
                    patient_menu = input("1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n>>> ")
                    if patient_menu == "1":
                        PatientManager().display_patients_list()
                    elif patient_menu == "2":
                        PatientManager().search_patient_by_id()
                    elif patient_menu == "3":
                        PatientManager().add_patient_to_file()
                    elif patient_menu == "4":
                        PatientManager().edit_patient_info_by_id()
                    elif patient_menu == "5":
                        break

            elif main_menu == "3":
                print("\nThanks for using the program. Bye!")
                break

Managment.display_menu()
