from pprint import pprint
from typing import Any

import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DetmirParser:
    def __init__(self):
        self.url = "https://www.detmir.ru/"
        self.driver = undetected_chromedriver.Chrome()

        self.blocks_1_css_selector = ".tO.tV.bNf.t_"
        self.blocks_2_css_selector = ".tO.tV.bM_1.t_"
        self.blocks_3_css_selector = ".tO.tV.bM_5.t_"
        self.blocks_4_css_selector = ".Y_._5x"
        self.imgs_4_css_selector = ".QG.QJ.QK"
        self.blocks_5_css_selector = ".er.hk"

    def get_detmir_data(self):
        self.driver.get(self.url)
        data = []

        web_block_1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.blocks_1_css_selector))
        )
        block_1 = self.parse_block(web_block_1, 2)
        data.extend(block_1)

        web_block_2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.blocks_2_css_selector))
        )
        block_2 = self.parse_block(web_block_2, 2)
        data.extend(block_2)

        web_block_3 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.blocks_3_css_selector))
        )
        block_3 = self.parse_block(web_block_3, 3)
        data.extend(block_3)

        web_block_4 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.blocks_4_css_selector))
        )[-1]
        element_4 = web_block_4.find_elements(By.CSS_SELECTOR, self.imgs_4_css_selector)
        block_4 = self.parse_block(element_4, 4)
        data.extend(block_4)

        return data

    def parse_block(self, elements: list[WebElement], place: int) -> dict[str, Any]:
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



if __name__ == "__main__":
    detmir_parser = DetmirParser()
    res = detmir_parser.get_detmir_data()
    pprint(res)
