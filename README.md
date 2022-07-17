
# Online Crime Reporting System in Python Project

	Modules:
The system comprises of 2 major modules with their sub-modules as follows:

1.	Admin:

•	Login: Admin can login in his personal account using id and password
•	View Complaints: Admin can view the complaints.
•	Update cases: Admin can update the crime cases.

2.	User:

•	User Registration: User has to register to file complaints, crimes or missing report.
•	User Login: User can login to system to file and check the status of his complaints or missing reports.
•	Complaints: Complaints consist of basic details the system asks and the user has to fill in order to register a complaint and check the status of his complaints.
•	Crimes: Crimes consist of all the details that the user has to fill in to register a complaint and provide a picture, if he has one related to the crime, also can check the status of the crimes he has filed.
•	Missing Persons: The System asks the user to enter all the details of the person with a photograph. The system also allows the user to check the status his previous filed cases.





## Installation

You need to have python3 , pip and pipenv installed to run project

To install pipenv on windows 

```bash
  pip install pipenv
  
```


 ## Clone Project Repository   

 ```bash
 git clone https://github.com/Maxino22/Shirlene_Project.git
  
```

 ## Install dependancies locally  

 ```bash
pipenv shell  #yo create virtuall environment

pipenv install -r requirements.txt
  
```


## Run Project

to run the project

```bash
  python manage.py runserver
  
```
