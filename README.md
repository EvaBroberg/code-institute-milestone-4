# milestone4

![alt text](static/img/readmelogo.jpg)

[![Build Status](https://travis-ci.org/EvaBroberg/code-institute-milestone-4.svg?branch=master)](https://travis-ci.org/EvaBroberg/code-institute-milestone-4)


[CHECK IT OUT](https://milestone-4-ugogirl.herokuapp.com/)

UgoGir is a female-only body building members site which purpouse is to affectivelly provide women with help they need on their journey to professional body building career. Site also serves as an ecommerse place to get equipted with anything one could need for training.

Exclaimer: this website has been built for educational purpouses and will not be used for an active business.

## UX
The design of the site seeks to be simplistic yet modern and appealing for an eye, yet easy to navigate and informative. Navigation is sticky and repeated on the footer so that user could easily navigate despite of the scroll location. Theme colours and elements such as buttons, dropdowns etc are repeated across the site.
User stories
As a guest user:
<ul>
<li> • I want to have access to information about different memberships.</li>
<li> • I want to be able to read the news.</li>
<li> • I want to be able to navigate easily on the site to contact information where I could enquire about training.
</li>
<li> • I want to access shop and be able to put items in the cart, I want these items to stay in the cart if I left the page without checking out.
</li>
</ul>
   
   
As a registered user:
<ul>
<li></li>
<li></li>
<li></li>
<li></li>
<li></li>
</ul>
    • I want all the functionality that guest user has +
    • I want to have access to my profile page and be able to update my information and profile picture.
    • I want to be able to comment under news posts.
    • I want to be able to buy items in the store and securely checkout.
    • I want to be able to upgrade and downgrade my subscription which will affect my monthly payments.
Admin:
    • I want to be able to write, edit and delete news posts.
    • I want to be able to approve or reject user’s comments under news posts.
Wireframes
    • Mobile
    • Desktop
          Technologies used
    • Photoshop 
    • HTML
    • CSS
    • JS
    • Python
    • Django
    • Postgres db
    • Materialize

          FEATURES
Existing:
To implement in the future:

## TESTING

## DEPLOYMENT
Hosted in Heroku and deployed to GitHub. Heroku will automatically update upon new github commits.
In order to deploy project locally:
    • Download code file from git repository by clicking ‘code’ button. Alternitavelly navigate to the location you would like to save the project and in your terminal/command-line enter: ‘git clone https://github.com/EvaBroberg/code-institute-milestone-4.git’
    • Using terminal/command-line set up virtual environment following these steps:
       1. pip install virtualenv
	2. virtualenv env
    • Activate your new virtual environment:
      1. env\Scripts\activate

    • Install project requirements:
      1.  pip install -r requirements.txt
      
    • Create a new file at the base directory level called env.py and add this code:
      
       import os
       
       os.environ.setdefault( 'DEVELOPMENT', 'True')
       os.environ.setdefault('SECRET_KEY', 'your_value')
       os.environ.setdefault('STRIPE_PUBLIC_KEY', 'your_value')
       os.environ.setdefault('STRIPE_SECRET_KEY', 'your_value')
       
    • Set up the databases by entering this line terminal:
       python manage.py migrate
    • Create a superuser in order to use django admin interface as well as to be able to perform admin-only actions on website:
       python manage.py createsuperuser
    • Start server
       python manage.py runserver
    • Follow URL outputted in terminal in order to view site.
Heroku deployment
    1. Login to Heroku and set up a new app with an unique name 
    2. On the Resources tab, in the Add-ons field type Heroku Postgres select the Hobby Dev then click the Provision button.
    3. After setting the Postgress database go back to the Settings tab and click Reveal Config Vars. Copy the values from your env.py file into Heroku. Make sure you load the following:
Key
Value
AWS_ACCESS_KEY_ID
<your_value>
AWS_SECRET_ACCESS_KEY
<your_value>
DATABASE_URL
<your_value>
SECRET_KEY
<your_value>
STRIPE_PUBLIC_KEY
<your_value>
STRIPE_SECRET_KEY
<your_value>
USE_AWS
<your_value>
       Grab the DATABASE_URL link from Heroku's Config Vars as we gonna need it later to migrate to the Heroku Postgres database.
    4. Now that the database on Heroku is created the following rule needs to be added to the env.py file
       os.environ.setdefault('DATABASE_URL', '<your postgres url grabbed from Heroku>')
       Be assured to not share this URL with anybody.
    5. Because this is a new database connection, the migrate command must be executed with the following command in your terminal:
       python manage.py migrate
       Do not forget to reactivate your virtual environment if the system or IDE is rebooted.
    6. Create the superuser for the postgres database so you can have access to the django admin.
       python manage.py createsuperuser
    7. Now we need to add the required data into the database in the following order:
       python manage.py loaddata groups.json
       python manage.py loaddata customers.json
       python manage.py loaddata itemtags.json
       python manage.py loaddata items.json
    8. With everything set push the code to a GitHub account of yourself:
       git init
       git commit -m 'getting ready to deploy to Heroku'
       git push -u origin
    9. From the Heroku dashboard of your newly created application, click on the "Deploy" tab, then scroll down to the "Deployment method" section and select GitHub.
    10. Use the GitHub link and type in the name of the repository and click the search button. Then connect the Heroku app to the desired GitHub repository.
    11. On the Deployment Tab, scroll a bit further down to the "Manual Deploy" section, select the master branch then click "Deploy Branch".
    12. Once your application is running, you may want to update the Deployment method from Manual to Automatic.
    13. From the Heroku dashboard select the Open app button on the top right. Add the following part to the end of the URL in the address bar (/admin/accounts/customer/1/change/) and login with the created superuser credentials. Connect the customer to an user (it is the first input field) Provide the company information for all the required fields and press the "SAVE" button on the bottom right.
    14. Go to the main admin page and click the Users option under the AUTHENTICATION AND AUTHORIZATION tab. Under the Permissions tab at Groups select the admin in the left box and push the arrow to switch it to the right box. Press SAVE on the bottom right corner of the page. The deployed project is now ready to be used.
    • 

