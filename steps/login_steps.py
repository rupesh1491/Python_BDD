import allure
from behave import given, when, then
from selenium.webdriver import chrome

from Pages.login_page import loginPage
from selenium import webdriver

from config.config_page import ConfigPage


@given(u'open dshboard page')
@allure.step("Given open dashboard page")
def step_impl(context):
    context.config_page = ConfigPage(browser='chrome')
    context.login_page = loginPage(config_page=context.config_page)
    context.login_page.open_login_page()



@when(u'Enter username "{user}" and password "{paw}"')
@allure.step('When Enter username "{user}" and password "{paw}"')
def step_impl(context,user,paw):
    context.login_page.enter_username(user)
    context.login_page.enter_password(paw)


@then(u'click on login button')
@allure.step("Then click on login button")
def step_impl(context):
    context.login_page.click_login_button()


@then(u'close browser')
@allure.step("Then close browser")
def step_impl(context):
    context.login_page.close_browser()
