# Django secret key generator
This is simple django secret key generator application designed in FLASK.

This simple appliucation is used to generate the SECRET_KEY that you can put in your
django applications settings.py file.

For more information on secret key in django, please refer thread in [stackoverflow](https://stackoverflow.com/questions/7382149/whats-the-purpose-of-django-setting-secret-key)

Requirements
------------
1. Python 3.8 and above
2. Flask 1.0.3
3. Git

Installing Instructions
-----------------------
1. Pull the source code from git using below url
   git pull https://github.com/harish-bhat-m/django-secret-key-generator.git
   cd django-secret-key-generator

2. Install Python3 Virtual Environment. Depending upon your operating system.
   
3. Create virtual environemnet using blow command.
   Linux : python3 -m venv <your virtual environment name>
   Windows: virtualenv <your virtual env name>

4. Activate created virtual environment.
   Linux: source <your virtual env name>/bin/activate
   Windows: venv/Scripts/activate

5. Install the project depedacies using below command.
   pip install -r requirements.txt

6. Run the application from local server using the shell script
   sh load_application.sh
