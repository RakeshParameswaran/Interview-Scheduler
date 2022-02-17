-- Steps for running the project locally --

1. Initially in the virtual environment created, after activating the same. Navigate to the project folder, use " pip install -r requirements.txt " to install the 
required packages for running the project. 
2. Use "python manage.py runserver" to run the project and click on " http://127.0.0.1:8000/  "
3. In the github repository I have added the db.sqlite3 file and migrations files as well. So the data will be available.
4. In order to access the admin using super user. The credentials are:
	Username : Admin
	Password : Entri1234
5. In case if you are not considering the migrations files and db file. You may have to do,
	1. python manage.py migrate
	2. python manage.py makemigrations
	3. python manage.py migrate
in this order respectively.

6. In order to create a super user to access admin. Use "python manage.py createsuperuser".


--- Assumptions made ---

I have assumed the interview slots to be between 9 AM and 7 PM. Also the initial value for time slots are set as 9 AM and 10 AM. I have assumed the
whole task as a website which enables a student to enter his/her timings through a form, same is the case with interviewer. The availability can be checked
by clicking on Check Availability button in the homepage and entering the id s of both student and interviewer. I have also added the student and interviewer 
data in a table for ease of identifying their id s.


