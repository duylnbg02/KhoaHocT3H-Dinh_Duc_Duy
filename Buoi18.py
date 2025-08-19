from playwright.sync_api import sync_playwright


# from playwright.async_api import async_playwright
class HoangHaScraper:
    def __init__(self, headless=False, name_browser="chrome"):
        self.headless = headless
        self.name_browser = name_browser

    def start_browser(self):
        self.pw = sync_playwright().start()
        self.browser = self.pw.chromium.launch(channel=self.name_browser, headless=self.headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def go_to_page(self, url_web: str):
        try:
            self.page.goto(url_web, wait_until="domcontentloaded")
            print("Truy cập vào web OK",url_web)
            return True
        except Exception as e:
            print("error go to page",url_web, e)
            return False

    def search_product(self,keyword:str):
        search_box = self.page.locator("input[placeholder='Hôm nay bạn muốn tìm kiếm gì?']").first
        if search_box.is_visible():
            self.page.wait_for_timeout(1000)
            search_box.fill(keyword)
            self.page.wait_for_timeout(5000)

    def close_browser(self):
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.pw:
            self.pw.stop()

    def get_products(self):
        products = []
        list_item = self.page.query_selector_all("div.v5-item")
        for item in list_item:
            product = self.get_item(item)
            products.append(product)
            print(products)
            break

    def get_item(self,item):
        product = {}
        name = item.query_selector("h3 a.text-limit").text_content().strip()
        url_img = item.query_selector("a.img img").get_attribute("src")
        return product

if __name__ == "__main__":
    scapper = HoangHaScraper()
    scapper.start_browser()
    if scapper.go_to_page("https://hoanghamobile.com/"):
        # scapper.search_product("samsung")
        # scapper.get_products()
        if scapper.search_product("samsung"):
            scapper.page.click()
            scapper.page.hover("")
            scapper.page.mouse.move("")
            scapper.page.mouse.up("")
            scapper.page.mouse.down("")
            scapper.page.wait_for_timeout(50000)