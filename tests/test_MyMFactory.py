import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import Checkout
from PageObjects.ConfirmPage import Confirm
from PageObjects.HomePage import HomePage


@pytest.mark.usefixtures("setup")
class TestOne:
    def test_MMF(self):
        homepage = HomePage(self.driver)
        homepage.getLogin().click()
        homepage.GetScreen()
        homepage.GetUsername().send_keys("Vladimeer")
        homepage.GetPass().send_keys("myfact456")
        homepage.GetSubmit().click()

        //kl;kl;kk;lfdfdfdfdfrrrrrrrrrrrrrrrrrr

        checkout = Checkout(self.driver)
        checkout.GetSearch().send_keys("Test")
        checkout.GetFind().click()
        checkout.AddItem().click()
        checkout.Proceed().click()

        iframe = checkout.GetFrame()
        self.driver.switch_to.frame(iframe)
        checkout.DismissAds().click()
        self.driver.switch_to.default_content()

        action = ActionChains(self.driver)
        action.move_to_element(checkout.Perform()).perform()
        action.move_to_element(checkout.MyLibrary()).click().perform()

        confirm = Confirm(self.driver)
        confirm.SaveforLater().click()
        # time.sleep(10)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//button[@id='delete-object']")))
        confirm.DeleteItem().click()

        alert = self.driver.switch_to.alert
        alert.accept()
