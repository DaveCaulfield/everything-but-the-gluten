# Everything but the Gluten

Everything but the gluten is a recipe sharing website helping people find and share gluten free recipes. The aim of the site is to help people living with coeliac disease on their life long gluten free journey.
Users are able to sign up to create their own personal account where they can post recipes, comment on recipes and save their favourite recipes.



View the live site here [Everything but the Gluten](https://everything-but-the-gluten.herokuapp.com/)

![landing page](README/assets/responsive.png)


## Features

### The Nav Bar
- There are different variations of the navbar feature depending on three possible users. 
    - A first time vistor or a user that has not signed into the site - Visitor navbar
    - A site member who has signed in - Members navbar
    - an admin user who has signed in - Admin navbar


### Visitor navbar

![Navbar visitor](README/assets/features/navbar-visitor.png)

- The visitor navbar is displayed when the site first loads. It contains navigation links to the Home page, Recipes page, About page, Login page and Register page. The sites name Everything but the Gluten is also displayed to the left and is used as a link to the homepage.


### Member navbar

![Navbar member](README/assets/features/navbar-member.png)

- The Member navbar is displayed when a user has successfully signed into the site. 
- A custom drop down menu feature greets the user displaying their username. 
- Within the users custom drop down menu are links to:
    - Add a Recipe - allows the user to submit a recipe
    - My Published Recipes - displays all recipes the user has submiited and have been approved.
    - My Favourite Recipes - displays all recipes the user has saved a s a favourite
    - My Pending Recipes - displays all recipes the user has submitted which are still waiting on approval.
    - Change Password - allows the user to change their password.
    - Sign out - allows the user to sign out.

- Each of the dropdown links also contain an icon to give an added visual indication to the user to assist them in navigating the site.


### Admin navbar

![Navbar admin](README/assets/features/navbar-admin.png)

- The Admin navbar is displayed when an admin has successfully signed into the site. 
- A custom drop down menu feature greets the admin displaying their username. 
- Within the admin custom drop down menu are links to:
    - Recipes Waiting - displays all recipes awaiting admin approval. 
    - Add a Recipe - allows the user to submit a recipe
    - My Published Recipes - displays all recipes the user has submiited and have been approved.
    - My Favourite Recipes - displays all recipes the user has saved a s a favourite
    - My Pending Recipes - displays all recipes the user has submitted which are still waiting on approval.
    - Change Password - allows the user to change their password.
    - Sign out - allows the user to sign out.

- Each of the dropdown links also contain an icon to give an added visual indication to the user to assist them in navigating the site.

- The navbar is fully responsive for mobile and tablet devices.


![Navbar mobile visitor](README/assets/features/navbar-mobile-vistor.png)

![Navbar mobile member](README/assets/features/navbar-mobile-member.png)

![Navbar mobile admin](README/assets/features/navbar-mobile.png)




### The landing page


![landing page1](README/assets/features/landing-page1.png) 

- The landing page contains a background image of a grandmother and granddaughter in a kitchen. The main colours of the image are white and light grey, this colour tone is continued through the site and provides a subtle and neutral feel to the site. The image is also very eye catching to anyone with coeliac disease (the main target audience). The image conveys the message that even though they are baking which is a high risk to coeliacs unless strict adherance to gluten free ingredients is followed the grandmother and granddaughter are also conveying the message of trust.

- A welcome messsage is displayed to the user with a descrption of the sites features.
- A call to action button leads the user to the Recipes section.
- The landing page is fully responsive for mobile and tablet devices.

![landing mobile](README/assets/features/landing-mobile.png) 


### The footer

![footer](README/assets/features/footer.png) 

A subtle footer contains social media icon links in the same color style as the rest of the site. The icon color changes to silver when hovered on.


### The Recipes page

![recipe page](README/assets/features/recipe-page.png) 

- The recipes page displays all recipes that have been submitted and approved.
- The recipes are displayed on bootstrap styled cards with a shadow effect added to highlight each of them.
- All vistors to the site can view the displayed recipes.
- All vistors to the site can click on a recipe to bring them to the recipe details page.
- The recipe page uses pagination to display 6 recipes at a time.


### The Pagination Menu

![pagination menu](README/assets/features/pagination-menu.png) 

- The pagination menu sits below the displayed recipes. It provides an easy to use navigation systme to the user.
- A first page and last page button allow easy and quick navigation to the first or last page.
- A next page and previous page arrow icon allows the user to quickly browse forward or back through pages of recipes.
- The current page being displayed is also highlighted to the user.
- This pagination menu gives the user an enjoyable and natural user experience.


### Add Recipe

![Add Recipe](README/assets/features/recipe-form-1.png) 
![Add Recipe](README/assets/features/recipe-form-2.png) 

- The Add Recipe feature uses a form to allow registered members to submit recipes.
- A Summernote editor has been add to the ingredients and instructions fields.
- An image file can be uploaded with the recipe, if a file is not uploaded by the user then a default placeholder image will be used.


### Input Validation

![Add Recipe](README/assets/features/form-validation.png) 

- Input validation has been applied allowing only alphanumeric characters in the title, only numbers in the preparation and cooking time fields.
- All fields are required to be filled.
- Feedback messages are displayed to the user if any field is not filled out correctly.


### Success Message

![Awaiting approval](README/assets/features/awaiting-message.png) 

- When a recipe has been successfully submitted a success message is displayed indicating that the recipe is now awaiting approval.
- Recipes are reviewed by administrator to ensure they only contain gluten free ingredients.

### Pending Recipes Page

![pending](README/assets/features/pending.png) 

- My Pending Recipe Page displays the registered members recipes that have been submitted and are awaiting approval.
- After a user has successfully submitted a recipe they are redirected to their Pending Recipes page where they can see a list of any recipes they have submitted that are awaiting approval.


### Published Recipes Page

![pending](README/assets/features/published-recipes.png) 

- My Published Recipe Page displays the registered members recipes that have been approved and are now published on the site.


### Favourite Recipes Page

![favourites](README/assets/features/favourites.png) 

- My Favourite Recipe page displays all the recipes that the user has marked as a favourite recipe.


### Recipe Details Page

![recipe details](README/assets/features/recipe-detail-a.png) 
- The Recipe Details page gives the full details of a recipe.
- The top of the page dislays the recipe title and author.
- If the user is the author of the recipe they are given the option of anEdit button anda Delet button. This is only displayed if the user is the author of the recipe.
- The option to Add to Favourites is also displayed allowing the user to save a recipe as a favourite by clicking on the heart outline icon. 

![recipe details](README/assets/features/saved-to-favourites.png) 
- When the user has added the recipe to their favourites the icon and text change to reflect this.
- A chat icon is also displayed and indicates the number of comments the recipe has received.

![recipe details](README/assets/features/recipe-detail-b.png) 

![recipe details](README/assets/features/recipe-detail-c.png) 
- The recipe details contain an image, a list of Ingredients and a list of Instruction steps.


### comments

![comments](README/assets/features/comments.png) 
- The Comments area is at the end of the recipe details page.
- The Comments area is only available to registered members.
- Only members can leave comments on recipes.
- Members comments are posted without the need for admin approval as it was felt this gives are more engaging experience to the user interacting with the site.


### Edit Recipe

![Edit Recipe](README/assets/features/edit-recipe-1.png) 
![Edit Recipe](README/assets/features/edit-recipe-2.png) 
- The edit recipe feature is availble to edit a recipe.
- A member can edit any recipe of which they are the author by selecting the Edit Button on the recipe detail page.
- A recipe form with the poulated details of the recipe is displayed which allows the author to edit the recipe. 
- When a recipe is updated it is submitted for review by an admin user before being approved. This is to ensure all recipes on the site only contain gluten free ingredients.

![update message](README/assets/features/update-message.png) 
-  A message is displayed to user when they submit an update or edit to a recipe.


### Delete Recipe

![Delete Recipe](README/assets/features/delete-recipe.png) 
- A member can delete their own recipe by selecting the Delete Button on the recipe details page.
- A message box displays a confirmation option to the user with the recipe title in it.


### Admin User - Recipes Waiting 

![admin menu](README/assets/features/admin-menu.png) 

![recipes waiting](README/assets/features/recipes-waiting.png) 

- The admin user has access to a Recipes Waiting page that allow them to see any recipes that are awaiting approval.


### Admin User - Recipe Approval

![admin approval](README/assets/features/admin-approved-1.png)
![admin approval](README/assets/features/admin-approved-2.png)

- The admin user can then select a recipe thats awaitng approval, review it and then set the recipe at the bottom of the recipe form to Published & Approved.
- Once approved the recipes will be published on the site for all users to see.



### Change Password

![Change Password](README/assets/features/change-password.png)

- The Change Password page allows a member to change their own password by filling out the password form


### Sign out

![Sign out](README/assets/features/sign-out.png)

- The Sign out page displays when the user selects to sign out from the navigation menu. 
- A message box displays a confirm sign out or cancel sign out button to the user.

## Future Features
- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



## Design

### User Experience (UX)
- The user experience (UX) and user interface (UI) was considered from the start of the design process. The site aims to give the user an enjoyable experience whilst easily and intuitively navigating and interacting with the site on mobile, tablet, laptop or desktop devices.

### Colour scheme

- Adobe color was used to extract the background colour #E9F0F2 from a background image used in the site.
- #E9F0F2 is also used as the background colour for the navbar and footer giving a an uncluttered and neutral feel to the site.

![colour](README/assets/color.png)

- The background image is used on the add recipe form page and update recipe form page. 
- Only the background colour #E9F0F2 is used on the recipe display pages to allow the recipes to stand out to the user.


- The font colour used is bootstraps secondary grey	#6C757D



### Wireframes

- [Balsamiq](https://balsamiq.com/wireframes/) was used to create wireframes for mobile, tablet and desktop versions of the site. See the screen shots here [Wireframes](wireframe.md)


## Wireframes


### Mobile

-  ![Wireframe](README/wireframe/wf-mobile-1.PNG)
-  ![Wireframe](README/wireframe/wf-mobile-2.PNG)
-  ![Wireframe](README/wireframe/wf-mobile-3.PNG)
-  ![Wireframe](README/wireframe/wf-mobile-4.PNG)
-  ![Wireframe](README/wireframe/wf-mobile-5.PNG)
-  ![Wireframe](README/wireframe/wf-mobile-6.PNG)
-  ![Wireframe](README/wireframe/wf-mobile-7.PNG)
-  ![Wireframe](README/wireframe/wf-mobile-8.PNG)
-  ![Wireframe](README/wireframe/wf-mobile-9.PNG)

[Back to top](#Everything-but-the-Gluten)

### Tablet

-  ![Wireframe](README/wireframe/wf-tablet-1.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-2.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-3.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-4.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-5.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-6.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-7.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-8.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-9.PNG)
-  ![Wireframe](README/wireframe/wf-tablet-10.PNG)

[Back to top](#Everything-but-the-Gluten)

### Desktop

-  ![Wireframe](README/wireframe/wf-desktop-1.PNG)
-  ![Wireframe](README/wireframe/wf-desktop-2.PNG)
-  ![Wireframe](README/wireframe/wf-desktop-3.PNG)
-  ![Wireframe](README/wireframe/wf-desktop-4.PNG)
-  ![Wireframe](README/wireframe/wf-desktop-5.PNG)
-  ![Wireframe](README/wireframe/wf-desktop-6.PNG)
-  ![Wireframe](README/wireframe/wf-desktop-7.PNG)


[Back to top](#Everything-but-the-Gluten)



## Data Model
-  A Recipe Model and a Comments Model were created for the database.
- Django Allauth was used to handle user authentication which uses Django's built-in User Model.

![data model](README/assets/data_model.png)



## User Stories

As a site visitor 
- I can view a pagination display of recipes so that I can easily see posted recipes.
- I can see the number of likes a recipe has  so that I can easily view favorited recipes
- I can click on a recipe so that I can see all the ingredients and instructions
- I can create an account so that I can post Recipes, Likes and Comments 

As a site member 
- I can sign into my account so that I can access the features available to members
- I can post a recipe so that I can share recipes on the site
- I can edit my recipes so that I can make changes if needed
- I can delete my recipes so that I can remove my recipes from the site if needed.
- I can Like/Unlike a recipe so that favorite recipes are highlighted 
- I can change my password so that I can change my password if needed
- I can display my published recipes so that I can easily see all recipes I have posted
- I can write comments on recipes so that I can interact with the community.
- I can see my pending recipes so that I can easily track my recipes
- I can see my favourite recipes so that I can easily access my favourite recipes


As a site admin 
- I can approve submitted recipe posts so that I can ensure post are suitable for display.
- I can reset account passwords so that an account can be unlocked if a member forgets their password.

[Back to top](#Everything-but-the-Gluten)


## Agile Develeopment 

- Agile methodology was used to manage developmenet of this project by breaking down the requirements and features for the site into user stories. 
- Acceptance criterias were assingned to each of the user stories 
- A list of software development tasks required to complete the user story objective and meet the acceptence criteria formed the steps of development to be carried out.

![user-story](README/assets/user_story.png)

- Githubs project kanban feature was used for easy tracking of user stories.
- A template was created for adding the user stories which populated them as issue into the To Do column of the kanban board.
- User stories were moved into the In Progress column while being worked on.
- Once all tasks belonging to a user story were completed and the acceptence criteria was met the user story was moved into the Done Column.

![user-story](README/assets/kanban.png)

[Back to top](#Everything-but-the-Gluten)



## Testing

Please see the [testing](testing.md) page for details of Everything but the Gluten testing. 




 ## Technologies Used

### Languages
  - python - used to develop the backend of the site.
  - HTML - used to structure webpage layout of website.
  - CSS - used to style webpages.

### Frameworks
 - Django Python Framework - used to create the backend structure for the site.
 - Bootstrap - used to style the website, add responsiveness and interactivity.
 - Django-allauth - used for account authentication.


### Database
- PostgreSQL - used as the deployed sites database.


### Other Tecnologies
- Cloudinary - image hosting service to store uploaded static and media files
- Gitpod - used as the IDE
- Git used for version control 
- GitHub - used for hosting the code repository
- Heroku - used as the cloud based deployment platform
- Balsamiq - used to create the wireframes
- Chrome DevTools - used for inspecting and debugging the site
- Crispy Forms - used to render and style Django Forms
- Font Awesome - used to source icons
- Github Projects - used to track user stories progress through the project
- Summernote - used as an editor within forms.
- Favicon.io - used for the favicon
- Adode Color - used for the color theme
- Google Sheets - for the database model tables and manual testing



[Back to top](#Everything-but-the-Gluten)




 ## Deployment
 - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


## Credits

### Content
- [BBC Goodfood](https://www.bbcgoodfood.com/) - for the recipes content and images
- [Pexels](https://www.pexels.com) - for the background images
- [CoreySchafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) - for the Class based vies and pagination YouTube tutorials.
- [Learn Django](https://learndjango.com/tutorials/django-slug-tutorial) - for the slug tutorial
- [Bootstrap](https://getbootstrap.com/) - for the custom drop down navigation menu
- [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tips/2016/08/04/django-tip-9-password-change-form.html) - for the change password feature.
- [djangoproject](https://docs.djangoproject.com/en/4.1/) - for adding messages in class based views
- [stackoverflow](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown) - for delete message function
- [stackoverflow](https://stackoverflow.com/questions/17165147/how-can-i-make-a-django-form-field-contain-only-alphanumeric-characters) - for alphanumeric input validation



## Acknowledgements
This site was built as my Portfolio 4 Project for the Full Stack Software Developer Diploma at the Code Institute.
I would like to thank my cohort facilitator Kasia Bogucka, my mentor Precious Leige, the Slack community, Tutor support and Student Care for the help and support provided to me throughout this project.
