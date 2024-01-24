from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.pause()
    page.goto("https://mystat.itstep.org/ua/auth/login/index?returnUrl=%2Fua%2Fmain%2Fdashboard%2Fpage%2Findex")
    page.fill("","Логін")
    page.get_by_placeholder("Пароль").fill("dfgdfg")
    page.get_by_role("button", name="Вхід").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
