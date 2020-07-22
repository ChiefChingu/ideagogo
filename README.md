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

![](https://github.com/ChiefChingu/ideagogo/blob/master/Structure%20plane.jpg?raw=true)

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

### User Stories
There are three different roles (site owner, idea owner and idea viewer). For each role the user stories are as follows:

#### As a site owner I want to be able to
1. Deal with upload of unwanted content.
2. Manage the idea category names.
3. Manage the idea tag names.

#### As an idea owner I want to be able to
4. Post my idea.
5. Upload a picture.
6. Change my uploaded picture.
7. Review my post.
8. Edit my post.
9. Delete my post.
10. Invite my friends to view and vote for my idea.

#### As an idea viewer (and idea owner) I want to be able to

11. Find interesting ideas.
12. Vote on ideas that interest me.
13. See that my vote was successful.
14. Remove my vote.
15. See that my vote was removed succesfully.
16. Share ideas to friends.
17. Send a message to the site owner.
18. View information about the site.

## Features
### Existing features
#### Site wide
- Clickable logo leading to the homepage.
- Hamburger menu that opens a modal for navigation.
- For larger viewports: navigation is shown in the header.
- Navigation linking to all pages.
- In case of a logged in user: the modal shows the logged in user name and a link to log out.
- In case of a logged in admin: the modal shows a link to the admin page.

#### Pages for logged in and logged out users
##### Home page
- Hero box that explains the purpose of the site.
- Secundary explanation to explain what you -the visitor- can do.
- Call to action: stimulate the user to take action. In this case cast a vote.

##### Ideas overview page
- Hero box that displays the top voted idea.
- A call to action bar to add your own idea. The button leads to the add idea page. Defensive design: in case user is not logged in an account needed page is rendered (see account needed).
- A search bar to quickly search for ideas. You can search by category name or by tag name.
- Idea cards: the ideas represented by cards. Each card has a 'front-side' and 'back-side'.
    - 'front-side': the card as rendered. This displays an image, title, number of votes and number of page views.
    - 'back-side': on click a panel slides up with more information. This shows the title, a short summary, the category name, three tags and a button to view the details of the project.
    - The category and tags are clickable and start a search query for categories and tags respectively (see [Search results](#search-results-page)).

##### Idea details page
- A 'bread crumb' to show where you are. Clickable to get back to the idea overview.
- Title of the idea.
- Hero image of the idea.
- Number of votes for idea.
- Number of page views of idea.
- Call to action button: like the idea. More details see voting. Defensive design: in case user is not logged in an account needed page is rendered (see [Account needed](#account-needed-page)).
- Social sharing bar: share the idea with your friends.
- Idea details to explain the idea.
- Label to indicate the category. On click all ideas within this category are displayed on a new page (see [Search results](#search-results-page)).
- Tags to describe characteristics of the idea.  On click all ideas with this tag are displayed on a new page (see [Search results](#search-results-page)).
- Date added.
- Idea owner.

##### Search results page
Search by category or tag leads to a search result page.
- A 'bread crumb' to show where you are. Clickable to get back to the idea overview.
- Title with number of search results.
- Subtitle to show what the search query is. It differentiates between category and tags.
- Idea cards: same cards as in [Ideas overview](#ideas-overview-page).

##### About page
- Title.
- Explanation.
- Call to action to feel free to send any inquiry.
- Call to action button to go to contact page.

##### Contact page
- Title.
- Call to action to feel free to send any inquiry.
- Contact form.
- Send button.

##### Account needed page
When a user is not logged in certain interactions are not possible. Defensive design: user is directed to this page.
- Title.
- Explanation why you need an account.
- Call to action button to create an account.
- Secundary call to action to check if user alreay has an account with link to login page.

##### Create account page
- Signup form.
- Signup button.
- Secundary call to action to check if user alreay has an account with link to login page.

##### Log in page
- Log in form.
- Log in button.
- Secundary call to action to check if user has an account with link to create account page.

#### Pages and features only for logged in users
##### Contact
- Username and email address are prefilled.

##### Add idea page
- Text fields for title, summary and details.
- File picker for picture upload.
- Drop down selectors for category and tags.
- Not visible to user, but also added to database: date of creation, username of creator, number of votes and number of views (both with zero as starting value).

##### Voting feature
- If idea is liked: a notification appears at the top of the page to tell that the vote was successful.
- If idea is liked: the button changes to remove vote.
- If vote is removed: a notification appears at the top of the page to tell that the vote was removed successfully.
- If vote is removed: button changes to initial state.

#### Features only for logged in users viewing their own idea pages
##### Idea details page - features
- Edit idea button leading to edit idea page.
- Edit picture button opening the edit picture modal.
- Delete button leading to delete idea modal.

##### Edit picture modal
- File picker to upload picture.
- Save button.
- Cancel button to return to idea detail page.

##### Edit idea page
- All fields are pre-filled with information from database and are editable.
- Update idea button to save changes.
- Cancel button to return to idea detail page.

##### Delete idea modal
- Warning that deletion is permanent.
- Delete idea button.
- Cancel button to return to idea detail page.

#### Pages and features only for admins
##### Admin features
- Admin can edit all ideas.
- Admin can edit all pictures.
- Admin can delete all ideas.

##### Admin functionalities page
- Title.
- Overview of category names.
- Per category name: delete button and edit category button.
- Add category button.
- Overview of tag names.
- Per tag name: delete button and edit tag button.
- Add tag button.

##### Add category page
- Title.
- Overview of all categories in label style.
- Input field for new category.
- Add category button.
- Back to admin link.

##### Edit category page
- Title.
- Prefilled category name in input field.
- Save changes button.
- Cancel button.

##### Add tag page
- Title.
- Overview of all tags in label style.
- Input field for new tag.
- Add tag button.
- Back to admin link.

##### Edit tag page
- Title.
- Prefilled tag name in input field.
- Save changes button.
- Cancel button.

### Features left to implement
#### Ideas
- Allow unlimited tags (currently three tags allowed), all displayed in a grid.
- Allow user generated tags and categories.
- Mark down for idea details.
- Comments and reactions on ideas.
- Free text search: search on title, tag, category and idea details.

#### User accounts
- Double opt-in at account creation.
- Reset password.
- Account overview page: display ideas, votes, comments.
- Editable profile: edit username, email and password.

## Data structure
The project brief was very explicit about the use of MongoDB, a non SQL database. This does not mean though that one should not think about the database structure carefully.

### Database Overview
The data was initially organised in seven collections. Two were automatically generated by using file upload in MongoDB (fs.chunks and fs.files). One was eventually dropped (Votes), but kept in here to show the thinking process while designing a voting system.

The collections are visually displayed as follows: ![](https://github.com/ChiefChingu/ideagogo/blob/master/ideagogodb.jpg?raw=true).

For each collection the fields are displayed below. The default id field is omitted in this overview. 

#### Users
- username: linked with ideas collection (field: username).
- email
- password: hashed password.
- voted_ideas: array of idea ids (To keep track of ideas in future account page and for alternative mechanism to enforce one vote per user on same project).

#### Ideas
- idea_title
- idea_summary
- idea_details
- category_name: linked with categories collection (field: category_name).
- idea_tag1: linked with tags collection (field: tag_name).
- idea_tag2: linked with tags collection (field: tag_name).
- idea_tag3: linked with tags collection (field: tag_name).
- image_name: linked with fs.files collection (field: filename).
- total_votes
- views
- user_votes: array of usernames that have voted on this particular project.
- date_added
- username: linked with users collection (field: username).

#### Categories
- category_name: linked with ideas collection (field: category_name).

#### Tags
- tag_name: linked with tags collection (fields: idea_tag1, idea_tag2, idea_tag3).

#### fs.chunks
Auto generated. Contains the data for all files that reside in fs.files.

#### fs.files
- filename: linked with ideas collection (field: image_name).
- contentType
- md5
- chunkSize
- length
- uploadDate

#### Votes
Removed. Initially created to design the logic for a one vote per user per project. For this I embarked on the thought train of setting the vote ID to the idea title and add user names that have voted in an array. If a user wants to vote, this collection is checked first to see if that user already exists. If so, no vote is possible.

In the end this proved to be too complex at the front end: using jinja if statements I wanted to display or hide the vote button, but ran into too many problems. See commit [04b75f1e290593f460efd8893e12c2a2f8cb5ca2](https://github.com/ChiefChingu/ideagogo/commit/04b75f1e290593f460efd8893e12c2a2f8cb5ca2) and following commits.

## Technologies Used
### Languages
- HTML
    - to create the elements
    - [https://whatwg.org](https://whatwg.org)
- CSS
    - to style the html elements
    - [https://www.w3.org/Style/CSS/](https://www.w3.org/Style/CSS/)
- JavaScript
    - to provide interactivity and logic
    - [https://developer.mozilla.org/en-US/docs/Web/JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- Python
    - for backend application
    - for all packages, see [requirements.txt](https://github.com/ChiefChingu/ideagogo/blob/master/requirements.txt)
    - [https://www.python.org](https://www.python.org)
- Jinja
    - for templating logic
    - [https://jinja.palletsprojects.com/en/2.11.x/](https://jinja.palletsprojects.com/en/2.11.x/)


### Libraries
- Flask
    - micro web server framework
    - [https://flask.palletsprojects.com/en/1.1.x/](https://flask.palletsprojects.com/en/1.1.x/)
- PyMongo
    - enable CRUD operations in MOngoDB
    - [https://flask-pymongo.readthedocs.io/en/latest/](https://flask-pymongo.readthedocs.io/en/latest/)
- JQuery
    - only for the shuffle cards function (see [Credits](#credits))
    - [https://jquery.com](https://jquery.com)
- Google Fonts
    - to use Lato fonts
    - [https://fonts.google.com/specimen/Lato](https://fonts.google.com/specimen/Lato)
- Font Awesome
    - to use icons
    - [https://fontawesome.com](https://fontawesome.com)
- EmailJS
    - to send contact form
    - [https://www.emailjs.com](https://www.emailjs.com)
- Materialize
    - to quickly add styling and interactivity
    - [https://materializecss.com](https://materializecss.com)

### Other tools
- MongoDB
    - the database used in this project
    - [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
- SCSS
    - to write custom CSS, especially for grids
    - [https://sass-lang.com](https://sass-lang.com)
- npm
    - to install SCSS
    - [https://www.npmjs.com](https://www.npmjs.com)
- Color blind filter
    - to check the used color palette
    - [https://www.toptal.com/designers/colorfilter](https://www.toptal.com/designers/colorfilter)
- GT Metrix
    - to check the loading times
    - [https://gtmetrix.com](https://gtmetrix.com)
- JSHint
    - to check JavaScript
    - [https://jshint.com](https://jshint.com)
- Markup Validation Service
    - to check HTML
    - [https://validator.w3.org](https://validator.w3.org)
- CSS Validation Service
    - to check CSS
    - [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
- Autoprefixer CSS online
    - to add vendor prefixes
    - [https://autoprefixer.github.io](https://autoprefixer.github.io)

## Testing
All standard online tests passed without any major problems.

The online and manual tests are detailed in the [TEST.md](https://github.com/ChiefChingu/ideagogo/blob/master/TEST.md).