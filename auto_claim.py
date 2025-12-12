import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def claim_daily_reward(user_id):
    print(f"\n{'=' * 10} START: {user_id} {'=' * 10}")

    BASE_URL = f"https://hub.playtogether.haegin.kr/go/login?player_id={user_id}&local=vi"

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        print(f"[{user_id}] Login web...")
        driver.get(BASE_URL)

        print(f"[{user_id}] Go to Store...")
        go_to_store_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Go to Store')] | //div[contains(text(), 'Go to Store')]")))
        go_to_store_btn.click()
        print(f"[{user_id}] Clicked 'Go to Store'")

        time.sleep(1)

        print(f"[{user_id}] Finding Free Item...")

        xpath_claim = "//button[contains(., 'Claim')] | //div[contains(text(), 'Claim')] | //span[contains(text(), 'Claim')] | //div[contains(text(), 'Free')]"
        claim_buttons = driver.find_elements(By.XPATH, xpath_claim)

        print(f"[{user_id}] Found {len(claim_buttons)} items to claim.")

        if len(claim_buttons) > 0:
            for index, btn in enumerate(claim_buttons):
                try:
                    print(f"[{user_id}] --- Processing Item {index + 1} ---")

                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(1)

                    wait.until(EC.element_to_be_clickable(btn)).click()
                    print(f"[{user_id}] Clicked Claim item {index + 1}")

                    print(f"[{user_id}] Waiting for 'Continue' popup...")

                    xpath_continue = "//button[contains(., 'Continue')] | //div[contains(text(), 'Continue')] | //button[contains(., 'OK')] | //div[contains(text(), 'OK')]"

                    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_continue)))
                    continue_btn.click()
                    print(f"[{user_id}] Clicked 'Continue/OK' button")

                    time.sleep(1)

                except Exception as e:
                    print(f"[{user_id}] Error at item {index + 1}: {e}")
                    continue
        else:
            print(f"[{user_id}] No 'Claim' buttons found.")

    except Exception as e:
        print(f"[{user_id}] Global Error: {e}")

    finally:
        print(f"[{user_id}] Finished script.")
        driver.quit()

def claim_daily_reward_vi(user_id):
    print(f"\n{'=' * 10} START: {user_id} {'=' * 10}")

    BASE_URL = f"https://hub.playtogether.haegin.kr/vi/go/login?player_id={user_id}&local=vi"

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 10)

    try:
        print(f"[{user_id}] Login web...")
        driver.get(BASE_URL)

        print(f"[{user_id}] Go to Store...")
        go_to_store_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Đi đến Cửa hàng')] | //div[contains(text(), 'Đi đến Cửa hàng')]")))
        go_to_store_btn.click()
        print(f"[{user_id}] Clicked 'Go to Store'")

        time.sleep(1)

        print(f"[{user_id}] Finding Free Item...")

        xpath_claim = "//button[contains(., 'Nhận')] | //div[contains(text(), 'Nhận')] | //span[contains(text(), 'Nhận')] | //div[contains(text(), 'Miễn Phí')]"
        claim_buttons = driver.find_elements(By.XPATH, xpath_claim)

        print(f"[{user_id}] Found {len(claim_buttons)} items to claim.")

        if len(claim_buttons) > 0:
            for index, btn in enumerate(claim_buttons):
                try:
                    print(f"[{user_id}] --- Processing Item {index + 1} ---")

                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                    time.sleep(1)

                    wait.until(EC.element_to_be_clickable(btn)).click()
                    print(f"[{user_id}] Clicked Claim item {index + 1}")

                    print(f"[{user_id}] Waiting for 'Continue' popup...")

                    xpath_continue = "//button[contains(., 'Continue')] | //div[contains(text(), 'Continue')] | //button[contains(., 'OK')] | //div[contains(text(), 'OK')]"

                    continue_btn = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_continue)))
                    continue_btn.click()
                    print(f"[{user_id}] Clicked 'Continue/OK' button")

                    time.sleep(1)

                except Exception as e:
                    print(f"[{user_id}] Error at item {index + 1}: {e}")
                    continue
        else:
            print(f"[{user_id}] No 'Claim' buttons found.")

    except Exception as e:
        print(f"[{user_id}] Global Error: {e}")

    finally:
        print(f"[{user_id}] Finished script.")
        driver.quit()

if __name__ == "__main__":
    LIST_USER_IDS = [
        "DMBETTHLLMYG",
        "RM3ZACRLLMGY",
        "8LCFU5ZLLMYU",
        "PJFVCCRLLMGY",
        "7KECTS9LLMYU",
        "KJBVCCRLLMYG",
        "XMHTYCRLLMYY",
        "YMEG-DD9L-LMGY",
    ]
    LIST_USER_IDS_vi = [
        "KJBVCCRLLMYG",
        "XMHTYCRLLMYY",
        "YMEG-DD9L-LMGY",
    ]

    for uid in LIST_USER_IDS:
        claim_daily_reward(uid)
        time.sleep(1)
        claim_daily_reward(uid)
        time.sleep(1)

    for uid in LIST_USER_IDS_vi:
        claim_daily_reward_vi(uid)
        time.sleep(1)
        claim_daily_reward_vi(uid)
        time.sleep(1)
    print("\nFINISHED.")


