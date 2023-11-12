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


##### Creating template directory
In the base folder, we will be creating a folder named `templates` inside which we will create another folder which corresponds with the app folder named `base`.
inside the "base" folder we will create an `html` file which we will name `home.html` and save the demo script `<h3>Hello world</h3>`


<img width="752" alt="homeHTML created" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/7edacadd-6897-4761-9299-4c57a37fecb4">



##### Adding the template folder in `settings.py`
This is done so that the just created `template` folder with be recognised in the configuration.

This is done by adding the following lines of code to the `settings.py` file
``` python
import os
TEMPLATES = [
    {
        
        'DIRS': [os.path.join('', 'templates'),
                 os.path.join('', 'base', 'templates', 'base'),
                
                ]
    }
]
```


<img width="908" alt="settings template" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/7890bccd-498d-4db6-b345-e125bc5e7aed">



##### Creating function to render template
We will have create a function that will render this template, and this configuration is done in the file named `view.py` which is located in the outter "base" folder


The `views` configuration basically functions that take in a request as return an http response, templates, etc..
This will be done by adding the following lines of code
``` python
def home(request):
	return render(request, 'base/home.html')
```

this fucntion returns the template


<img width="936" alt="views" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/09975638-d6b0-48c2-a36c-89bdc73ad3a6">


##### Creating a URL routing system
In the `base` app folder, we will create another file called `urls.py`


This will be responsible for calling the function `home`, which will in turn render the template `home.html`


<img width="909" alt="urls config" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/b257ce11-d749-42af-8a5d-0a82f0bc7978">


##### Configuring base urls.py file
There is another file `urls.py` created by default in the `base/simplewebsite/` folder, this default one needs to be configured to recognise the one we created by using the `include` method


<img width="1178" alt="urls 1" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/b3890e87-c6b7-4270-8c70-6652880ad16c">


Which we will edited to :
``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
```

<img width="1135" alt="urls 2" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/7b7e3bbb-e11a-4223-a98f-38e5887b7536">


Now we should be able to run our server to confirm the configuration
We will be doing that from the cli using the command `python manage.py runserver`
