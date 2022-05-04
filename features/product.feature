Feature: checking product details
	
	Scenario: go to user's cart
		Given we want to view a the cart
		When we click the cart link
		Then the page opens

	Scenario: user wishes to create a login
		Given we are on the home page
		When the user moves to the register page
		Then the user provides valid login details
		Then the user is logged in

	Scenario: add a product
		Given we want to view a product and have a product list
		When we click the button
		Then page opens
