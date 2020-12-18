from selenium.webdriver.common.by import By


class Confirm:

    def __init__(self, driver):
        self.driver = driver

    saveforlater = (By.XPATH, "//li[@id='menu-saved']//a[@role='tab'][normalize-space()='Saved For Later']")
    deleteitem = (By.XPATH, "//button[@id='delete-object']")

    def SaveforLater(self):
        return self.driver.find_element(*Confirm.saveforlater)

    def DeleteItem(self):
        return self.driver.find_element(*Confirm.deleteitem)
