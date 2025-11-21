iiit_ranchi_org = {
    "Administration": {
        "Director": "Prof. Rajeev Srivastava",
        "Registrar": "Dr. Jayadeep Pati",
    },
    "Departments": {
        "Computer Science and Engineering": {
            "Professors": [
                "Prof. Rajeev Srivastava", 
                "Dr. Roshan Singh",
                "Dr. Rajiv Kumar",
                "Dr. Bharat Singh",
                "Dr. Puja Ghosh",
                "Dr. Priyank Khare",
                "Dr. Kirti Kumari",
                "Dr. Tarun Biswas",
                "Dr. Sandhir Kumar Singh",
                "Dr. Rohit Kandulna",
                "Dr. Rishikesh Dutta Tiwary",
                "Dr. Priyabrat Garanayak",
                "Dr. Nishit Malviya",
                "Dr. Ravi Shanker",
                "Dr. Shashi Kant",
                "Dr. Noopur",
                "Dr. Ranjan Kumar Behera",
                "Dr. Gaurav Sundaram",
                "Dr. Akash Srivastava",
                "Dr. N Kishore Babu",
                "Dr. Ankita Kumari",
                "Dr. Abhinav Kumar",
                "Dr. Anuj Singh",
                "Dr. Chandra Prakash Singh",
                "Dr. Amit Kumar Singh",
                "Dr. Dhiran Kumar Mahto",
                "Dr. Nitika Nigam",
                "Dr. Rajesh Dwivedi"
            ],
            "Assistant Professors": [
                "Dr. Santosh Kumar Mahto",
                "Dr. Dhananjoy Bhakta",
                "Dr. Jayadeep Pati", 
                "Dr. Shashi Kant Sharma",
                "Dr. Jitendra Kumar Mishra",
                "Dr. Rashmi Panda",
                "Dr. Priyabrat Garanayak",
                "Dr. Nishit Malviya",
                "Dr. Ravi Shanker",
                "Dr. Shashi Kant",
                "Dr. Noopur",
                "Dr. Ranjan Kumar Behera",
                "Dr. Gaurav Sundaram",
                "Dr. Akash Srivastava",
                "Dr. N Kishore Babu",
                "Dr. Ankita Kumari",
                "Dr. Abhinav Kumar",
                "Dr. Anuj Singh",
                "Dr. Chandra Prakash Singh",
                "Dr. Amit Kumar Singh",
                "Dr. Dhiran Kumar Mahto",
                "Dr. Nitika Nigam",
                "Dr. Rajesh Dwivedi"
            ]
        }
    }
}

prof_name = input("Enter the name of the professor: ").strip().lower()

found = False
for department, staff in iiit_ranchi_org["Departments"].items():
    professors = [name.lower() for name in staff.get("Professors", [])]
    assistants = [name.lower() for name in staff.get("Assistant Professors", [])]

    if prof_name in assistants:
        print(f"\nAssistant Professor {prof_name.title()} found!")
        print(f"Department: {department}")
        found = True
        break
    elif prof_name in professors:
        print(f"\nProfessor {prof_name.title()} found!")
        print(f"Department: {department}")
        found = True
        break

if not found:
    print("Professor not Found!!!")
