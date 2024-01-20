# Simple_Portfolio_Website
##### This project is a simple portfolio website created with `Django`


It demonstrates the application of `Django` with `Python` as a very powerful web framework.
`Django` is a high-level web framework written in Python that encourages rapid development and clean, pragmatic design. It follows the Model-View-Controller (MVC) architectural pattern, but in `Django`, it's often referred to as the Model-View-Template (MVT) pattern.
The goal of this is to show the elegance of `Django` as a web framework of `Python`, where a simple template is created in an app, and how a `Python` function was created to render this function.
This project also shows how to create and use static files.


##### Prerequisites
- Python 
- Pip
- Django
- Command Line Interface
- Text Editor
  

From the command line interface(CLI), we will make sure to be in the desired working directory afterwhich we will create our project file using the command `django-admin startproject simplewebsite` with `simplewebsite` being the desired project name.
This automatically creates a folder with the project name in the directory.

<img width="684" alt="projeect start" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/7262de0a-cb9d-4f7f-b1b3-1ba0c253a21a">


Using the `cd` command, we will change directory into the newly created folder and turn on the django server with the following command `python manage.py runserver`


<img width="1075" alt="turn on server" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/0db1d9a9-6b04-4672-8d7f-7b008bbbcf2d">


This tells us that our project is now live on `127.0.0.1:8000` and we will proceed to confirm that from a web browseer


<img width="1138" alt="Django homepage" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/f41dd073-3e3d-4d0e-a9cc-1cfc10746ef2">

Seeing the Django wwelcome page above shows that we have successfully installed and launched `Django`


The next step is to customize our files and settings such that Django will serve the files we want and not the default.
For that we will be openning some files and editing them in any preferred text editor (for this we will be using `sublime text`.


##### Creating the app folder
This is where all databases and templates will be stored, for this we will be using the command `python manage.py startapp base` please note that `base` is a desired name, and this process creates a folder named "base" in the directory. 


##### Connecting the app folder to setting.py
This is a configuration done so that the project will be aware of the just created app

In `settings.py`, `'base',` will be added to the list of `INSTALLED_APPS` as shown in the photo below


<img width="802" alt="adding base app" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/9ee4b274-9e08-4866-9ac5-5d5eae746185">


##### Creating template directory
In the base folder, we will be creating a folder named `templates` inside which we will create another folder which corresponds with the app folder named `base`.
inside the "base" folder we will create an `html` file which we will name `home.html` and save a demo script `<h3>Hello world!</h3>`


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
We will create a function that will render this template, and this configuration is done in the file named `view.py` which is located in the outter "base" folder


The `views` configuration basically houses functions that take in a request as return an http response, templates, etc..
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


<img width="793" alt="Hello world" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/c997b38c-ba0b-4aaa-85e6-d5b234300a8e">

This shows that our template is well rendered


##### Creating paths and files for static files
We will be doing this by created a new folder in our root directory `simplewebsite`, this is where we will store our images, css, and javascript etc.


We will name this folder `staticfiles` inside which we will create a folder for all images named `images`, a folder for all css files named `css`, inside which we will create a css file named `main.css`


<img width="570" alt="staticfiles dir" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/bbd8d525-14b1-4e47-8cc5-a5e07c4cd6e6">


##### Configuring `settings.py` to recognise static files & paths

From the `settings.py` file we are going to edit the `STATIC_URL = '/static/'` to `STATIC_URL = '/staticfiles/'`


We will also add the line `MEDIA_URL = `'/images/'` so that the image directory will be recognised

Also, we will add the line 
``` python
STATICFILES_DIRS = [
   os.path.join('', 'staticfiles')


<img width="892" alt="static dir edit" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/8cf7affe-05c6-463c-9f3c-5431eb42f2d1">



]
```
this is to direct the configuration to the folder `staticfiles`


In the `home.html` file we will paste and save the following lines of code:

``` html

{% load static %}

<!DOCTYPE html>
<html>
<head>
	<title>Stephen Olaleye</title>
	<link href="{% static '/css/main.css'  %}" rel="stylesheet" type="text/css">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
	
</head>
<body>
	<br>
	<div class="container">
		<div class="row">
			<div class="col-md-3">
				<div class="card card-body h-100  border-info" id="profile-wrapper">
					<img id="profile-pic" src="{% static 'images/steev.jpeg' %}" >
					<hr>
					<h4>Hi i am Stephen Olaleye!</h4>
					<p>I am a Python developer and a DevOps Engineer</p>
				</div>
			</div>

			<div class="col-md-9">
				<div class="card card-body h-100  border-info">
					<h4>Who i am</h4>
					<hr>
					<p>A versatile Python Developer/DevOps Engineer with a proven track record of creating efficient, scalable software solutions and streamlining deployment processes. Experienced in full-stack development, cloud technologies, and automation tools. 
					I have strong problem-solving skills, a commitment to continuous improvement, and a proactive approach to challenges. Adept at collaborating with cross-functional teams to drive project success and enhance operational efficiency. I actively seek opportunities to apply my expertise in delivering robust software and optimising DevOps pipelines.</p>

					<ul class="social-links">
						<li><img class="social" src="{% static 'images/facebook.png' %}"></li>
						<li><img class="social" src="{% static 'images/linkedin.png' %}"></li>
						<li><img class="social" src="{% static 'images/twitter.png' %}"></li>
						<li><img class="social" src="{% static 'images/youtube.png' %}"></li>
					</ul>

				</div>
			</div>
		</div>
		<br>
		<div class="row">
			<div class="col-md-6">
				<div class="card card-body h-100">
					<h5>Professinal Summary</h5>
					<hr>
					<p>Python Developer</p>

					<p>•	Designing, coding, and maintaining Python applications, modules, and libraries to meet project requirements.

					<p>	•	Collaborating with cross-functional teams, including front-end developers, back-end developers, and stakeholders to deliver comprehensive solutions.</p>

					<p>	•	Optimising code for performance and efficiency, ensuring the application runs smoothly and efficiently.</p>

					<p>	•	Conducting unit and integration testing, debugging code, and resolving issues to maintain code 			quality.</p>

					<p>	•	Managing and maintaining code repositories using version control systems such as Git.</p>

					<p>	•	Creating and maintaining technical documentation, including code comments and system architecture 		documentation.</p>

					<p>	•	Integrating third-party APIs and services into Python applications, ensuring seamless data 				exchange.</p>

					<p>	•	Developing and maintaining database structures and queries, often using technologies like SQL or 		 NoSQL databases.</p>
					<p>	•	Implementing security best practices to protect applications and data, including authentication, 		 authorization, and encryption.</p>

					<p>	•	Monitoring and analysing application performance, identifying and addressing bottlenecks and scaling issues.
						</p>
					</div>
			</div>

			<div class="col-md-6">
				<div class="card card-body h-100">
					<h5>Professional Summary</h5>
					<hr> DevOps Engineer
					<p>
					<p>•	Actively contributing to the establishment of CI/CD pipelines, gaining hands-on experience in the end-to-end software delivery process.

					<p>	•	Immersed in the world of Infrastructure as Code, utilizing tools like Terraform to automate cloud resource management under mentorship.

					<p>	•	Collaborating with the development team using Git for version control, actively participating in collaborative coding practices.

					<p>	•	Learning the fundamentals of containerization with Docker, contributing to the deployment consistency of applications.

					<p>	•	Actively involved in tasks related to cloud platforms (e.g., AWS, Azure, or Google Cloud), contributing to resource optimization and scalability.

					<p>	•	Exploring scripting languages like Bash and Python to automate routine tasks, enhancing efficiency and automation skills.

					<p>	•	Assisting in the setup and understanding of monitoring tools, actively participating in the identification and response to potential issues.

					<p>	•	Engaging in collaborative problem-solving with the team, providing support and contributing to solutions for improved system performance.

					<p>	•	Developing an understanding of security measures, including authentication and authorization, to contribute to maintaining system integrity.

					<p>	•	Taking the lead in initiating documentation practices for infrastructure configurations and processes, contributing to a comprehensive knowledge base.
									</p>
				<!--	<p>PS: Working on Node JS, Mongo DB and Machine Learning.</p> -->
				</div>
			</div>
		</div>
		<br>
		<div class="row">
			<div class="col-md-6">
				<div class="card card-body h-100">
					<h5>Education</h5>
					<hr>
					<p>	•	DevOps Engineering  - Darey.io, Jul 2021 - Present
					<p>	•	Data Science with Python - Simplilearn/Skillup - 2023
					<p>	•	AWS Cloud Computing - Simplilearn/Skillup - 2023
					<p>	•	Cloud computing - Simplilearn/Skillup - 2023
					<p>	•	Bachelor of Technology - BTech - Federal University of Technology Minna - Jan 2009 - Feb 2013</p>

				</div>
			</div>

			<div class="col-md-6">
				<div class="card card-body h-100">
					<h5>Projects</h5>
				<hr>
				<p>PROJECTS
				<p>	•	DevOps Projects - GitHub-AndromedaIsComingg/Other-Projects: Projects > than 4       
				<p>		Jul 2023 - Present                                                                            
				<p>	•	Python projects - GitHub-AndromedaIsComingg/Python-Projects
           		<p>		Oct 2021 - Present </p>
				

				</div>
			</div>
		</div>
		<br>
	</div>


</body>
</html>
```


And in the `main.css` file, we will paste and save the following lines of code:


``` css
body{
	background-color:#F8F8F8!important;
}

#profile-wrapper{
	text-align: center;
}

#profile-pic{
	width:150px;
	height: 150px;
	border-radius: 50%;
	margin-left: auto;
  	margin-right: auto;
}

ul{
	padding: 0;
    list-style-type: none;
}


.social-links ul, li{
	list-style-type:none;
	display: inline-block;
}

.social{
	width:20px;
	height: 20px;
}
```


This Should produce an output like in the photos below


<img width="1273" alt="output 1" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/c29c7a27-8f6c-4121-b03d-727652c61f2f">

<img width="1263" alt="output 2" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/28691098-5fed-4f1a-9134-691ce13264e1">

<img width="1280" alt="output 3" src="https://github.com/AndromedaIsComingg/Python-Projects/assets/140917780/3d0dfa3b-eff8-4d6d-88a8-b98d28bf430d">




---------------------------------![Alt Text](https://cssbud.com/wp-content/uploads/2021/05/thanks-for-your-time.gif)---------------------------------------------
