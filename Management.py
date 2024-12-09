from PatientManager import PatientManager
from DoctorManager import DoctorManager

class Management:
    def display_menu(self):
        pm = PatientManager()
        dm = DoctorManager()

        while True:
            print(
                "\nWelcome to Alberta Hospital (AH) Managment system"
                "\nSelect from the following options, or select 3 to stop: \n "
            )

            main_menu = input(
                "1 - Doctors\n"
                "2 - Patients\n"
                "3 - Exit Program\n>>> "
            )

            # nested while loops to keep the menu up each input
            # when invalid entry put in program simply ignores and keeps running
            if main_menu == "1":
                while True:
                    print("\nDoctors Menu:")

                    doctor_menu = input(
                        "1 - Display Doctors list\n"
                        "2 - Search for doctor by ID\n"
                        "3 - Search for doctor by name\n"
                        "4 - Add doctor\n"
                        "5 - Edit doctor info\n"
                        "6 - Back to the Main Menu\n>>> "
                    )

                    if doctor_menu == "1": dm.display_doc_list()
                    elif doctor_menu == "2": dm.search_by_id()
                    elif doctor_menu == "3": dm.search_by_name()
                    elif doctor_menu == "4": dm.add_doc_to_file()
                    elif doctor_menu == "5": dm.edit_info()
                    elif doctor_menu == "6": break

            elif main_menu == "2":
                while True:
                    print("\nPatients Menu:")

                    patient_menu = input(
                        "1 - Display patients list\n"
                        "2 - Search for patient by ID\n"
                        "3 - Add patient\n"
                        "4 - Edit patient info\n"
                        "5 - Back to the Main Menu\n>>> "
                    )

                    if patient_menu == "1": pm.display_patients_list()
                    elif patient_menu == "2": pm.search_patient_by_id()
                    elif patient_menu == "3": pm.add_patient_to_file()
                    elif patient_menu == "4": pm.edit_patient_info_by_id()
                    elif patient_menu == "5": break

            elif main_menu == "3":
                print("\nThanks for using the program. Bye!")
                break