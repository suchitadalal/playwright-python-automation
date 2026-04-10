from playwright.sync_api import Page, Locator  # type: ignore[reportMissingImports]


class ElementsPage:
    URL = "https://demoqa.com/elements"

    def __init__(self, page: Page):
        self.page = page
        self.header: Locator = page.locator(".main-header")
        self.text_box_item: Locator = page.locator("#item-0")
        self.check_box_item: Locator = page.locator("#item-1")
        self.radio_button_item: Locator = page.locator("#item-2")
        self.web_tables_item: Locator = page.locator("#item-3")
        self.buttons_item: Locator = page.locator("#item-4")
        self.links_item: Locator = page.locator("#item-5")
        self.broken_links_item: Locator = page.locator("#item-6")
        self.upload_download_item: Locator = page.locator("#item-7")
        self.dynamic_properties_item: Locator = page.locator("#item-8")

    def goto(self) -> None:
        self.page.goto(self.URL)
