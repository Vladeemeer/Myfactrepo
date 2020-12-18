from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    login = (By.XPATH, "//li[@class='login-main']//a[@href='#'][normalize-space()='Login']")
    screen = (By.XPATH, "//div[@id='loginscreen']")
    user = (By.XPATH, "//input[@id='username']")
    password = (By.XPATH, "//input[@id='password']")
    submit = (By.XPATH, "//input[@id='_submit']")

    def getLogin(self):
        return self.driver.find_element(*HomePage.login)

    def GetScreen(self):
        return self.driver.find_element(*HomePage.screen)

    def GetUsername(self):
        return self.driver.find_element(*HomePage.user)

    def GetPass(self):
        return self.driver.find_element(*HomePage.password)

    def GetSubmit(self):
        return self.driver.find_element(*HomePage.submit)
