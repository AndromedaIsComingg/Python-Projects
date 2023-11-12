# SImple_Portfolio_Website



From our command line interface, we will make sure to be in the desired working directory afterwhich we will create our project file using the command `django-admin startproject simplewebsite` with `simplewebsite` being the desired project name.
This automatically creates a folder with the project name in the directory.

<img width="684" alt="projeect start" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/7262de0a-cb9d-4f7f-b1b3-1ba0c253a21a">


Using the `cd` command. we will change directory into the newly created folder and turn on the django server with the following command `python manage.py runserver`


<img width="1075" alt="turn on server" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/0db1d9a9-6b04-4672-8d7f-7b008bbbcf2d">


This tells us that our project is now live on `127.0.0.1:8000` and we will proceed to confirm that from a web browseer


<img width="1138" alt="Django homepage" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/f41dd073-3e3d-4d0e-a9cc-1cfc10746ef2">

Seeing the Django wwelcome page above shows that we have successfully installed and launched Django


Now the next step is to customize our files and settings such that Django will serve the files we want and not the default.
For the we will be openning the files and editing them in any preferred text editor (for this we will be using `sublime text`.


##### Creating the app folder
This is where all datasese and templates will be stored, for this we will be using the command `python manage.py startapp base` please note that `base` is a desired name, and this process creates a folder named "base" in the directory. 


##### Connecting the app forlder to setting.py
This is a configuration done so that the project will be aware of the just created app

and `'base',` will be added to the list of `INSTALLED_APPS` a show in the photo below


<img width="802" alt="adding base app" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/9ee4b274-9e08-4866-9ac5-5d5eae746185">
