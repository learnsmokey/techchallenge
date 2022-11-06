import time

from behave import given, when, then


@given("Open amazon page")
def open_amazon(context):
    context.app.main_page.open_amazon_website()


@when("Search for books")
def search_book(context):
    context.app.main_page.search_items('books')


@then("Verify Correct product is searched")
def verify_product(context):
    context.app.main_page.verify_items()


@when("Search for {arg0}")
def search_items(context, arg0):
    context.app.main_page.search_items(arg0)


@when("Search for1 {arg0}")
def search_items(context, arg0):
    context.app.main_page.clear_search()
    context.app.main_page.search_items(arg0)


@when("Search item {arg0}")
def search_items(context, arg0):
    context.app.main_page.search_items(arg0)
    time.sleep(2)
    context.app.main_page.search_button()
    time.sleep(2)
    context.app.main_page.clear_search()
    time.sleep(2)


@then("Click on search button")
def search_button(context):
    context.app.main_page.search_button()
    time.sleep(2)


@then("Search for peppa pig")
def step_impl(context):
    context.app.main_page.search_items('peppa pig')