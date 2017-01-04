Features:
1.	Able to Sign up and Login.
2.	Ability to Upload Photos
3.	Ability to add Captions
4.	Can edit Captions
5.	Can delete photos
6.	Able to Logout
7.	10 photos per Page and ability to move next and previous
8.	Only PNG, GIF and JPG files are accepted, rest are ignored.
9.	All photos are sorted with most recent one first.

Instructions on How to run Photogram

1.	Install Python 2.7 https://www.python.org/download/releases/2.7/
2.	Install pip https://pip.pypa.io/en/stable/installing/
3.	Install Django    Run command “pip install Django”
4.	Run command “pip install Pillow”
5.	Copy project to your workarea
6.	Change directory to photogram
7.	Run command “python manage.py makemigrations photolist”
8.	Run command “python manage.py migrate”
9.	Run command “python manage.py runserver 8080”
10.	Go to your browser and point URL to http://localhost:8080/photogram/

Site Usage:
1.	Click on Not a member, click here to Register. If already registered, then login.
2.	Enter your details and click on Register. Will Login automatically.
3.	Click on Choose File to select a photo and click Upload. Caption is optional
4.	To Edit caption, click Edit Caption below picture.
5.	To delete photo, click on delete.


This site uses Django + python + PIL (Image validation) + sqlite (in built database)










Code Documentation:

Photolist contains the source code of this application

Folder Structure:
1.	Static – All static files like css, images and jss are stored here.
2.	Templates – All the html files are stored here.
3.	The python files are present in the current directory.

Python Files:
1.	Admin.py   & Apps. Py – Part of Framework
2.	Forms.py contains the Form Class that defines the uploaded data.
3.	Models.py contains the model class that is used to persist into the sqlite database.
4.	 Urls. Py contains all URL mapping.
5.	Views.py contains all the view handlers.


