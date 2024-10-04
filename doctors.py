from reception import Reception
class Doctors:
    doctors=[]
    appointment=[]
    def __init__(self,dr_id,dr_name,specialist,dr_no):
        self.dr_id=dr_id
        self.dr_name=dr_name.title()
        self.specialist=specialist
        self.dr_no=dr_no

    
    def add_doctors(self):
        dr_info={'Doctor Id':self.dr_id,'Doctor name':self.dr_name,'Specialist':self.specialist,'Doctor Phone number':self.dr_no}
        Doctors.doctors.append(dr_info)
        return f"{self.dr_name} has been added."
    
    def show_dr_info(self):
        return Doctors.doctors
    
    def update_doctors(self,dr_id,new_dr_name=None,new_dr_no=None):
       for i in Doctors.doctors:
            if i['Doctor Id'] == dr_id:
                if new_dr_name:
                    i['Doctor name'] = new_dr_name
                if new_dr_no:
                    i['Doctor Phone number'] = new_dr_no
                return f"Doctor with id {dr_id} has been updated."
            return f"Doctor with id {dr_id} not found."

    def show_appointment(self,dr_id):
        appointments = []
        for i in Reception.appointment:
            if i['dr_id'] == dr_id:
                print(i)
                self.appointment.append(i)
        if appointments:
            return appointments
        return f"No appointments found for doctor with id {dr_id}."
        
