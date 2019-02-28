# Codagram #

## Project ##

We are building a simple learning web app targeting the 7 to 11 years old.<br/>
Our goal is to introduce kids to code :computer: Who knows we might create vocation ... :heart:

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

## bonus features ##

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

## Authors ##
- [Onkar Sahota](https://github.com/OSSahota)
- [Emanuele Gorga](https://github.com/emanuelegorga)
- [Gabriel Matos](https://github.com/GabMat97)
- [Celine Kaslin](https://github.com/CelineKaslin?tab=repositories) (myself)
