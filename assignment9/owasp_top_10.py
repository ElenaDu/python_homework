from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    # Try to open the web page
    driver.get("https://owasp.org/www-project-top-ten/")
    time.sleep(5)
    #Find each of the top 10 vulnerabilities
    list_items = driver.find_elements(By.XPATH, '//section[@id="sec-main"]//ul[2]//li')
    if not list_items:
        print("No list items found on the page.")
    else:
        vuln_list = []
        for item in list_items:
            try:
                a = item.find_element(By.CSS_SELECTOR, 'a')
                link = a.get_attribute('href')
                title = a.find_element(By.CSS_SELECTOR, 'strong').text
                vuln_list.append({"title": title, "link": link})
            except Exception as e:
                print("An error occurred: ", e)
            
        #Print out the list
        for vulnerability in vuln_list:
            print(vulnerability)
    
        #Save the data to the owasp_top_10.csv
        with open('owasp_top_10.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['title', 'link'])
            for vulnerability in vuln_list:
                writer.writerow([vulnerability['title'], vulnerability['link']]) 
        print("Scraping complete. Data saved to owasp_top_10.csv.")
except Exception as e:
    print(f"Exception: {type(e).__name__} {e}")

finally:
    driver.quit()