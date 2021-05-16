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
<p align="center">
  <img width="460" height="300" src="https://i.gyazo.com/877738232080f6c6b7da538563bf1ce7.jpg"> </p> 
 
## Architecture 

### My Current ERD Relationship Diagram 

The climbing Centre will either have no relationship with a climber or a relationship with multiple climbers. For simplicity reasons, a climber can only either have no relationship with a climbing centre or a relationship with one centre at a time. 
<p>

<img align="left" width="350" height="200" src="https://i.gyazo.com/6818060b71452c45c71f8e1082692010.png">

<p align="center">
  <img width="350" height="200" src="https://i.gyazo.com/46b01c78a2f55f8f646f1acb980969de.png"> </p>
 <br><br>

### Below is an example of some of the ideas I considered before settling for the above. 

This is an example of many to many relationship with multiple tables in the database schema. The Centre & Climber and Climber & Centre have the same relationships as above. The difference is that a climber can be in multiple groups and groups can have multiple climbers. 

<p align="center">
  <img width="450" height="250" src="https://i.gyazo.com/c9a1d3bc6a13f66fa21cda517b99d480.png"> </p>

<br><br>

### Continous Integration 

![Continous Integration Pipeline](https://i.gyazo.com/2251906d0381f3874102da31cf58ebd7.png)

Above is the Continuous integration used in my project. The focus is speed and efficiency from application, _including any future changes in code_, development-to-deployment. As code is pushed to my GitHub repository, Jenkins fetches and builds the code in my repository. Jenkins will then run any pre written unit and integration testing in a testing environment and with pre-installed plugins, Jenkins is then able to produce reports on how the application is performing.  
 
#### An image of Jenkins tracking changes (commits) made in my GitHub repo 
![Repo Tracking by Jenkins](https://i.gyazo.com/c6f6a3dfd9b315b1f6bd536a7bffddc7.png)


## Risk Assessment 

I did some risk assessment before embarking on building the project and I discovered the following associated risks with building a web application: 

![Risk Assessment Image](https://i.gyazo.com/e5bd70eaa95414b528faed0d09821aaf.png)

[A link to my full Risk Assessment](hhttps://docs.google.com/spreadsheets/d/1olqQSJ7y09J8EA4TxXEmbGOleK4tgDaq/edit?usp=drive_web&ouid=115195321729310544192&rtpof=true)
 



## Development 

I used Google Cloud Platform, **GCP**, To build my virtual machines and to host my application. 

I also used the same platform to build my SQL database, that will be used to store all data collected from users. 

The application was written using the python programming language on the Visual Studio Code.

Once completed, The backend end was tested using unit testing and The full functionality of the application was testing using Selenium. 




## Testing 

### Unit Testing 


#### Coverage Report 

![Coverage Report](https://i.gyazo.com/eabe7d91e63ca411ce6f725478bf54b6.png)


### Integrating Testing 

In Integration testing I tested my software application as a whole, rather than mocking the application to it's routes as I did in unit testing.

![](https://i.gyazo.com/6e7f37743af3ff5004f38068055f41e6.png)

##### This is an example of the line that was not being tested. Lines 17 to 20. 

![](https://i.gyazo.com/886de20a22e15520a41fa902f005c432.png)

##### However a full integration testing, with 100% coverage showed that the application is working. 
![](https://i.gyazo.com/29c7937acb4efe8812491693d6c16387.png)


## Known Issues 

## Future Improvements 

## Footer 
