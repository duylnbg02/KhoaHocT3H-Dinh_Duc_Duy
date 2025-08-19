from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    web = pw.chromium.launch(channel="chrome", headless=False)  #True : chay o che do an - False : chay o che do cua so
    context = web.new_context()  #Tao 1 trinh duyet rieng biet
    page = context.new_page() #Tao 1 tab moi
    page.goto("https://clickspeedtest.com/",wait_until="domcontentloaded") #link duong dan
    # Click bắt đầu trước


    # Lặp click nhiều lần vào cùng vị trí
    for i in range(1000000):
        page.locator("text='Click Here to Start Playing'").click()
        page.wait_for_timeout(0)

    page.wait_for_timeout(100000)
