import pytest
from playwright.sync_api import Page, expect

@pytest.mark.usefixtures("login")
def test_add_backpack_to_cart(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_have_text("Remove")