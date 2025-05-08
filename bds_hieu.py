import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule

def bds_dothi():
    driver = webdriver.Chrome()
    driver.get("https://dothi.net/")
    WebDriverWait(driver, 20)
    driver.find_element(By.ID, "cboCate").click()
    time.sleep(1)
    ds_bds = driver.find_element(By.CSS_SELECTOR, "#cboCate .gridcontainer ul")
    ban_nha_rieng = ds_bds.find_element(By.CSS_SELECTOR, "li[rel='41']")
    ban_nha_rieng.click()
    time.sleep(1)
    driver.find_element(By.ID, "select2-ddlCity-container").click()
    time.sleep(1)
    da_nang_li = driver.find_element(By.XPATH, "//li[starts-with(@id, 'select2-ddlCity-result-') and contains(@id, '-DDN') and text()='Đà Nẵng']")
    da_nang_li.click()
    time.sleep(2)
    driver.find_element(By.ID, "ContentPlaceHolder1_BoxSearch1_lbtSearch").click()
    time.sleep(3)
    dulieu = []
    trang = 1
    while True:
        url = f"https://dothi.net/ban-nha-rieng-da-nang/p{trang}.htm"
        print(url+"\n")
        driver.get(url)
        time.sleep(2)
        posts = driver.find_elements(By.CLASS_NAME, "vip-5-highlight")
        if not posts:
            print("Không còn bài đăng.")
            break
        for post in posts:
            try:
                tde = post.find_element(By.CLASS_NAME, "vip5").get_attribute("title").strip()
                link = post.find_element(By.CLASS_NAME, "vip5").get_attribute("href")
                print(link)
                try:
                    gia = post.find_element(By.CSS_SELECTOR, ".price").text.strip()
                except:
                    gia = "Không có thông tin"
                try:
                    dtich = post.find_element(By.CSS_SELECTOR, ".area").text.strip()
                except:
                    dtich = "Không có thông tin"
                try:
                    dchi = post.find_element(By.CSS_SELECTOR, ".location").text.strip()
                except:
                    dchi = "Không có thông tin"
                # Lấy mô tả chi tiết
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(link)
                time.sleep(2)
                try:
                    mta = driver.find_element(By.CLASS_NAME, "pd-desc-content").text.strip()
                except:
                    mta = "Không có thông tin"
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                dulieu.append({
                    "tieude": tde,
                    "mta": mta,
                    "gia": gia,
                    "dtich": dtich,
                    "diachi": dchi,
                    "link": link
                })
                print(f"Tiêu đề: {tde} - Giá: {gia} - Địa chỉ: {dchi} - Diện tích: {dtich} - Mô tả: {mta} ")
            except Exception:
                print("Lỗi")
        trang += 1
    driver.quit()
    df = pd.DataFrame(dulieu)
    df.to_excel("BDSDothi.xlsx", index=False)

bds_dothi()
schedule.every(1).day.at("06:00").do(bds_dothi)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)