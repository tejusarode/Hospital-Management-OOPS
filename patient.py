class Patient:
    patient=[]
    last_id=0
    def __init__(self,pt_name,pt_no,pt_id=None):
        if pt_id:
            self.pt_id = int(pt_id)
        else:
            Patient.last_id += 1
            self.pt_id = int(Patient.last_id)
        self.pt_name=pt_name.title()
        self.pt_no=pt_no

    def add_patient(self):
        pt_info={"Patient id":self.pt_id,"Patient Name":self.pt_name,"Patient phone number":self.pt_no}
        p=Patient.patient.append(pt_info)
       
        return f"{self.pt_name} is added "
    
    def show_patient(self,pt_id):
        for i in Patient.patient:
            if i["Patient id"] == pt_id:
                return Patient.patient
            else:
                return f"Wrong Patient id {pt_id} entered"
    
    def update_patient(self,pt_id,new_pt_name=None,new_pt_no=None):
       for i in Patient.patient:
            if i['Patient id'] == pt_id:
                if new_pt_name:
                    i['Patient name'] = new_pt_name
                if new_pt_no:
                    i['Patient Phone number'] = new_pt_no
                return f"Doctor with id {pt_id} has been updated."
            return f"Doctor with id {pt_id} not found."
  
        