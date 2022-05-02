Feature: checking product details
	
	Scenario: go to user's cart
		Given we want to view a the cart
		When we click the cart link
		Then the page opens

	Scenario: add a product
		Given we want to view a product and have a product list
		When we click the button
		Then page opens
