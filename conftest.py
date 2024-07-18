# conftest.py
import pytest
from playwright.sync_api import sync_playwright, Browser, Page

@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    yield page
    page.close()

@pytest.fixture(scope="session")
def login(context):
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill('standard_user')
    page.locator("[data-test=\"password\"]").fill('secret_sauce')
    page.locator("[data-test=\"login-button\"]").click()
    yield context
    page.close()