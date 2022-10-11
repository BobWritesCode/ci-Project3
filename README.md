# Hotdog Empire Tycoon


![Multiple Device Demo](./readme-content/imgs/preview.png)

## Live Site

[Hotdog Empire Tycoon](
  https://dashboard.heroku.com/apps/hotdog-empire-tycoon/)

## Repository

[https://github.com/BobWritesCode/ci-Project3](
  https://github.com/BobWritesCode/ci-Project3)

---

## Table of Contents

- [Hotdog Empire Tycoon](#hotdog-empire-tycoon)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Table of Contents](#table-of-contents)
  - [Objective](#objective)
  - [Brief](#brief)
    - [Hotdoog Empire Tycoon](#hotdog-empire-tycoon-1)
  - [UX &#8722; User Experience Design](#ux--user-experience-design)
    - [User Requirements](#user-requirements)
      - [First Time User](#first-time-user)
      - [Returning User](#returning-user)
      - [Interested Party](#interested-party)
    - [Initial Concept](#initial-concept)
      - [Wireframes](#wireframes)
        - [Desktop](#desktop)
      - [Colour Scheme](#colour-scheme)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Logic](#logic)
    - [Initial Flow](#initial-flow)
    - [Python Logic](#python-logic)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [UX](#ux)
      - [Keywords](#keywords)
    - [Features Left to Implement](#features-left-to-implement)
  - [Data Model](#data-model)
  - [Technologies Used](#technologies-used)
    - [Python Packages](#python-packages)
    - [Other Tech](#other-tech)
      - [VSCode Extensions](#vscode-extensions)
  - [Testing](#testing)
    - [Python Testing](#python-testing)
      - [Manual Python Testing](#manual-python-testing)
        - [Manual Testing Documentation](#manual-testing-documentation)
      - [PEP8 Testing](#pep8-testing)
      - [Other Python Testing](#other-python-testing)
    - [W3C Validator](#w3c-validator)
  - [Bugs](#bugs)
    - [Current](#current)
    - [Resolved](#resolved)
  - [Development](#development)
    - [GitHub](#github)
    - [GitPod](#gitpod)
      - [Cloning](#cloning)
      - [Editing](#editing)
    - [Working With Python](#working-with-python)
      - [Packages](#packages)
      - [Debugging](#debugging)
    - [Google Sheets](#google-sheets)
      - [Creating Sheets](#creating-sheets)
      - [API Credentials](#api-credentials)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

---

## Objective

Design an interactive game that uses an existing API for to save user game data and a leader board.
The project should run in a CLI, deployed via Heroku, using Python.

***The needs within this project are not genuine and are made purely
for the purpose of completing this project.***

---

## Brief

### Hotdog Empire Tycoon

The goal of this site is to provide an interactive game where the user / player can compete for a place on the leader board. The final product should:

- be programmatically error free,
- be written using Python,
- have replayability,
- handle all user input errors gracefully and appropriately,
- give clear instructions regarding use and valid inputs.
---

## UX &#8722; User Experience Design

Some example user stories which will affect the design

#### First Time User

> *"As a person who like likes to play games, I would like something that provides some challenges but not overly difficult to learn."*
>
> *"As a competitive player, I would like to know how I compare with other users and go for top of a leader board."*
>
> *"As someone unfamiliar with tycoon game concept, I would like something that is to pick up and provides adequate direction."*

### Returning User

> *"As a returning user, I would like to see a list of current high-scores."*
>
> *"I would like to be able to continue a game where I left off."*
>
> *"I would the experience to be different each time I play."*

#### Interested Party

> *"As someone interested in how the application has been made, I am interested to see how user inputs have been validated and errors have been handled"*
>
>*"As someone interested in how the application wasm, I am interested to see any interesting code you made have used or created."*

---

### Initial Concept

I intend to make a game application inspired by a childhood memory of Lemonade stand. The version I played was a flash game but learnt from starting this project that it all started with the [original created by Bob Jamison](https://en.wikipedia.org/wiki/Lemonade_Stand).

I intend to:
- use an API to store user game data, which the user can also use to retrieve a previous game they have not completed yet.
- use an API to store a leader board, which users will be able to view.
- write error proof logic.
- a fun and interesting game.

I do not intend:
- to store any user sensitive information using the API.

#### Wireframes

Due to the nature of this project the wireframes are very basic. There is only
one page and the design does not change across any devices, only a change in
content.

##### Desktop

![Wireframe](./readme-content/imgs/wireframe.png)

---

#### Colour Scheme

I wanted to go for a vibrant eye-catching look. I also tried to keep to a colour theme as much as possible and not use too many colours.

- Cyan - Used mainly for headers.
- Pink - Used mainly for user tips.
- Orange - Used mainly for when user input was required.
- Red - Used mainly for errors and grabbing user attention.
- Yellow - Used mainly to highlight '0. Go Back' to the user
- Gold - Used mainly to highlight positive information to the user.
- Green - Used mainly for cash balance and some areas to help separate information from each other.

To create the different colour text in the game I used code found of [Grepper](https://www.codegrepper.com/code-examples/python/how+to+color+text+in+python+3).

```python
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
```

I then created specfic colour functions to have better readability, keep colours uniformed and make it quicker to add coloured text.

```python
def pink(text):
    '''
    Changes to PINK if printed to termail
    '''
    return colored(255, 105, 180, text)
```

---

#### Typography

I do not use any external font outside the terminal except for the button provided by Code Institute to 'RUN PROGRAM'

---

#### Imagery

There is no imagery used for this project.

---

## Logic

### Initial Flow

This chart shows what the user will expereience / see and is the concept of how the game will run

![Flowchat for frontend](./readme-content/imgs/flowchart-frontend.png)

---

### Python Logic

![Flowchat for backend](./readme-content/imgs/flowchart-backend.png)

---

## Features

### Existing Features

#### UX

---

#### Keywords

---

### Features Left to Implement

---

## Data Model

## Technologies Used

### Python Packages

---

### Other Tech

---

#### VSCode Extensions

---

## Testing

### Python Testing

#### Manual Python Testing

##### Manual Testing Documentation

#### PEP8 Testing

#### Other Python Testing
---

## Bugs

### Current

### Resolved
---

## Development

The site was made using [GitHub](#GitHub) and [GitPod](#GitPod)

### GitHub
---

### GitPod

#### Cloning

#### Editing

### Working With Python


#### Packages

#### Debugging

### Google Sheets

#### Creating Sheets

#### API Credentials

## Deployment

### Heroku

---

## Credits

### Content

### Media

### Acknowledgements

