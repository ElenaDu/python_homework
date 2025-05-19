from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json
import time

#Task 3: Write a Program to Extract the data from the Durham Library Site

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Try to open the web page
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    time.sleep(5)

    #Find all the li elements for the search result
    li_elements = driver.find_elements(By.CSS_SELECTOR,"li.cp-search-result-item")
    print(f"The page contains {len(li_elements)} books.")

    results = []
    for li in li_elements:
        try:
            title = li.find_element(By.CLASS_NAME, "title-content").text
            authors = li.find_elements(By.CLASS_NAME, "author-link")
            authors_all = "; ".join(name.text for name in authors)
            format_year = li.find_element(By.CLASS_NAME, "display-info-primary").text

            # Append results
            results.append({
                "Title": title,
                "Author": authors_all,
                "Format-Year": format_year
            })
        except Exception as e:
            print("An error occurred: ",e)

    #Create a DataFrame from this list of dicts. Print the DataFrame
    df = pd.DataFrame(results)
    print(df)

    #Task 4: Write out the Data 
    #Write the DataFrame to a file get_books.csv
    df.to_csv("get_books.csv", index = False)

    #Write the results list out to a file get_books.json
    with open("get_books.json", "w") as f:
        json.dump(results, f, indent=4)

    print("Scraping complete. Data saved to get_books.csv and get_books.json.")

except Exception as e:
    print("Couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")

finally:
    driver.quit()