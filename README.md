# OnlineTestAPI
## Setup libraries and Environment for using OnlineTestAPI 
### Firstly Install python virtual environment and install django and djangorestframework in python virtualenvironment.
#### install virtualenv :
> pip install virtualenv
#### create python virtualenvironment :
>  virtualenv venv
#### activate virtualenv/venv :
>  venv\Scripts\activate.bat <br> this will activate virtual environment
#### after that install django , djangorestframework and required python libraries by :
1. Use already existing requirements.txt file which contain all required python libraires
> pip install -r requirements.txt
### or 
2. Install them individually
> pip install dango dangorestframework
##### With this all required python libraries and environment will setup in the system.
## About App Folder Contain and its function :
#### accounts app folder : 
> This accounts app folder contains account or user credentials related functionalities 
> This app have custom User of User database model(Table)
> it also have contains register, login and logout.
#### exam app folder :
> This exam app folder have all exam related database models
> this app contain serializers of exam.models 
> this app have function like creating exam, Questions, Option which is access /integrated by MCQ db model as whole
> other functions are exam question list, exam scchedule ,  examschedulelist.
