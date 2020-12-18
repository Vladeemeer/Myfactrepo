from selenium.webdriver.common.by import By


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    search = (By.ID, "mymini_userinterfacebundle_search_query_desktop")
    find = (By.ID, "search_button")
    add = (By.XPATH, "//input[@id='save109473']")
    proceed = (By.XPATH, "//a[@id='tnphoto']")
    frame = (By.ID, "aswift_5")
    dismisads = (By.ID, "dismiss-button")
    perf = (By.XPATH, "//a[@id='tnphoto']")
    mylibrary = (By.LINK_TEXT, "My Library")

    def GetSearch(self):
        return self.driver.find_element(*Checkout.search)

    def GetFind(self):
        return self.driver.find_element(*Checkout.find)

    def AddItem(self):
        return self.driver.find_element(*Checkout.add)

    def Proceed(self):
        return self.driver.find_element(*Checkout.proceed)

    def GetFrame(self):
        return self.driver.find_element(*Checkout.frame)

    def DismissAds(self):
        return self.driver.find_element(*Checkout.dismisads)

    def Perform(self):
        return self.driver.find_element(*Checkout.perf)

    def MyLibrary(self):
        return self.driver.find_element(*Checkout.mylibrary)
