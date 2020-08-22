# milestone4

![alt text](static/img/readmelogo.jpg)

[![Build Status](https://travis-ci.org/EvaBroberg/code-institute-milestone-4.svg?branch=master)](https://travis-ci.org/EvaBroberg/code-institute-milestone-4)


[CHECK IT OUT](https://milestone-4-ugogirl.herokuapp.com/)

UgoGir is a female-only body building members site which purpouse is to affectivelly provide women with help they need on their journey to professional body building career. Site also serves as an ecommerse place to get equipted with anything one could need for training.

Exclaimer: this website has been built for educational purpouses and will not be used for an active business.

## UX
The design of the site seeks to be simplistic yet modern and appealing for an eye, yet easy to navigate and informative. Navigation is sticky and repeated on the footer so that user could easily navigate despite of the scroll location. Theme colours and elements such as buttons, dropdowns etc are repeated across the site.

## USER STORIES

As a guest user:
<ul>
    <li>I want to have access to information about different memberships.</li>
    <li>I want to be able to read the news.</li>
    <li>I want to be able to navigate easily on the site to contact information where I could enquire about training.
    </li>
    <li>I want to access shop and be able to put items in the cart, I want these items to stay in the cart if I left the page without checking out.
    </li>
</ul>
   
As a registered user:
<ul>
    <li>I want all the functionality that guest user has +
    </li>
    <li>I want to have access to my profile page and be able to update my information and profile picture.
    </li>
    <li>I want to be able to comment under news posts.
    </li>
    <li>I want to be able to buy items in the store and securely checkout.
    </li>
    <li>I want to be able to upgrade and downgrade my subscription which will affect my monthly payments.
    </li>
</ul>

As an admin:
<ul>
    <li>I want to be able to write, edit and delete news posts.</li>
    <li>I want to be able to approve or reject user’s comments under news posts.</li>
</ul>

## TECHNOLOGIES USED
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JS</li>
    <li>Python</li>
    <li>Django</li>
    <li>Postgres db</li>
    <li>Materialize</li>
</ul>
    

## FEATURES

<h2>Existing:</h2>

<h3>Login/Register/Logout</h3>

<ul>
    <li>Upon entering site User is able to view all pages and even place items to the cart, however in order to create a custom account or make a purchase they need to be registered.</li>
    <li>Login/Register buttons are placed in a usual place in the nav.</li>
    <li>After user registers they are prompted to login.</li>
    <li>Once user is logged in they are assigned to customer group and a personal account is generated<li>
    <li>If user is admin, profile isn't generated for them as this is a feature to be implemented in the future.</li>
    <li>In the menu user can now see options 'log out' and 'profile'</li>
    <li>Upon clicking 'log out' user is redirected back to home page and options login/register are available in the menu once more.</li>
</ul>

<h3>User Profile</h3>
<ul>
    <li>Upon entering profile page user's name and image placeholder is displayed on the left menu.</li>
    <li>Below they can access progress page, which at the moment is only a placeholder page which does not generate personal data of the user</li>
    <li>Progress page will prompt user to update their membership if they are currently on the free plan as this functionality is only available to paying customers</li>
    <li>Further down the menu there is coutches link which is a placeholder page which would display user's coutches that have been assigned to them.</li>
    <li>News link is taking user to the blog page</li>
    <li>Account page is a placeholder page that needs to be updated</li>
    <li>On the right user can update their info and image using form provided</li>
</ul>

<h2>To implement in the future:</h2>

<h3>Login/Register/Logout</h3>
<ul>
    <li>On login create a module that generates a admin profile which would have different functionality to user profile</li>
</ul>

<h3>User Profile</h3>
<ul>
    <li>Create admin user profile that would include all the basic profile page functionality as well as control panel where admin would be able to see their calendar, sheduled bookings, client progress/messages etc and send customized workout plans and data to specific user's accout which will then be displayed in that user's Progress page.</li>
    <li>Upon clicking 'Coutches' tab user is provised with names. profile pics and contact info of their couthes as well as a opportunity to message them on the chat</li>
    <li>Account page should show user's current membership and prompt them to update it if they like</li>
</ul>

## TESTING

## DEPLOYMENT
Hosted in Heroku and deployed to GitHub. Heroku will automatically update upon new github commits.
In order to deploy project locally:
<ul>
    <li>Download code file from git repository by clicking ‘code’ button. Alternitavelly navigate to the location you would like to save the project and in your terminal/command-line enter: ‘git clone https://github.com/EvaBroberg/code-institute-milestone-4.git’
    </li>
    <li>Using terminal/command-line set up virtual environment following these steps:
        <ol>
        <li>pip install virtualenv</li>
        <li>virtualenv env</li>
        </ol>
    </li>
    <li>Activate your new virtual environment:
        <ol>
            <li>env\Scripts\activate</li>
        </ol>
    </li>
    <li>Install project requirements:
        <ol>
            <li>pip install -r requirements.txt</li>
        </ol>
    </li>
    <li>Create a new file at the base directory level called env.py and add this code:
        <ol>
            <li>import os</li>
        </ol>
    </li>
    <li>Set up the databases by entering this line terminal:
       python manage.py migrate
    </li>
    <li>Create a superuser in order to use django admin interface as well as to be able to perform admin-only actions on website:
       python manage.py createsuperuser
    </li>
    <li>Start server
        <ol>
            <li>python manage.py runserver</li>
        </ol>
    </li>
    <li>Follow URL outputted in terminal in order to view site.
        Heroku deployment
        <ol>
            <li>Login to Heroku and set up a new app.</li>
            <li>On the Resources tab, in the Add-ons field type Heroku Postgres select the Hobby Dev then click the Provision button.</li>
            <li>After setting the Postgress database go back to the Settings tab and click Reveal Config Vars. Copy the values from your env.py file into Heroku.</li>
            <li>Add os.environ.setdefault('DATABASE_URL', '<your postgres url grabbed from Heroku>') to the env.py file.</li>
            <li>Create the superuser python manage.py createsuperuser</li>
            <li>Add the required data into the database.</li>
            <li>Push the code to a GitHub.</li>
            <li>Click 'Deploy' , then scroll down to the 'Deployment method' section and select GitHub.</li>
            <li>Connect the Heroku app to the desired GitHub repository.</li>
            <li>On 'Manual Deploy' section, select the master branch then click 'Deploy Branch'.</li>
        </ol>
    </li>
</ul>




