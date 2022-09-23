import time

from behave import *

from Utilities import configReader
from pageobjects.RegistrationPage import RegistrationPage


@given(u'I navigate to the way2automation site')
def step_impl(context):
    context.reg = RegistrationPage(context.driver)
    context.reg.open(configReader.readConfig("basic info", "testsiteurl"))


@when(u'Enter the Name as "{name}"')
def step_impl(context, name):
    context.reg.setName(name)


@when(u'Enter the PhoneNum ad "{PhoneNumber}"')
def step_impl(context, PhoneNumber):
    context.reg.setPhone(PhoneNumber)


@when(u'Enter the Email as "{email}"')
def step_impl(context, email):
    context.reg.setEmail(email)


@when(u'select the Country as "{country}"')
def step_impl(context, country):
    context.reg.setCountry(country)


@when(u'Enter the City as "{city}"')
def step_impl(context, city):
    context.reg.setCity(city)


@when(u'Enter the Username "{username}"')
def step_impl(context, username):
    context.reg.setUsername(username)


@when(u'Enter the Password as "{password}"')
def step_impl(context, password):
    context.reg.setPassword(password)


@then(u'I click on the submit the form')
def step_impl(context):
    context.reg.submitForm()
    assert False
    time.sleep(10)
