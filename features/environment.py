import time

import allure
import webdriver_manager
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager

from Utilities import configReader


def before_scenario(context, driver):
    if configReader.readConfig("basic info","browser") == "chrome":
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif configReader.readConfig("basic info","browser") == "firefox":
        context.driver = webdriver.firefox(service=ChromeService(GeckoDriverManager().install()))




def after_scenario(context, driver):
    context.driver.quit()


def after_step(context, step):
    print()
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
