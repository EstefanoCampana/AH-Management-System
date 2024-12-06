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
        with open("Project Data/doctors.txt" ,"r") as d:
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
    
        for doctor in objects_doc:
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
        with open("Project Data/doctors.txt","w") as w:
            for line in objects_doc:
                w.write(DoctorManager.format_doc_info(line))
                w.write("\n")


#edit inof
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
        print("")
        doctor = DoctorManager.enter_doc_info()
        objects_doc.append(doctor)
        DoctorManager.format_doc_info(doctor)
        DoctorManager.write_list_of_doctors_to_file()
        DoctorManager.read_doc_file()
        print(f"\n{doctor.get_doc_name()} has been succesfully added")


DoctorManager.constructor()
DoctorManager.display_doc_list()
DoctorManager.search_by_id()
DoctorManager.search_by_id()
DoctorManager.search_by_name()
DoctorManager.search_by_name()
DoctorManager.add_doc_to_file()
DoctorManager.display_doc_list()
DoctorManager.edit_info()
DoctorManager.display_doc_list()