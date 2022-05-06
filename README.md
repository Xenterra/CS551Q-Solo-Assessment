# CS551Q-Solo-Assessment
#### Codio Terminal Commands
##### Startup Commands
These will need to be applied in order to start maintenance on the project from a new device
git init #This prepares the project for github integration, whether on setup or for pulling from an existing repository
git pull git@github.com:Xenterra/CS551Q-Solo-Assessment.git master #pulls the files from the repository, when the remote is not set up. May ask for confirmation.
source .venv/bin/activate 	# this activates the virtual environment
python3 manage.py runserver 0.0.0.0:2500 #  the app locally  on port 2500, shown in the URL below

##### GitHub Project Details
GitHub Username: Xenterra
GitHub Repository Name: CS551Q-Solo-Assessment.git
Example Codio Box URL: https://meteoramigo-heliumalmond-2500.codio-box.uk
(This will change depending on the codio box it is run in)

##### All GitHub  Commands
- git init 				  #create target folder for the Git Repository
- git status              #check the current status of the GitHub repository
- git add .               #add changes to the local repo
- git commit -m "update"  #save changes made to the local repo
- git push origin master  #push the local changes to the master branch of the repo
- git pull origin master  #pull the repository from git hub and merge files 

These commands are used to update the Git server and check the status 

##### Heroku Commands
- git push heroku master	#commit the changes of Git's master branch to Heroku, this will redeploy as a new version
- heroku status				#used to check how the Heroku deployment is progressing
- heroku login				#used to initially setup connection with heroku
-- Use 'heroku login -i' to complete the login within the terminal
- heroku git:remote -a cs551q-solo-assessment	#used to initially setup connection between git and heroku
- heroku config:set DISABLE_COLLECTSTATIC=0 #using either 0 or 1 to turn the function on or off for static integration

Heroku URL: https://cs551q-solo-assessment.herokuapp.com/

As Heroku is run automatically, use the status command to check its functioning well, and the 'push heroku' command to apply changes to a new version of the app

##### Other Terminal Commands of note
pip freeze > requirements.text #This command will create the txt file that records pip module versions, mainly for heroku.
python3 manage.py makemigrations #Prep the system for changes to the models.py file. (Required for the next command to work)
python3 manage.py migrate #Implement changes from the model.py file into the system.
behave #When used while in the top folder, it will activate the automatic testing that has been created.
python manage.py createsuperuser #used to create a new user with full access rights. Asks for further details upon entry.
python3 database_fill.py #Used to initiate the program that converts the .csv file in the database for the system.
python3 manage.py startapp shopApp #Creates the app folder that will hold the system functionality.
python3 manage.py startapp mysite #creates the app folder that will hold the website information and the server specifications.

#### Web Pages
##### These will follow either the Codio Box URL or the Heroku URL
###### Main Created Pages
- /						# Home Page
- /appDetails/			# Details page for individual items
- /statistics/			# Page for charts
- /search/				# App Search Page
- /cart/				# Shopping Basket Page
- /register/			# Page with form for new users
- /purchase/			# Confirmation of Purchase
- /purchase/complete/	# Landing Page after purchase

##### Registration Pages
###### These follow from the /account/ subset and were mainly from the University material
- /login					# Page that contains the login form.
- /password_reset_complete	# These pages form the password reset functionality, however this function is not fully implemented.
- /password_reset_confirm	# These pages form the password reset functionality, however this function is not fully implemented.
- /password_reset_email		# These pages form the password reset functionality, however this function is not fully implemented.
- /password_reset_done		# These pages form the password reset functionality, however this function is not fully implemented.
- /password_reset_form		# These pages form the password reset functionality, however this function is not fully implemented.

#### Testing
##### Behave
Three Tests currently 
The first test scenario, "go to user's cart", has been created to first; test that the test environment is functioning correctly and second; check that the basic elements of the system have been successfully created in the testing environment. 
The second test is to check that the user can create an account which will automatically log the user in upon the account being created. This checks the page links, the registration form, the login feature and the display of the user login.
The final test is to check that the user can add an item from the system to their own basket. However, this test could not be completed due to me being unable to add data to the testing environment so I was unable to test this in an automatic format.

##### Manual Test - Main Functionality
The steps below are a scenario test to be completed to test the viability of the system when used for it's intended purpose:
1. Open the website's home page and click the Login button at the top left of the screen
2. Complete the login form using a valid username and password combination.
2.a. If you don't already have an account, click the '+ Create Account' button and fill the form to make an account.
3. As you should be on the home page, with a list of apps, click on one of the 'More Details' button present on the right side of the page
4. You should now be on the details page for the app selected. Scroll to the bottom of the page and click the 'Add to Basket' button.
**Result part 1:** You should now be on the basket page with only one item visable in the displayed list.
5. Click the 'Search' button in the menu bar to open the search page.
6. In the 'Text' entry field, type out 'Age of Conquest: World' and click the search button.
7. One record should be displayed, repeat steps 3 and 4 to add this item to the basket.
**Result part 2:** You should now be on the cart page with 2 items in your basket. 
8. At the bottom of the table of items you should see a total and the Purchase Basket button. Click this button.
9. You should now be on the purchase page, your user details should already be entered, needing bank card details to be entered.
10. Once the detials are checked and filled, click the 'Complete Transaction' button
**Final Result:** You should be on a page showing your order number and a return to home link.
**~Further Check** If you are an admin, you can go to the admin panel and check that this order has been completed and ready for processing.

#### Remaining Errors
- (minor) logging in when on the Details page reloads the page with the form details. This makes the page a blank table.
- (major) Third Behave test is unable to be completed due to there being no data in the test environment.