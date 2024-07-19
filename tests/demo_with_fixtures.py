import re
import pytest
from playwright.sync_api import expect, Page, BrowserContext, sync_playwright

def test_add_and_remove_items(page: Page):
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_have_text("Remove")
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_have_text("Add to cart")
    page.locator("[data-test=\"shopping-cart-link\"]").click()

def checkout(page: Page):
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page).to_have_url(re.compile("https://www.saucedemo.com/cart.html"))
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_have_text("Error: First Name is required")
    page.locator("[data-test=\"firstName\"]").fill("Martin")
    page.locator("[data-test=\"lastName\"]").fill("Antelo")
    page.locator("[data-test=\"postalCode\"]").fill("15009")
    page.locator("[data-test=\"continue\"]").click()
    page.locator("[data-test=\"finish\"]").click()
  

def logout(page: Page):
    page.locator("[data-test=\"back-to-products\"]").click()
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"logout-sidebar-link\"]").click()

@pytest.mark.usefixtures("login")
def test_demo(login:BrowserContext):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.locator("[data-test=\"username\"]").fill('standard_user')
        page.locator("[data-test=\"password\"]").fill('secret_sauce')
        page.locator("[data-test=\"login-button\"]").click()
        expect(page).to_have_url(re.compile(".*inventory.html"))
        page.goto("https://www.saucedemo.com/")
        expect(page).to_have_title(re.compile("Swag Labs"))
        expect(page).to_have_url(re.compile(".*inventory.html"))
        test_add_and_remove_items(page)
        checkout(page)
        logout(page)
        page.wait_for_timeout(5000)  
        page.close()