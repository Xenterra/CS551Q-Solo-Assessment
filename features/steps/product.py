import urllib
from urllib.parse import urljoin, urlparse
from behave import given, when, then, model
from django.conf import settings
from django.shortcuts import resolve_url

@given(u'we want to view a the cart')
def user_on_index_page(context):
	print("Given Step Here:")
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	print(base_url)
	open_url = urljoin(base_url,'/')
	context.browser.get(open_url)

@when(u'we click the cart link')
def user_clicks_cart_button(context):
	context.browser.find_element_by_name('cartLink').click()

@then(u'the page opens')
def cart_page_opens(context):
    assert 'cartPage' in context.browser.page_source


@given(u'we want to view a product and have a product list')
def user_on_index_page(context):
	print("Given Step Here:")
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	print(base_url)
	open_url = urljoin(base_url,'/')
	context.browser.get(open_url)

@when(u'we click the button')
def user_clicks_more_button(context):
	#print(context.browser.page_source)
	context.browser.find_element_by_name('selectButton').click()

@then(u'page opens')
def details_page_opens(context):
    assert 'Icon' in context.browser.page_source