import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def claim_daily_reward():
    # Cấu hình user_id và URL
    BASE_URL = "https://hub.playtogether.haegin.kr/go/login?player_id=AKHE-TTHL-LMGC&local=vi"

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Tạm thời comment headless để bạn dễ debug (nhìn thấy trình duyệt)
    options.add_argument("--window-size=1920,1080")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 20)

    try:
        print("Login web...")
        driver.get(BASE_URL)

        print("Go to Store...")
        go_to_store_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Go to Store')] | //div[contains(text(), 'Go to Store')]")))
        go_to_store_btn.click()
        print("Clicked 'Go to Store'")

        time.sleep(5)

        print("Finding Free Item...")

        xpath_claim = "//button[contains(., 'Claim')] | //div[contains(text(), 'Claim')] | //span[contains(text(), 'Claim')] | //div[contains(text(), 'Free')]"
        claim_buttons = driver.find_elements(By.XPATH, xpath_claim)

        print(f"Found {len(claim_buttons)} items to claim.")

        if len(claim_buttons) > 0:
            for index, btn in enumerate(claim_buttons):
                try:
                    print(f"--- Processing Item {index + 1} ---")

                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(1)  # Đợi scroll ổn định

                    wait.until(EC.element_to_be_clickable(btn)).click()
                    print(f"Clicked Claim item {index + 1}")

                    print("Waiting for 'Continue' popup...")

                    xpath_continue = "//button[contains(., 'Continue')] | //div[contains(text(), 'Continue')] | //button[contains(., 'OK')] | //div[contains(text(), 'OK')]"

                    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_continue)))
                    continue_btn.click()
                    print("Clicked 'Continue/OK' button")

                    time.sleep(3)

                except Exception as e:
                    print(f"Error at item {index + 1}: {e}")
                    continue
        else:
            print(" No 'Claim' buttons found.")

    except Exception as e:
        print(f"Global Error: {e}")

    finally:
        print("Finished script.")
        time.sleep(5)
        driver.quit()


if __name__ == "__main__":
    claim_daily_reward()