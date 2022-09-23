from pageobjects.BasePage import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def setName(self, name):
        self.type("nike_XPATH", name)

    def setPhone(self, phoneNum):
        self.type("puma_XPATH", phoneNum)

    def setEmail(self, email):
        self.type("email_XPATH", email)

    def setCountry(self, country):
        self.select("country_XPATH", country)

    def setCity(self, city):
        self.type("city_XPATH", city)

    def setUsername(self, username):
        self.type("username_XPATH", username)

    def setPassword(self, password):
        self.type("password_XPATH", password)

    def submitForm(self):
        self.click("submit_XPATH")
