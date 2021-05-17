# CRUD APP: Indoorclimbing Centres 

## Contents 

* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Project Tracking](#project-tracking)
  * [Trello Board](#trello-board)
* [Architecture](#architecture)
  * [Entity Relationship Diagram](#entity-relationship-diagram)
  * [Continuous Integration](#continuous-integration)
* [Risk Assessment](#risk-assessment)
* [Development](#development)
* [Testing & Analysis](#testing)
  * [Unit Testing](#unit-testing)
  * [Integration Testing](#integration-testing)
* [Front-End Design](#front-end)
* [Database](#database)
* [Footer](#footer)



## Introduction 

### Objective 
The overall objective with this project is the following:

**To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.**

The request was to specifically display the following within the project: 
The requirements of the project are as follows:

* **Functioning CRUD application created in Python.**
* **Functioning front-end to website using Flask.**
* **Trello board or equivalent.**
* **Relational database - must contain at least one one-to-many relationship.**
* **Clear documentation**
* **Detailed risk assessment.**
* **Automated tests.** 
* **Fully integrated into Github or other VCS.**

### Proposal 

My proposal was to develop an **An Indoor Climbing Centre** application that allowed users to input their personal information as well as the information of the centres the visited.  

An outline of how CRUD will be implemented can be seen below.

**Create**:
* Add the name and address of a climbing centre 
* Users can then sign up using a sign up button 


**Read**:
* Users are able to read centre information on the home page 
* Users are able to see other users and the centres they have signed up to


**Update**:
* Users can update thier personal information 
* Users can update the centres they are signed up too


**Delete**:
* user/profile

Additionally, I would like to allow users to: 
* List their experience Levels 
* Rate how difficult they find the climbing centre 
* To interact with other users on a forum
* Navigate to the website of centres to find out more information.


## Project Tracking 
 I used a Trello Board to track the progress of my project (Image below)

 [A link to my Trello Board](https://trello.com/b/mkSUq0gB/indoor-bouldering-centre-ratings)
 

### Trello Board 
![](https://i.gyazo.com/877738232080f6c6b7da538563bf1ce7.jpg)
 
## Architecture 

### My Current ERD Relationship Diagram 

The climbing Centre will either have no relationship with a climber or a relationship with multiple climbers. For simplicity reasons, a climber can only either have no relationship with a climbing centre or a relationship with one centre at a time. 
<p>

<img align="left" width="500" height="300" src="https://i.gyazo.com/6818060b71452c45c71f8e1082692010.png">

<p align="center">
  <img width="500" height="300" src="https://i.gyazo.com/46b01c78a2f55f8f646f1acb980969de.png"> </p>
 <br><br>

### Below is an example of some of the ideas I considered before settling for the above. 

This is an example of many to many relationship with multiple tables in the database schema. The Centre & Climber and Climber & Centre have the same relationships as above. The difference is that a climber can be in multiple groups and groups can have multiple climbers. 

<p align="center">
  <img width="450" height="250" src="https://i.gyazo.com/c9a1d3bc6a13f66fa21cda517b99d480.png"> </p>

<br><br>

### Continous Integration 

![Continous Integration Pipeline](https://i.gyazo.com/2251906d0381f3874102da31cf58ebd7.png)

Above is the Continuous integration used in my project. The focus is speed and efficiency from application, _including any future changes in code_, development-to-deployment. As code is pushed to my GitHub repository, Jenkins fetches and builds the code in my repository. Jenkins will then run any pre written unit and integration testing in a testing environment and with pre-installed plugins, Jenkins is then able to produce reports on how the application is performing.  

#### A build being automated following a git push 
![Build automation](https://i.gyazo.com/6c9f8d61ac93e880ba9bb6f66623381e.png)
 
#### An image of Jenkins tracking changes (commits) made in my GitHub repo 
![Repo Tracking by Jenkins](https://i.gyazo.com/c6f6a3dfd9b315b1f6bd536a7bffddc7.png)


## Risk Assessment 

I did some risk assessment before embarking on building the project and I discovered the following associated risks with building a web application: 

![Risk Assessment Image](https://i.gyazo.com/e5bd70eaa95414b528faed0d09821aaf.png)

[A link to my full Risk Assessment](https://drive.google.com/file/d/1olqQSJ7y09J8EA4TxXEmbGOleK4tgDaq/view?usp=sharing)
 

## Development 

I used Google Cloud Platform, **GCP**, To build my virtual machines and to host my application. 

I also used the same platform to build my SQL database, that will be used to store all data collected from users. 

The application was written using the python programming language on the Visual Studio Code and stored in GitHub.

There are a total of 9 branches with more than 15 commits in GitHub. 

I named each branch "run" as can be seen from the image below

![](https://i.gyazo.com/15c5996ad85ca80779c8fb9b660d7f6c.png)

When you look at "run1", it is 15 commits behind the current "run" (image below). 

![](https://i.gyazo.com/ce3a95c0a28007b5b784dc41511532b1.png)

Once completed, The backend end was tested using unit testing and The full functionality of the application was tested using Selenium. 

## Testing 

### Unit Testing 

I used pytest to run the unit tests on the app. These are designed to determine if a certain function is running as expected. Jenkins produces console outputs that will inform the developer how many tests the code passed and which tests failed. The images below show the type of outputs produced by Jenkins.

They are identical to what happens when the test are manually executed in a python terminal. 

![](https://i.gyazo.com/a51880748f52f76d226b479ff864234e.png)

In this image, the circled part shows the testing coverage. In simple terms, the proportion of the application that is being tested. 

Unit Testing = 76%
Integration Testing = 100%

Jenkins also shows you were the testing is failing ( pointed arrow )

![](https://i.gyazo.com/9cdbfc0bca877b509b0abbb42fd331aa.png)

From the image below, I have higlighted the areas not being tested in the Unit Testing

![](https://i.gyazo.com/6e7f37743af3ff5004f38068055f41e6.png)


This is the exact part of one of the areas not being tested

![](https://i.gyazo.com/93136a7c545096557ed86d2a090d1b95.png)

### Integration Testing 

In Integration testing I tested my software application as a whole, rather than mocking the application to it's routes as I did in unit testing.I used selenium to simulate a user navigating the site (by clicking on elements in each page) and filling in forms as the testing

The /create page that was not being tested in the Unit Testing was covered in the Integration Tests

In the image below, the code mimicks what a user will do. Firstly, it finds the /create page on the application.

It then enters the details inside and returns to the /home page. 

![](https://i.gyazo.com/29c7937acb4efe8812491693d6c16387.png)

#### Coverage Report 

Overall, this is the proportion of the application that have written test to determine it functionality. 

![Coverage Report](https://i.gyazo.com/eabe7d91e63ca411ce6f725478bf54b6.png)


## Front-End Design 

### Home Page (Crud Read Function)

The image below shows what the first ever user will see. The url: /home, will direct the user to this page.

![](https://i.gyazo.com/c288e570258abf5e8eab9b5b5d2f0dc7.png)



### Create Page (Crud Create Function)

Clicking on the **Add New** button will direct the user to this create page (/create).

The User will then able to add the name and address of a climbing centre they use. 

![](https://i.gyazo.com/8115081efe2097503eaf648623b922a9.png)

Once the user clicks on submit, the will be redirected to the home page (/home), where they will be able to access and read all the neccessary information. 

![](https://i.gyazo.com/884f41ebf540d18f5f14cd0f06bbc7ce.png)

### Sign-Up Page (Crud Update Function)

A climber will then be able to electronically sign-up to a centre by clicking the sign-up button.
The url, in this case (/signup/2), where the 2 is the direct ID of a climbing centre which I will show and explain more about later. 

![](https://i.gyazo.com/5c420bb033469ae770d87b7cedac3c4a.png)

After the climber enters their information, they will be redirected to the home page.

The climbers name will be displayed but for security reasons, their email will not. 

![](https://i.gyazo.com/ec628163b900a64ca51215abfe0fb18f.png)

### Delete Page (Crud Delete Funtion)

Clicking the delete button will return the user to the home page and any information that was deleted will be removed from the database and the home page of the application. 

![](https://i.gyazo.com/9f31e017591a3cb079ebe42287f1a35b.png)

## Database 

I decided to use mysql to store my data because it was more secure than a standalone database. 

Looking at the below image, you can see that the data input by the user is now securely stored in the relevant tables. 

The number 2, which was shown on the sign-up page can be seen under centre_ID

![](https://i.gyazo.com/1b09d98a0f29848ff8cb157a4c35821f.png)


We can see that delete function works because once the button is clicked, the information in the database is now deleted. 

![](https://i.gyazo.com/d2061198f0b6a5486f4455ea185fb40c.png)

## Security Measures 

Refer to Risk Assessment 

## Known Issues 
* The delete function currently only deletes information related to the Climbing Centre and leaves the Climber information. 

* 3/3 passed in the manual integration testing. 2/3 passed in Jenkins. 

## Future Improvements 

The majority of improvements are outlined in my Trello Board using the MoSCoW principles. The current version of the application includes only must haves.

 [A link to my Trello Board](https://trello.com/b/mkSUq0gB/indoor-bouldering-centre-ratings)

* Burndown Chart to better apportion work left to do vs time
* A more user friendly Interface 
* The application should have a forum that allows for interactions and social meetups  
* Include a ratings function for users. 
* Include a Gunicorn 
* 100% coverage report 

## Author 

Abs Pinnankoh-Morrison 

## Footer 
Special thanks to
 
Harry Volker 

Oliver Nichols 

Help Desk 