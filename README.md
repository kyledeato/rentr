# Rentr
> A full CRUD online rental marketplace allowing users to rent out their belongings to other people.
<!-- > Live demo [_here_](https://www.example.com). If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies and Frameworks Used](#technologies-and-frameworks-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- A centralized marketplace for renting or renting out anything from users.
- Intends to take out the problem of not knowing where to post your ad like Facebook, Craigslist, etc., and just have one place specifically for it.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies and Frameworks Used
- Python3 - version 3.10.2
- MySQL - version 8.0.22
- Jinja2
- BCrypt
- OS


## Features
- Ability to create an account to post a rent.
- Logged in users has full CRUD (create, read, update, delete) ability to their post(s).
- Logged in users has image upload to show what they are renting out.
- Non registered users can see the rent-board and message the user through email to rent.


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
Have Python installed and to set up local environment.
Windows:
```
pip install pipenv
```
Mac:
```
pip3 install pipenv
```
Active virtual environment.
```
pipenv shell
```
While virtual environment is running, use this to start the application.
```
python server.py
```
## Usage
Create a new account or use
email: kyledeato@gmail.com
password: password

NOTE: users have to type a image name in order for the picture to have a unique id. To get pass this, just type random letters or numbers.


## Project Status
Project is: _in progress_


## Room for Improvement

Room for improvement:
- Users not having to input a image name (id).
- Make most recent post to the top of the rent-board.
- A better User Interface.

To do:
- Css, css, css, and maybe uhhh more css?
- Make image upload better.


## Acknowledgements
-Featured on Coding Dojo's learning platform.


## Contact
Created by Kyle Deato.
Email: kyledeato@gmail.com
(and no, my actual password is not password...don't even try)


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
