

""" Esta me pareció la manera más correcta de hacerlo y comprensible usando una aproximación
que deja un poco de lado la estructura de PlayWright. Lo hice también usando un conftest y fixtures, pero 
no conozco bien aún la librería y me da algunos fallos, como que abre 2 pestañas antes de realizar todos los test
Me estuve peleando bastante con el contexto en el fixture y conseguí solucionarlo, pero entonces
daba otros fallos, como no realizar todos los test.
 """


from playwright.sync_api import  expect, sync_playwright
import re
import time

class Automation:
    def __init__(self):  
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False,args=["--start-maximized"])
        self.context = self.browser.new_context(no_viewport=False)
        self.page = self.context.new_page()
        self.environment = None
    
    def login(self, username, password):
        self.page.goto("https://www.saucedemo.com/")
        self.page.locator("//input[@id='user-name']").fill(username)
        self.page.locator("//input[@id='password']").fill(password)
        self.page.locator("//input[@id='login-button']").click()
    
    def burgerNavigate(self,menuItem):
        self.page.locator("//button[@id='react-burger-menu-btn']").click()
        self.page.locator("//a[@id='" + menuItem + "']").click()
    
    def logout(self):
        self.burgerNavigate("logout_sidebar_link")

    def add_and_remove_items(self):
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        expect(self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_have_text("Remove")
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
        self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]").click()
        expect(self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_have_text("Add to cart")
        self.page.locator("[data-test=\"shopping-cart-link\"]").click()

    def make_purchase(self):
        self.page.locator("[data-test=\"shopping-cart-link\"]").click()
        expect(self.page).to_have_url(re.compile("https://www.saucedemo.com/cart.html"))    
        self.page.locator("[data-test=\"checkout\"]").click()
        self.page.locator("[data-test=\"continue\"]").click()
        expect(self.page.locator("[data-test=\"error\"]")).to_have_text("Error: First Name is required")
        self.page.locator("[data-test=\"firstName\"]").click()
        self.page.locator("[data-test=\"firstName\"]").fill("Martin")
        self.page.locator("[data-test=\"lastName\"]").click()
        self.page.locator("[data-test=\"lastName\"]").fill("Antelo")
        self.page.locator("[data-test=\"postalCode\"]").click()
        self.page.locator("[data-test=\"postalCode\"]").fill("15009")
        self.page.locator("[data-test=\"continue\"]").click()
        expect(self.page.locator("[data-test=\"total-label\"]")).to_have_text("Total: $64.78")
        expect(self.page.locator("[data-test=\"subtotal-label\"]")).to_have_text("Item total: $59.980000000000004")
        expect(self.page.locator("[data-test=\"tax-label\"]")).to_have_text("Tax: $4.80")
        self.page.locator("[data-test=\"finish\"]").click()
        self.page.locator("[data-test=\"complete-header\"]").click()
        expect(self.page.locator("[data-test=\"complete-header\"]")).to_have_text("Thank you for your order!")
        self.page.locator("[data-test=\"back-to-products\"]").click()
    
    def are_inputs_visible(self):
            user_name_input = self.page.locator("//input[@id='user-name']")
            password_input = self.page.locator("//input[@id='password']")
            assert user_name_input.is_visible()
            assert password_input.is_visible()
           
       

demo = Automation()
demo.login("standard_user", "secret_sauce")

def test_main(): 
    time.sleep(2)
    demo.add_and_remove_items()
    demo.make_purchase()
    demo.logout()
    demo.are_inputs_visible()