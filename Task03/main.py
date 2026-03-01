from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import random
import time
import os

chrome_options = Options()
prefs = {
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 20)

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

def take_screenshot(step_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"screenshots/{timestamp}_{step_name}.png"
    driver.save_screenshot(file_path)
    print(f"-- Скриншот сохранен: {file_path}")

def scrollTo(xPath: str) -> None:
    item = wait.until(EC.presence_of_element_located((By.XPATH, xPath)))
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", item)
    time.sleep(2)

def clickTo(xPath: str) -> None:
    item = wait.until(EC.element_to_be_clickable((By.XPATH, xPath)))
    driver.execute_script("arguments[0].click()", item)
    time.sleep(2)

def testCase1() ->None:
    print("-------- Добавление товара в корзину --------")
    print("1. Сайт открыт.")
    take_screenshot("site_opened")
    scrollTo("//h2[contains(text(), 'Часто заказывают')]")

    print("2. Выбираем часто заказываемую пиццу")
    clickTo("//h2[contains(text(), 'Часто заказывают')]/following-sibling::div//button | //h2[contains(text(), 'Часто заказывают')]/parent::section//article[1]")
    take_screenshot("pizza_selected")

    print("3. Добавляем его в корзину")
    clickTo("//button[contains(., 'В корзину за')]")
    take_screenshot("pizza_selected")
    
    print("4. Выбираем точку откуда заберем заказ")
    clickTo("//button[contains(., 'Забрать из пиццерии')]")
    take_screenshot("pickup_selected")

    clickTo("//p[contains(.,'Цены, меню и акции зависят от пиццерии')]/../../div[2]/div[2]/div[1]/ul/li[1]")
    take_screenshot("pickup_point_chosen")

    clickTo("//p[contains(.,'Цены, меню и акции зависят от пиццерии')]/../../button[contains(.,'Выбрать')]")
    take_screenshot("pickup_confirmed")
    
    print("5. Кнопка подтверждения выбора нажата.")

    print("6. Открытие корзины")
    clickTo("//button[contains(., 'Корзина')]")
    take_screenshot("cart_opened")

    print("7. Тест успешно завершен.")
    print()

def testCase2() ->None:
    print("-------- Изменение параметров товара (кастомизация) --------")
    print("1. Листаем до блока 'Часто заказывают'")
    scrollTo("//h2[contains(text(), 'Часто заказывают')]")
    take_screenshot("scrolled_popular_tc2")

    print("2. Выбираем часто заказываемую пиццу")
    clickTo("//h2[contains(text(), 'Часто заказывают')]/following-sibling::div//button | //h2[contains(text(), 'Часто заказывают')]/parent::section//article[1]")
    take_screenshot("pizza_opened_tc2")

    print("3. Выбираем тонкое тесто")
    clickTo("//label[contains(.,'Тонкое')]")
    take_screenshot("pizza_opened_tc2")

    print("4. Меняем размеры пиццы на 35см")
    clickTo("//label[contains(.,'35')]")
    take_screenshot("size_35_selected")

    print("5. Добавляем его в корзину")
    clickTo("//button[contains(., 'В корзину за')]")
    take_screenshot("custom_pizza_added")

    print("6. Тест успешно завершен.")
    print()

def testCase3() -> None:
    print("-------- «Применение несуществующего промокода» (Негативный сценарий) --------")

    promo_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Промокод']")))
    print("1. Поле промокода найдено")
    take_screenshot("promo_field_found")
    promo_input.click()

    invalid_promo = "ОШИБКА2024"
    print(f"2. Вводим невалидный промокод: {invalid_promo}")
        
    for char in invalid_promo:
        promo_input.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))
    take_screenshot("promo_field_found")

    print("3. Пробуем его применить")
    clickTo("//a[contains(.,'Применить')]")
    take_screenshot("promo_apply_clicked")
    time.sleep(5) # для ручного прохождения капчи

    error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='promocode-error']")))
    print(f"4. Ошибка валидации получена: {error_msg.text}")
    take_screenshot("promo_error_displayed")
    # Промокод не найден. Попробуйте другой
    print("5. Тест успешно завершен.")
    time.sleep(4)
    print()

if __name__ == '__main__':
    driver.get("https://dodopizza.ru/saransk")
    try:
        testCase1()
        testCase2()
        testCase3()
    except Exception as e:
       print(f"ОШИБКА: {e}")
       driver.save_screenshot("fail_reason.png")
       print("Скриншот ошибки сохранен как 'fail_reason.png'")
    finally:
        driver.quit()