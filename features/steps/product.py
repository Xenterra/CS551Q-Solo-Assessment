import urllib
from urllib.parse import urljoin, urlparse
from behave import given, when, then, model
from django.conf import settings
from django.shortcuts import resolve_url
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'we want to view a the cart')
def user_on_index_page(context):
	#print("Cart Given Step Here:")
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	#print(base_url)
	open_url = urljoin(base_url,'/')
	context.browser.get(open_url)

@when(u'we click the cart link')
def user_clicks_cart_button(context):
	context.browser.find_element_by_name('cartLink').click()

@then(u'the page opens')
def cart_page_opens(context):
	assert 'cartPage' in context.browser.page_source



@given(u'we are on the home page')
def user_on_index_page(context):
	#print("Login Given Step Here:")
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	#print(base_url)
	open_url = urljoin(base_url,'/')
	context.browser.get(open_url)
	
@when(u'the user moves to the register page')
def user_navigates_to_registration(context):
	context.browser.find_element_by_name("noUsername").click()
	context.browser.find_element_by_name("registration").click()

@then(u'the user provides valid login details')
def user_enters_login_details(context):
	username = context.browser.find_element_by_name('username')
	username.send_keys("admin")
	email = context.browser.find_element_by_name('email')
	email.send_keys("admin@admin.com")
	password1 = context.browser.find_element_by_name('password1')
	password1.send_keys("admin1234+")
	password2 = context.browser.find_element_by_name('password2')
	password2.send_keys("admin1234+")
	context.browser.find_element_by_name("registerButton").click()	
	print(context.browser.page_source)

@then(u'the user is logged in')
def browser_returns_to_home(context):
	assert 'usernameHeading' in context.browser.page_source



@given(u'we want to view a product and have a product list')
def user_on_index_page(context):
	#print("Product List Given Step Here:")
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	#print(base_url)
	open_url = urljoin(base_url,'/')
	context.browser.get(open_url)

@when(u'we click the button')
def user_clicks_more_button(context):
	#print(context.browser.page_source)
	context.browser.find_element_by_name('selectButton').click()

@then(u'page opens')
def details_page_opens(context):
	assert 'Icon' in context.browser.page_source