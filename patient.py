patients = {
    1: {'Name': 'Ajit Singh', 'Age': 30, 'Disease': 'Flu'},
    2: {'Name': 'Jaya Sharma', 'Age': 25, 'Disease': 'Cold'},
    3: {'Name': 'Esha Gupta', 'Age': 40, 'Disease': 'Diabetes'}
}

def get_patient_details(patient_id):
    if patient_id in patients:
        patient = patients[patient_id]
     
        return (patient['Name'], patient['Age'], patient['Disease'])
    else:
        print(f"Error: Patient with ID {patient_id} does not exist.")
        return None


patient_data = get_patient_details(1)
if patient_data:
    print(f"Patient Details: {patient_data}")

patient_data = get_patient_details(2)
if patient_data:
    print(f"Patient Details: {patient_data}")