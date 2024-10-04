class Reception:
    appointment=[]
    wards=[]
    booked_wards=[]

    #Book an appointment
    def add_appointment(self,dr_id,pt_id,pt_name,dr_name,date,time):
        if Reception.appointment:
            for i in Reception.appointment:
                if i['dr_id']==dr_id:
                    if i['date']==date:
                        if i['time']==time:
                            print("Appointment slot already taken")
                else:
                    Reception.appointment.append({"dr_id":dr_id,"pt_id":pt_id,"pt_name":pt_name,"dr_name":dr_name,"date":date,"time":time})
                    print("Appointment was scheduled succesfully this ")
                    break
        else:
            Reception.appointment.append({"dr_id":dr_id,"pt_id":pt_id,"pt_name":pt_name,"dr_name":dr_name,"date":date,"time":time})
            print("Appointment was scheduled succesfully this ")
        print("Appointment was scheduled succesfully")

    #Ward availability
    def show_available_wards(self):
        return Reception.wards
    
    #adding ward
    def add_ward(self,ward_id,room_no,floor_no):
        ward={"ward id":ward_id,"room number":room_no,"floor number":floor_no}
        Reception.wards.append(ward)
    
    #Admitting Patient
    def book_wards(self,ward_id,pt_id,pt_name,date,time):
        for i in Reception.wards:
            if i['ward id'] == ward_id:
                Reception.booked_wards.append({'Ward id':ward_id,'patient id':pt_id,'patient name':pt_name,'date':date,'time':time})
                Reception.wards.remove(i)
            else:
                return "ward not available"
    
    #Discharging patient
    def delete_wards(self,ward_id):
        for i in Reception.booked_wards:
            if ward_id in self.wards:
                a=Reception.booked_wards.remove(ward_id)
                Reception.wards.append(i)
                return f"{ward_id} was removed sucessfully"
            else:
                print(f'Ward {ward_id} not found.')

    #Will give all the ward info
    def ward_info(self):
        return {'available wards':Reception.wards,'Booked wards':Reception.booked_wards}   
