import re
import time
from playwright.sync_api import sync_playwright, expect


def test_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.saucedemo.com/")
        expect(page).to_have_title(re.compile("Swag Labs"))

        # Login
        page.locator("[data-test=\"username\"]").fill('standard_user')
        page.locator("[data-test=\"password\"]").fill('secret_sauce')
        page.locator("[data-test=\"login-button\"]").click()
        
        # Comprueba la URL, si no está logeado este test falla.
        expect(page).to_have_url(re.compile(".*inventory.html"))

        # Añade la mochila y comprueba que luego el texto cambia a "Remove"
        page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_have_text("Remove")

        #Añadimos los dos artículos
        page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()

        #Eliminamos el primer artículo del carrito
        page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
        expect(page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_have_text("Add to cart")

        #Vamos al carrito
        page.locator("[data-test=\"shopping-cart-link\"]").click()
        expect(page).to_have_url(re.compile("https://www.saucedemo.com/cart.html"))

        #Error por no introducir los datos
        page.locator("[data-test=\"checkout\"]").click()
        page.locator("[data-test=\"continue\"]").click()
        expect(page.locator("[data-test=\"error\"]")).to_have_text("Error: First Name is required")

        #Datos personales
        page.locator("[data-test=\"firstName\"]").click()
        page.locator("[data-test=\"firstName\"]").fill("Martin")
        page.locator("[data-test=\"lastName\"]").click()
        page.locator("[data-test=\"lastName\"]").fill("Antelo")
        page.locator("[data-test=\"postalCode\"]").click()
        page.locator("[data-test=\"postalCode\"]").fill("15009")
        page.locator("[data-test=\"continue\"]").click()

       # expect(page.locator("[data-test=\"subtotal-label\"]")).to_have_text("59.980000000000004")
       # expect(page.locator("[data-test=\"tax-label\"]")).to_have_text("4.80")
       # expect(page.locator("[data-test=\"total-label\"]")).to_have_text("64.78")


        page.locator("[data-test=\"finish\"]").click()
        page.locator("[data-test=\"complete-header\"]").click()
        page.locator("[data-test=\"back-to-products\"]").click()
        page.get_by_role("button", name="Open Menu").click()
        page.locator("[data-test=\"logout-sidebar-link\"]").click()
        page.locator("[data-test=\"username\"]").click()
        page.locator("[data-test=\"password\"]").click()


        page.wait_for_timeout(5000)  # wait for 5 seconds to observe the result