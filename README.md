[Introduction](#introduction)

[UX](#ux)

[Features](#features)

[Data structure](#data-structure)

[Technologies used](#technologies-used)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)

[Future updates of coding structure](#future-updates-of-coding-structure)

## Introduction
This is the third milestone project of the fullstack software development course of Code Institute. I choose to create a 'light' Indiegogo clone: users can upload ideas. Other users can 'back' the idea by casting a vote on the project. The most popular project will be highlighted at the top of the page.

The project uses the required base functionality of CRUD: users can create, read, update and delete their projects. As a bonus a voting system is implemented, which requires user authentication.

To keep the project within a manageable scope you can only upload projects within the energy and green tech section. The live project can be found here: [https://ideagogo.herokuapp.com](https://ideagogo.herokuapp.com).

## UX
All designs start from the mobile perspective. Larger viewports are handled with media queries.

### Strategy Plane
#### Product objectives
As a site owner my objective is: show my skills and qualifications in order to pass the third milestone project.
I added one more objective to this: I want to get a score of at least 80% in order to receive 'first grade honors' at the end of the complete course.

#### User needs
There are two types of users in addition to the site owner role. A user who has an idea and a user who is curious and wants to view other persons' ideas. 
- A user who has an idea can post this idea. This user type is the idea owner. 
- A user who wants to see ideas can view all ideas that are posted. This user type is the idea viewer.
- An idea owner is an idea viewer by default (they always view their own idea).
- An idea viewer can become an idea owner when he or she posts an idea.

##### User needs idea owner
- Easy and intuitive way to post an idea.
- Make the idea 'findable': add categorization and/or labels.
- Let the world know about the idea: social sharing options.

##### User needs idea viewer
- Easy and intuitive way to browse ideas.
- Pick favorites: vote on ideas that are interesting.

##### User needs site owner
- Authority to edit and delete all ideas of all users.
- Manage (CRUD) categories and tags.

### Scope Plane
When designing this project a lot of ideas came up. Keeping the main objective in mind (pass the third milestone project) I decided to have these basic features (Full details on features: [Features](#features).)

#### Basic Features
- idea cards: quickly glance over an idea. Click to show more details on the card.
- CRUD on ideas: create, read, update and delete for site owner and idea owner.
- categorization: add a category to which your idea belongs.
- specification: add 3 tags to specify what your idea is about.

#### Advanced Features
Advanced features for a high grade are:
- vote on ideas.
- account creation.
- idea authorisation: only idea owners and site owner can perform edit and delete actions.
- limit the votes: a user cannot vote multiple times on the same project.
- make all labels clickable and initiate a search query.
- store images in MongoDB.
- manage ideas, categories and tags via a custom made backend.

### Structure Plane
The structure of the site is straightforward: a homepage connects to the idea overview page, an about page, a contact page, a registration page and a login page.

The idea overview page connects to all idea detail pages. From each idea detail page you can access the edit idea page (if you are the idea owner). Only visible to the site owner: an admin page where the categories and tags are managed (CRUD).

There is one special page: the account required page. This page is triggered when a user wants to perform an action while not logged in (vote, add idea).

[structure-plane](https://github.com/ChiefChingu/ideagogo/blob/master/Structure%20plane.jpg)

### Skeleton Plane
This project is designed with the mobile user in mind: mobile first and desktop second. The mobile viewport is the baseline. Media queries are used to handle the larger  viewports.

The wireframes are found [here](https://github.com/ChiefChingu/ideagogo/blob/master/Ideagogo%20-%20wireframes.pdf).

### Surface Plane
The final product can be viewed [here](https://ideagogo.herokuapp.com).

#### Typography
For this project the Google font Roboto is used. Roboto is an open source, sans-serif font originally developed by Google for Android. Its a modern, crisp typeface which fits perfectly in this project.

#### Color palette
The background color is white: easy on the eye, provides a clean and clear background. This makes it possible to add accents with these contrasting colors:

- Blue for background of hero and mobile menu (#e0f0fa).
- Pink for contrast (#e84d74).

The contrasting colors are checked in a [color blind web page filter](https://www.toptal.com/designers/colorfilter) with good results on all filters.
