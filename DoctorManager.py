from Doctor import Doctor

class DoctorManager:
    def __init__(self):
        self.list_doctors = []
        self.objects_doc = []

        self.list_id = []
        self.list_name = []
        self.dic_doctors = {}
 
        #   Constructor creates an empty list and calls a function to read doctors.txt file and append this 
        #   information on the list.
        self.read_doc_file()


    # Read doctor file
    def read_doc_file(self):
        #   read_doc_file function uses 3 different lists and a dictionary to be used on later parts of the code.
        #   List objects_doc has the objects type of Doctors, list_doctors has the __str__() function of these objects.

        with open("Project Data/doctors.txt" ,"r") as d:
            for line in d:
                # Process to sort the information of doctors in
                # various lists depending on the length of the file.
                line = line.rstrip().split("_")

                # Each value in the list is sorted to
                # create a object for each doctor in the file.
                doc_id = line[0]
                name = line[1]

                docs = Doctor(
                    doctor_id = doc_id,
                    name = name,
                    speciality = line[2],
                    timing = line[3],
                    qualification = line[4],
                    room_number = line[5]
                )

                # Doctor objects are appended into objects_doc list.
                self.objects_doc.append(docs)
                # This dictionary is useful to find a doctor through their ID and Name.
                self.dic_doctors[doc_id] = name
                # Both lists are useful for search_by_id and search_by_name functions.
                self.list_id.append(doc_id)
                self.list_name.append(name)

            #  For loop to append the __str__() representation of
            # each object into another list to make it easier to format it.
            for item in self.objects_doc:
                self.list_doctors.append(item.__str__())

    def enter_doc_info(self):
        doctor_id = input("Enter new doctor's ID: ")
        name = input("Enter new doctor's name: ")
        spec = input("Enter new doctor's speciality: ")
        timing = input("Enter new doctor's timing (e.g., 7am-10pm): ")
        qual = input("Enter new doctor's qualification: ")
        room = input("Enter new doctor's room number: ")

        doctor = Doctor(
            doctor_id = doctor_id,
            name = name,
            speciality = spec,
            timing = timing,
            qualification = qual,
            room_number = room
        )

        return doctor


    def format_doc_info(self, doctor):
        # Function to format a single doctor object through
        # getters to add a doctor object type into the doctors.txt file.
        doctor = f"{doctor.get_doc_id()}_{doctor.get_doc_name()}_{doctor.get_doc_speciality()}_{doctor.get_doc_timing()}_{doctor.get_doc_qualification()}_{doctor.get_doc_room_num()}"
        return doctor


    def display_doc_info(self, doctor):
        # Displaying a single doctor object thorugh its getters when finding a doctor by their ID or name.
        print("\nId{:>10s}".format("Name"),"{:>30s}".format("Speciality"),"{:>10s}".format("Timing"),"{:>20s}".format("Qualification"),"{:>15s}".format("Room Number"))
        print(f"\n{doctor.get_doc_id():8s}{doctor.get_doc_name():25s}{doctor.get_doc_speciality():15s}{doctor.get_doc_timing():14s}{doctor.get_doc_qualification():18s}{doctor.get_doc_room_num()}")


    def display_doc_list(self):
        print("\nId{:>10s}".format("Name"),"{:>30s}".format("Speciality"),"{:>10s}".format("Timing"),"{:>20s}".format("Qualification"),"{:>15s}".format("Room Number"))

        # Formatting and displaying every doctor object in the doctor's list through its getters.
        for doctor in self.objects_doc:
            print(f"\n{doctor.get_doc_id():8s}{doctor.get_doc_name():25s}{doctor.get_doc_speciality():15s}{doctor.get_doc_timing():14s}{doctor.get_doc_qualification():18s}{doctor.get_doc_room_num()}")


    def search_by_id(self):
        search_id = input("\nEnter doctor's ID: ")

        search_checker = search_id.isnumeric()
        if search_checker == True:
            #   Iterating through the dictionary created in read_doc_file function to find the desired doctor.
            for _id in self.dic_doctors: 
                found_id = self.dic_doctors.get(search_id)
                #   If the ID is found then iterates through a list containing each doctor ID, also created in read_doc_file.
            if found_id in self.dic_doctors.get(search_id, []):
                index_id = self.list_id.index(search_id)
                #   doctor_found is equal to the object of the ID found. Then returns display_doc_info of the found doctor.
                doctor_found = self.objects_doc[index_id]
                return self.display_doc_info(doctor_found)
            #   If the ID is not found then print that this ID is not valid.
            elif found_id not in self.dic_doctors.get(search_id, []):
                doctor_not_found = print(f"Doctor with ID {search_id} could not be found.")
                return doctor_not_found
            
        else:
            print("Invalid Input, please type a number.")


    def search_by_name(self):
        #   Making an inverse dictionary to get the name of the doctor instead of their ID.
        inverse_dic = {id: name for name, id in self.dic_doctors.items()}
        search_name = str(input("\nEnter doctor's name: "))
        search_checker = search_name.isascii()

        if search_checker == True:
            #   Iterating through the inverse dictionary to find the desired doctor.
            for name in inverse_dic:
                found_name = inverse_dic.get(search_name)
            #   If the name is found then iterates through a list containing each doctor name, also created in read_doc_file.
            if found_name in inverse_dic.get(search_name, []):
                index_name = self.list_name.index(search_name) 
            #   doctor_found is equal to the object of the name found. Then returns display_doc_info of the found doctor.
                doctor_found = self.objects_doc[index_name]
                return self.display_doc_info(doctor_found)
            #   If the name is not found then print that this name is not valid.
            elif found_name not in inverse_dic.get(search_name, []):
                doctor_not_found = print(f"{search_name} could not be found.")
                return doctor_not_found
        else:
            print("Invalid Input, please type alphabetic characters.")


    def write_list_of_doctors_to_file(self):
        #   The file to write the infotmation on NEEDS to be contained in a folder called "Project Data"
        with open("Project Data/doctors.txt","w") as w:
            for line in self.objects_doc:
                #   Formats each information obtained on each doctor type object.
                w.write(self.format_doc_info(line))
                w.write("\n")


    def edit_info(self):
        #   Same process of the search_by_id function to find the ID of the desired doctor.
        search_id = input("\nEnter doctor's ID to edit their information: ")

        search_checker = search_id.isnumeric()
        if search_checker == True:

            for id in self.dic_doctors: 
                found_id = self.dic_doctors.get(search_id)

            if found_id in self.dic_doctors.get(search_id, []):
                index_id = self.list_id.index(search_id)
                #   doctor variable means the doctor object type of the found ID.
                doctor = self.objects_doc[index_id]
                #   Using setters to modify information of the desired doctor.
                doctor.set_doc_name(input("Enter new name: "))
                doctor.set_doc_speciality(input("Enter new speciality: "))
                doctor.set_doc_timing(input("Enter new timing: "))
                doctor.set_doc_qualification(input("Enter new qualification: "))
                doctor.set_doc_room_num(input("Enter new room number: "))
                #   Appending this new information into the objects list and __str__() list.
                self.objects_doc[index_id] = doctor
                self.list_doctors[index_id] = doctor.__str__()
                #   Writing this new information into the file, and then reading the file again to update every list.
                self.write_list_of_doctors_to_file()
                # self.read_doc_file()

                print(f"\n{doctor.get_doc_name()} has been edited.")

            elif found_id not in self.dic_doctors.get(search_id, []):
                doctor_not_found = print(f"Doctor with ID {search_id} could not be found.")
                return doctor_not_found
            
        else:
            print("Invalid Input, please type a number.")


    def add_doc_to_file(self):
        #   Adding to doctor file requires to call every other function setted in DoctorManager class.
        print("")
        #   Starts with entering the new information for a new doctor.
        doctor = self.enter_doc_info()
        #   Appends this new doctor into the doctor's file.
        self.objects_doc.append(doctor)
        #   Formats it before writing it into the list.
        self.format_doc_info(doctor)
        #   Writes the new information into the file.
        self.write_list_of_doctors_to_file()
        #   Reads file to update all lists.
        #   self.read_doc_file()
        print(f"\n{doctor.get_doc_name()} has been succesfully added")