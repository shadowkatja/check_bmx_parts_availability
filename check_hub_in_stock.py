import logging
from datetime import datetime

from playwright.sync_api import sync_playwright


def is_hub_available():
    hub_url = "https://bikemaster.ru/catalog/zapchasti_vtulki/vtulki_perednie/vtulka_perednyaya_xenium_str_41.html"
    BLACK_HUB_SELECTOR = "//tr[.//span[contains(., '36Н')]]"
    BLACK_HUB_OUT_OF_STOCK_INPUT_SELECTOR = "//tr[.//span[text()='36Н черная']]//input[@disabled]"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(hub_url)
            page.wait_for_selector(BLACK_HUB_SELECTOR, timeout=60000)
            element = page.locator(BLACK_HUB_OUT_OF_STOCK_INPUT_SELECTOR)

            if element.count() > 0:
                message_text = 'Втулки нет'
            else:
                message_text = 'Беги заказывай втулку'
            logging.info(f"Результат проверки: {message_text}")
            browser.close()

            return message_text
        except Exception as e:
            logging.info(f"{datetime.now()}️ Ошибка: {e}")
            browser.close()
