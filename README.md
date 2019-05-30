# Awwards

This project was generated with Python version 3.6.

### By Niklauspeter

##  Description
This is a django web appliction that mimics the awwards online website application. It allows a user to sign up and have their own awwards account and thereafter, can post projects they have made, active links to them and have them reviewed by other users. once logged tney can also review other users' projects .

## User Stories

The user is able to:
* enter the url to load the website
* sign up for an user account .
* view a grid of uploaded projects displayed in the root page
* search for a particular project its by title  
* upload and have their own projects displayed and reviewed


## Prerequisites
To develop the application , youll need to preinstall a few application. including
* Python 3.6
* Django
* pip
* postgress

## Technologies Used
* python 3.6
* Django 
* postgress

## Setup Information
* Clone the application repository to your local machine .
* Create a new virtual environment and access the folder through your virtual amchine.
* access the code through your preffered code editor
* create your database and link it in the config.py
* run this on your terminal python3.6 manage.py server
* Once run, the project can be accessed on your localhost using the address: localhost:8000.

## BDD
|Behavior |Input |Output |
|:------------| :---------|:--------|
| user loads url on browser | user loads url on web browser | user is redirected to a login page with an option to register for an account|
|user creates an account|user redirected to a sign up page where they create an account|user is able to view either a profile page or the home page|
|user finds projects posted by other users|user clicks on the search icon in the navbar |user searches other projects by title and is redirected to another page where they are able to view the project|
|user logs out |click on logout in navbar |user is logged out of the application|


## LICENSE
MIT License

Copyright (c) 2019 niklauspeter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact Information
For any enquiries email me at oriokiklaus@gmail.com or github username niklauspeter