# Test document

Back to the [README](https://github.com/ChiefChingu/ideagogo/blob/master/README.md).

First I tested the project with the validators for css and markup. Then I manually tested all user stories and features (if relevant). All results are displayed below. The last section goes into more detail about the issues I encountered.

## W3C CSS Validation Service
Directly inputting the project URL into the validators causes errors that are bugged. For instance:
```
Value Error : margin Unknown dimension 1rem
```
Of course this is not right. The validator gives around 300 of such errors. To overcome this I have copied the CSS from my custom stylesheet. And ran this in the validator tool. The result is perfectly fine code.

Note that I did not bother to check the materialize CSS.

## W3C Markup Validation Service
Many errors resulting from customizing materializecss components. After fixing these, no errors or warnings were shown.

### JSHint
#### email.js
- Undefined variable: ```emailjs``` (lines 3 and 22). This is out of my control, I use the EmailJS code as per instruction. 
- Unexpected use of '|' (line 21). Again out of my control, I use the EmailJS code as per instruction.

### app.js
- One warning: Do not use 'new' for side effects (line 19). Solved this by storing it in a var mobile.
- Warning is gone, but now there is a mention of an unused variable...

## User stories
Each user story is tested thoroughly. All steps are taken in the main browsers at 3 different viewports: mobile (including tablet) and desktop.

### Site owner
#### 1. Deal with upload of unwanted content.
In case of an idea that has unwanted content(offensive, copyrighted, etc.):
- Go to the log in page (mobile menu > login or desktop menu > login)
- Click on the idea card.
- View the title, summary, category and tags. If unwanted: click on the 'view details' button.
- View the idea details. Decide to either edit the idea and correct the unwanted parts or to delete the idea completely.

#### 2. Manage the idea category names
- Go to the log in page (mobile menu > login or desktop menu > login).
- Go to the admin page (mobile menu > admin or desktop menu > admin).
- View all category names in table style.
- Add:
  - click add category.
  - view all categories in label style.
  - type category name.
  - click add category.
  - see added category appear in all categories.
  - new category is added at end of this list.
  - see active cursor ready to add another category.
  - click back to admin to end adding category.
  - view all category names in table style.
  - view the newly added categories: they are listed alphabetically. 
- Edit:
  - click edit category at the category name you want to edit.
  - view the category prefilled in the input field.
  - rename/change the category.
  - save changes.
  - return to the admin page.
  - view the edited category: listed alphabetically in the table style overview.
- Delete:
  - click delete category at the category name you want to edit.
  - see the page refresh and the respective category disappear. 

#### 3. Manage the idea tag names
- Go to the log in page (mobile menu > login or desktop menu > login).
- Go to the admin page (mobile menu > admin or desktop menu > admin).
- View all tag names in table style.
- Add:
  - click add tag.
  - view all tags in label style.
  - type tag name.
  - click add tag.
  - see added tag appear in all tags.
  - new tag is added at end of this list.
  - see active cursor ready to add another tag.
  - click back to admin to end adding tag.
  - view all tag names in table style.
  - view the newly added tags: they are listed alphabetically. 
- Edit:
  - click edit tag at the tag name you want to edit.
  - view the tag prefilled in the input field.
  - rename/change the tag.
  - save changes.
  - return to the admin page.
  - view the edited tag: listed alphabetically in the table style overview.
- Delete:
  - click delete tag at the tag name you want to edit.
  - see the page refresh and the respective tag disappear. 

### Idea owner
#### 4. Post my idea
- Go to the log in page (mobile menu > login or desktop menu > login).
- If no account: go to register and create an account.
- Log in.
- Go to the idea page.
- Click on the add idea button.
- View the add idea page.
- All fields are mandatory to fill in.
- Complete all fields.
- Upload a picture: click the 'Choose file' button.
- Select a file from your device.
- Click add idea to finish.
- Your newly added idea is loaded.
- View the notification that the new idea is added.

#### 5. Upload a picture
Upload of a picture is included in the post idea user story above.

#### 6. Change my uploaded picture
- Go to the log in page (mobile menu > login or desktop menu > login).
- Go to the idea page.
- Go to your idea.
- Click the edit picture button.
- View a modal activate.
- Click the 'Choose file' button.
- Select a file from your device.
- Click the save new picture button.
- Return to the idea details.
- See your new picture.

#### 7. Review my post
- After finishing 'add idea', your newly added idea is shown.
- Review your idea immediately, without extra clicks/navigation.
- See issues and solutions for details about this functionality.

#### 8. Edit my post
- Go to your idea.
- If logged in: see the edit idea button.
- If not logged in: you cannot see the edit idea button. Log in first via the log in page (mobile menu > login or desktop menu > login).
- Click the edit idea button.
- The idea loads in edit mode with all values pre-filled.
- Change one of the fields.
- Click update idea.
- See notification appear that idea is updated.
- Review your change.

#### 9. Delete my post
- Go to the idea you want to delete.
- If logged in: see the delete idea button.
- If not logged in: you cannot see the delete idea button. Log in first via the log in page (mobile menu > login or desktop menu > login).
- Click delete.
- A confirmation window opens.
- Click cancel to return to your idea.
- Click delete to permanently delete your idea.
- After delete: view the notification that the deletion was successful.
- You return to the idea overview page.

#### 10. Invite my friends to view and vote for my idea
- Go to the idea you like to share.
- View the social sharing icons.
- Click an icon to share.
- Modal opens with the selected social network.

### Idea viewer, Idea owner
#### 11. Find interesting ideas.
There are several ways to find ideas.
1. Browse randomly:
  - go to ideas.
  - scroll through ideas and click the ones you find interesting.
  
2. Search by category:
  - go to ideas.
  - locate the search by category drop down menu.
  - click the drop down menu.
  - view a list of category names open.
  - click a category name.
  - see a result page with the number of search results in the title.
  - see the name of the searched category.
  - scroll through the search result.
  
3. Search by tag:
  - go to ideas.
  - locate the search by tag drop down menu.
  - click the drop down menu.
  - view a list of tag names open.
  - click a tag name.
  - see a result page with the number of search results in the title.
  - see the name of the searched tag.
  - scroll through the search result.

4. Click on any category label:
  - on all idea cards a category is specified.
  - this category label is clickable.
  - click on a category label.
  - see a result page with the number of search results in the title.
  - see the name of the searched category.
  - scroll through the search result.
  
5. Click on any tag:
  - on all idea cards a tag is specified.
  - this tag is clickable.
  - click on a tag.
  - see a result page with the number of search results in the title.
  - see the name of the searched tag.
  - scroll through the search result.

#### 12. Vote on ideas that interest me.
- Find an idea that you want to vote on.
- Click the 'like this idea!' button.
- If you are not logged in you will see a page 'account needed'.
    - If no account, click 'create an account'.
    - If you have an account click 'please log in here'.
    - Click the 'like this idea' button.
    - If no account: go to register and create an account.
    - Log in.
    - Find the idea you want to vote on.
    - Click the 'like this idea!' button.

#### 13. See that my vote was successful.
- View the notification at the top of the page that your vote was successful: 'Thanks for voting!'.
- View the counter of the votes go up.

#### 14. Remove my vote.
- Go to the idea on which you voted.
- Click on the button 'remove my vote'.

#### 15. See that my vote was removed succesfully.
- View the notification at the top of the page that your vote was removed: 'Vote is removed!'.
- View the counter of the votes go down.

#### 16. Share ideas to friends.
- Go to the idea you like to share.
- View the social sharing icons.
- Click an icon to share.
- Modal opens with the selected social network.

#### 17. Send a message to the site owner
- Go to contact.
- If logged in: username and email are pre-filled.
- If not logged in: enter username and email.
- Write message.
- Click 'send'.
- View send confirmation message: 'Thanks for contacting!'.

#### 18. View information about the site
- Go to about.
- Read the information.

## Features
Most of the features are covered by the test of user stories. Remaining features are tested individually and work as intended.

## Known error(s)
In Vivaldi on a real mobile device (Galaxy S10) the date added and submitted by are glitched. [See this screenshot](https://github.com/ChiefChingu/ideagogo/blob/master/Screenshot_20200725-110113_Vivaldi.jpg)

On iPhone X the select dropdowns are bugged. The wrong value is selected and thus the wrong search result is presented. For example: if you select the tag 'eco' it shows the results for 'air filter'. I searched for a solution and added a file select.js and added the reference in the base.html template. Unfortunately, this does not fix the issue.

