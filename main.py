from doctors import Doctors
from reception import Reception
from patient import Patient


def display_menu():
    print("\nMenu:")
    print("1. Book an appointment")
    print("2. Show Doctor info")
    print("3. Show Patient info")
    print("4. Book an ward")
    print("5. Discharge the patient")
    print("6. Show appointments")
    print("7. Update Doctor information")
    print("8. Update Patient information")
    print("9. Exit")

#Adding doctor
doc1=Doctors(1,"Gauri Pawar","Dentist",7537573)
doc2=Doctors(2,"jisa Saji","General Physician",3533434)
doc3=Doctors(3,"Madina Mirza","Gynaecologist",4344546757)
doc4=Doctors(4,"Vrukshali Pangam","Skin",243654765)
doc1.add_doctors()
doc2.add_doctors()
doc3.add_doctors()
doc4.add_doctors()

#Adding patient
pt_id=input("Enter patient id or leave blank: ")
pt_name=input("Enter patient_name : ").title()
pt_no=int(input("Enter patient phone number : "))
pt=Patient(pt_name,pt_no,pt_id)
pt.add_patient()


#adding wards
r=Reception()
w1=r.add_ward(1,101,0)
w2=r.add_ward(2,102,0)
w3=r.add_ward(3,111,1)
w4=r.add_ward(4,112,1)

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":

        print("\nBook an appointment : ")
        dr_id=int(input("Enter Doctor id : "))
        pt_id=int(input("Enter Patient id : "))
        pt_name=input("Enter Patient name : ").title()
        dr_name=input("Enter Doctor name : ").title()
        date=input("Enter Date : ")
        time=input("Enter time in 24 hrs format : ")
        r.add_appointment(dr_id,pt_id,pt_name,dr_name,date,time)
    elif choice == "2":
        print("\nDoctor Info : ")
        print(doc1.show_dr_info())
    elif choice=='3':
        print("\nPatient Info : ")
        pt_id=int(input("Enter patient id : "))
        print(pt.show_patient(pt_id))
    elif choice=='4':
        print("\nBook an ward")
        print(r.wards)
        ward_id=int(input("Enter ward id : "))
        pt_id=int(input("Enter Patient id : "))
        pt_name=input("Enter patient name : ").title()
        date=input("Enter Date : ")
        time=input("Enter time in 24hrs format : ")
        print(r.book_wards(ward_id,pt_id,pt_name,date,time))
    elif choice=='5':
        print("\nDischarge to patient")
        ward_id=int(input("Enter the ward_id : "))
        print(r.delete_wards(ward_id))
    elif choice=='6':
        print("\nShow appointments scheduled")
        dr_id=int(input("Enter the Doctor id : "))
        # pt_id=input("Enter the Patient id : ")
        # date=input("Enter the date : ")
        # time=input("Enter the time : ")
        print(doc1.show_appointment(dr_id))
    elif choice=='7':
        print("\nUpdate Doctor Info")
        dr_id=int(input("Enter Doctor id : "))
        print('1. Update Dr name')
        print('2. Update Dr number')
        choose=input("Enter 1 or 2 : ")
        if choose=='1':
            dr_name=input("Enter Doctor name : ").title()
            doc1.update_doctors(dr_id,dr_name)
        elif choose=='2':
            dr_no=input("Enter Doctor phone number :")
            doc1.update_doctors(dr_id,dr_no)
        else:
            print("Wrong input given")
    elif choice=='8':
        print("\nUpdate Patient Info")
        pt_id=int(input("Enter Patient id : "))
        print('1. Update Patient name')
        print('2. Update Patient number')
        choose=input("Enter 1 or 2 : ")
        if choose=='1':
            pt_name=input("Enter Patient name : ").title()
            pt.update_patient(pt_id,pt_name)
        elif choose=='2':
            pt_no=input("Enter Patient phone number :")
            pt.update_patient(pt_id,pt_no)
        else: 
            print("Wrong input given")
    elif choice =='9':
        break
    else:
        print("Wrong input given")
    
