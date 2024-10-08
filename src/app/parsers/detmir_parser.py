import re
import time
from typing import Any

import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DetmirParser:
    def __init__(self):
        self.url = "https://www.detmir.ru/"

        options = undetected_chromedriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        # options.binary_location = "/usr/bin/google-chrome"
        self.driver = undetected_chromedriver.Chrome(options=options)

        self.blocks_1_css_selector = ".sY.s_4.bPq.s_9"
        self.blocks_2_css_selector = ".sY.s_4.bO_4.s_9"
        self.blocks_3_css_selector = ".sY.s_4.bO_8.s_9"
        self.blocks_4_css_selector = ".iC.iL"
        self.imgs_4_css_selector = ".CM.CP.CQ"
        self.blocks_5_css_selector = ".sa.fm"

    def get_detmir_data(self) -> list[dict[str, Any]]:
        self.driver.get(self.url)
        time.sleep(3)
        data = []

        web_block_1 = WebDriverWait(self.driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.blocks_1_css_selector))
        )
        block_1 = self.parse_block(web_block_1, 1)
        data.extend(block_1)

        web_block_2 = WebDriverWait(self.driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.blocks_2_css_selector))
        )
        block_2 = self.parse_block(web_block_2, 2)
        data.extend(block_2)

        web_block_3 = WebDriverWait(self.driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.blocks_3_css_selector))
        )
        block_3 = self.parse_block(web_block_3, 3)
        data.extend(block_3)

        web_block_4 = WebDriverWait(self.driver, 25).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.blocks_4_css_selector))
        )[-1]
        element_4 = web_block_4.find_elements(By.CSS_SELECTOR, self.imgs_4_css_selector)
        block_4 = self.parse_block(element_4, 4)
        data.extend(block_4)

        web_block_5 = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.blocks_5_css_selector))
        )
        block_5 = self.parse_adv_block(web_block_5, 5)
        data.extend(block_5)

        return data

    def parse_block(self, elements: list[WebElement], place: int) -> list[dict[str, Any]]:
        data = []
        for i, element in enumerate(elements):
            img_element = element.find_element(By.TAG_NAME, "img")
            content_element = element.find_element(By.XPATH, './following-sibling::a')

            alt_text = img_element.get_attribute('alt')
            img_url = img_element.get_attribute('src')
            content_url = content_element.get_attribute('href')

            data.append({
                "image_url": img_url,
                "content_url": content_url,
                "meta": alt_text,
                "place": place,
                "position": i + 1
            })
        return data

    def parse_adv_block(self, element: WebElement, place: int) -> list[dict[str, Any]]:
        data = []
        content_element = element.find_element(By.TAG_NAME, 'a')
        content_url = content_element.get_attribute('href')

        img_elements = element.find_element(By.TAG_NAME, "div") \
            .find_element(By.TAG_NAME, "div") \
            .find_elements(By.TAG_NAME, "div")

        for i, element in enumerate(img_elements):
            img_urls = element.get_attribute('style')

            urls = re.findall(r'url\("([^"]+)"\)', img_urls)
            urls_list = ";".join(urls)

            data.append({
                "image_url": urls_list,
                "content_url": content_url,
                "meta": None,
                "place": place,
                "position": i + 1
            })
        return data
