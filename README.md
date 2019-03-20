# Codagram #

## Project ##

We are building a simple learning web app targeting the 7 to 11 years old.<br/>
Our goal is to introduce kids to code :computer: Who knows we might create vocation ... :heart:

Deployed on: https://examplecodagram.herokuapp.com/

## Screen shots ##

![homepage](https://user-images.githubusercontent.com/43742795/53587325-f5131800-3b81-11e9-9508-269966f49ddc.png)

![question](https://user-images.githubusercontent.com/43742795/53587371-13791380-3b82-11e9-8045-caef9524e4d0.png)

## User story ##

```
As a kid
So that I can create an account
I need to be able to sign up
```
```
As a kid
So I can access my account
I need to be able to sign in
```
```
As a kid
So I can leave my account
I need to be able to sign out
```
```
As a kid
So that I can learn a programming language
I need to be able to choose a language between multiple
```
```
As a kid
So that I can learn syntax
I want to be able to reply to a multiple choice question
```
```
As a kid
So that I can carry on learning
I want to be able to see a validation if my reply is the correct one
```
```
As a kid
So that I can correct myself
I want to be able to see an hint about the correct reply if I am wrong
```
```
As a kid
So that I can test that I understood the previous concept
I want to be able after I finished the 5 questions of a topic, to have a recap exercise with 5 questions that I can complete myself
```
```
As a kid
So that I can always learn new concepts
I want to be able after the recap exercise to move on to an other topic
```
```
As a kid
So I can continue my learning
I want to have access to my profile page and to choose with which language I want to continue
```
```
As a kid
So I can follow my learning
I want to be able to see how many percentage of the course I have completed
```
```
As a kid
So that I enjoy being on the website
I want something colourful and pretty to look at
```

## Our approach ##

This project is done in a team of 4 people.<br/>
We are using these high level skills :<br/>
1. [XP values](#xp-values) to guide your behaviour<br/>
2. The full [developer workflow](#development-workflow) (Creating issues, branching, reviewing, squirrelling, merging.<br/>
3. Keeping code quality using *Travis* <br/>
4. Agile processes (diagram, morning/afternoon stand up, 2 days sprint (planning days (scrum methodology) - retro days), strict TDD principle, code pairing)

## MVP ##

Our Minimum Viable Product is the following one:<br/>

1. Kid is able to go to a landing page where an introduction about coding and about Ruby are displayed (able to learn 1 language => Ruby)
2. On the landing page kid can click on a button to be redirected to the first exercise
3. Kid is redirected on the exercise page, where the explanation and the first multiple choice question is displayed
4. Kid can tick the box in front of the reply he thinks is the good one
5. If the reply is wrong kid sees a message giving him an hint to correct his reply
6. Kid can re-tick one of the reply, if still not correct step 5 happen again
7. If correct reply, kid see a congratulation message and a button to go to the next question is displayed

## Mock up ##

![codagram](https://user-images.githubusercontent.com/43742795/53085589-1f6a3300-34fb-11e9-939f-780e9b381b32.png)

## Bonus features ##

If we will have more time our goal would have been to :
- Add more languages/levels
- User authentication => User can have their ow profile page
- Score - progress made through the course
- Make features tests. As we have to face team member missing and we choose to put our main goal as learning with a dead line. We had to prioritise and we sadly miss time to test as it is tough using all those new tech stack.

## Tech Stack ##
- Python (version 3)
- Flask - web framework
- Html/ CSS - front-end/styling
- Github
- Postgresql - DB
- SqlAlchemy - ORM

## Code Quality ##

- Travis
- Flake8 - linter

## How to use ##

### Set Up ###

1. clone the repo<br/>
Under the repo name click *clone or download*<br/>
Click on *use HTTPs*, copy the clone URL of the repo<br/>
In the terminal go on the working directory where you want the cloned directory to be<br/>
Use the `git clone` command and paste the clone URL then press enter :

```shell
$ git clone https://github.com/your-username/your-repositary.git
```

2. On your local machine go inside of the *Codagram* directory :

```shell
$ cd Codagram
```
3. You can see the different files/ directories by using the `ls` command :<br/>

```shell
$ ls
```

4. You can open any files that you want to read and change the code in your text editor or using `vim` :

```shell
$ vim wanted_file.py
```
Or you can just read the contains of it from the command line with `cat` :

```shell
$ cat wanted_file.html
```
5. To install all the *requirements* contained in the *requirements.txt*, you have to run `pip install -r requirements.txt`:
Install :

```shell
$ pip install -r requirements.txt
```

6. To use Pyhton, you have to create a `virtual environment` from your root directory. If not already installed you have to install the *virtual environment package* by using the command `pip install virtualenv`

```shell
$ pip install virtualenv
```

7. Now create the virtual environment, by using the command `virtualenv python3`

```shell
$ virtualenv python3
```

8. To activate the virtual environment and be into it, you have to run the command `source python3/bin/activate`

```shell
$ source python3/bin/activate
```

9. If you wish to exit the virtual environment, use the command `deactivate`

```shell
$ deactivate
```

### Database ###

1. If you do not have it already, install *psql* on your local machine.

2. To create the database, from your command line, type `sudo -u createdb codagram`

3. Connect to psql and connect to your database using the `\c codagram;` command.<br/>
Once you are connected to the database you've chosen, you can list the tables using the `\dt` command.<br/>

```shell
$ psql
admin= \c codagram;
codagram= \dt
```

5. To apply the migration to the DB, type the following command `python manage.py db migrate` and then `python manage.py db upgrade`

```shell
$ python manage.py db migrate
$ python manage.py db upgrade
```

6. You can connect to a specific table by using the `SELECT * FROM tablename;` command.<br/>

```shell
codagram= SELECT * FROM tablename;
```

## Code quality ##

Check that the code respects the quality of the *Flake8* guideline, by running `flake8` from the *codagram* directory :

```shell
$ cd codagram
$ flake8
```

## Run the app ##

1. Copy and paste the following in your command line:

```shell
$ export APP_SETTINGS="config.DevelopmentConfig"
$ export DATABASE_URL="postgresql://localhost/codagram"
```

2. To run the app, from the command line type the following command `python manage.py runserver`:

```shell
$ python manage.py runserver
```

3. Open your browser and got to the *localhost:5000* <br/>
The page will be displayed on your browser.

4. Enjoy playing around with our app as much as you want :smile:


## Authors ##
- [Onkar Sahota](https://github.com/OSSahota)
- [Emanuele Gorga](https://github.com/emanuelegorga)
- [Gabriel Matos](https://github.com/GabMat97)
- [Celine Kaslin](https://github.com/CelineKaslin?tab=repositories) (myself)
