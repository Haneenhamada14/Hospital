# Initialize empty queues for each specialization
queues = {'Children': [], 'Surgery': [], 'Cardiology': [], 'Neurology': [], 'Oncology': [],
          'Gynecology': [], 'Orthopedics': [], 'Dermatology': [], 'Psychiatry': [], 'Urology': [],
          'Endocrinology': [], 'Gastroenterology': [], 'Hematology': [], 'Infectious Diseases': [],
          'Nephrology': [], 'Pulmonology': [], 'Radiology': [], 'Rheumatology': [], 'Ophthalmology': []}

# Function to add a new patient to a queue
def add_patient():
    print("Specializations:")
    print(list(queues.keys()))
    spec = input("Enter specialization: ")
    if spec not in queues:
        print("Invalid specialization.")
        return
    if len(queues[spec]) >= 10:
        print(f"{spec} queue is full.")
        return
    name = input("Enter patient name: ")
    queues[spec].append(name)
    print(f"{name} added to {spec} queue.")

# Function to print all patients in all queues
def print_patients():
    for spec, queue in queues.items():
        if len(queue) > 0:
            print(f"{spec} queue:")
            for i, name in enumerate(queue):
                print(f"{i+1}. {name}")
        else:
            print(f"{spec} queue is empty.")

# Function to get the next patient from a queue
def get_next_patient():
    spec = input("Enter specialization: ")
    if spec not in queues:
        print("Invalid specialization.")
        return
    if len(queues[spec]) == 0:
        print(f"{spec} queue is empty.")
        return
    name = queues[spec].pop(0)
    print(f"Next patient in {spec} queue is {name}.")

# Function to remove a leaving patient from a queue
def remove_patient():
    spec = input("Enter specialization: ")
    if spec not in queues:
        print("Invalid specialization.")
        return
    if len(queues[spec]) == 0:
        print(f"{spec} queue is empty.")
        return
    name = input("Enter patient name: ")
    if name not in queues[spec]:
        print(f"{name} is not in {spec} queue.")
        return
    queues[spec].remove(name)
    print(f"{name} removed from {spec} queue.")

# Main program loop
while True:
    print("\nProgram Options:")
    print("1) Add new patient")
    print("2) Print all patients")
    print("3) Get next patient")
    print("4) Remove a leaving patient")
    print("5) End the program")

    choice = input("\nEnter your choice (from 1 to 5): ")

    if choice == '1':
        add_patient()
        
    elif choice == '2':
        print_patients()
        
    elif choice == '3':
        get_next_patient()
        
    elif choice == '4':
        remove_patient()
        
    elif choice == '5':
        break
        
print("\nProgram ended.")

# Step 1: Ask for the specialization number
specialization_num = int(input("Please enter the specialization number (1-20) where you want to add a new patient: "))

# Step 2: Ask for the patient's name
patient_name = input("Please enter the name of the new patient: ")

# Step 3: Ask for the patient's status
patient_status = int(input("Please enter the status of the new patient (0=normal, 1=urgent, 2=super urgent): "))

# Step 4: Check if there are already 10 patients in this specialization
if len(hospital_system[specialization_num]) >= 10:
    print("Sorry, there are already 10 patients in this specialization. Cannot accept new patient.")
else:
    # Step 5: Add the new patient according to their status
    if patient_status == 0:
        hospital_system[specialization_num].append(patient_name)
    elif patient_status == 1:
        for i in range(len(hospital_system[specialization_num])):
            if hospital_system[specialization_num][i] == "normal":
                hospital_system[specialization_num].insert(i, patient_name)
                break
        else:
            hospital_system[specialization_num].append(patient_name)
    elif patient_status == 2:
        for i in range(len(hospital_system[specialization_num])):
            if hospital_system[specialization_num][i] == "normal" or hospital_system[specialization_num][i] == "urgent":
                hospital_system[specialization_num].insert(i, patient_name)
                break
        else:
            hospital_system[specialization_num].append(patient_name)

    print(f"The new {status[patient_status]} patient {patient_name} has been added to specialization {specialization_num} {position[patient_status]}")
# Define a dictionary to store the patient queue for each specialization
patient_queues = {
    'cardiology': [],
    'neurology': [],
    'oncology': []
}

# Function to add a patient to the queue for a given specialization
def add_patient(specialization, patient):
    patient_queues[specialization].append(patient)

# Function to get the next patient for a given specialization
def get_next_patient(specialization):
    if len(patient_queues[specialization]) > 0:
        # Get the top patient from the queue
        next_patient = patient_queues[specialization][0]
        # Remove the top patient from the queue
        del patient_queues[specialization][0]
        return next_patient
    else:
        # Inform the doctor that there are no patients in the queue
        print(f"No patients in {specialization} queue")

# Example usage:
add_patient('cardiology', 'John')
add_patient('cardiology', 'Mary')
add_patient('neurology', 'Bob')

next_patient = get_next_patient('cardiology')
print(f"Next cardiology patient: {next_patient}")

next_patient = get_next_patient('neurology')
print(f"Next neurology patient: {next_patient}")

next_patient = get_next_patient('oncology') # No patients in oncology queue   

# create a list of patients with their specialization and name
patients = [
    {"specialization": "Cardiology", "name": "John Doe"},
    {"specialization": "Neurology", "name": "Jane Smith"},
    {"specialization": "Oncology", "name": "Bob Johnson"}
]

# get input from user for the leaving patient's specialization and name
leaving_specialization = input("Enter specialization of leaving patient: ")
leaving_name = input("Enter name of leaving patient: ")

# loop through the list of patients to find the leaving patient
for i in range(len(patients)):
    if patients[i]["specialization"] == leaving_specialization and patients[i]["name"] == leaving_name:
        # remove the leaving patient from the list
        del patients[i]
        print(f"{leaving_name} ({leaving_specialization}) has been removed from the system.")
        break
else:
    # if no such person is found, inform the user
    print(f"No record found for {leaving_name} ({leaving_specialization}).")