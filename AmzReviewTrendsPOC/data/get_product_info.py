import os
import time
import requests
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager

cache = {}

def get_product_info(asin, token=os.environ.get("GITHUB_APPS_TOKEN")):
    if asin in cache:
        return cache[asin]
    
    try:
        # GitHub API Authentication
        if not token:
            raise Exception("GitHub token is not provided")

        headers = {
            'Authorization': f'token {token}'
        }

        # Example GitHub API call to verify authentication
        github_url = 'https://api.github.com/user'
        response = requests.get(github_url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"GitHub API authentication failed with status code: {response.status_code}")
        
        # Set up Firefox options
        firefox_options = Options()
        firefox_options.headless = True  # Run Firefox in headless mode (no GUI)

        # Initialize Firefox WebDriver
        driver = Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

        # URL of the Amazon product page
        url = f"https://www.amazon.com/dp/{asin}"

        # Open the page
        driver.get(url)

        # Wait for the product details section to load
        product_name = None
        date_first_available = None
        max_retry = 3
        retry_count = 0
        while retry_count < max_retry:
            try:
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "productTitle")))
                product_name = driver.find_element(By.ID, "productTitle").text.strip()

                # Attempt to extract the "Date First Available" text
                try:
                    # XPath modified to find the specific table cell (td) containing the date information
                    date_element = driver.find_element(By.XPATH, '//div[@id="detailBullets_feature_div"]//li[contains(text(), "Date First Available")]/span')
                    date_first_available = date_element.text.strip()
                except NoSuchElementException:
                    print(f"Date First Available not found for ASIN {asin}")
                    date_first_available = "Not available"

                # Cache the result
                cache[asin] = (product_name, date_first_available)
                break  # Exit the retry loop on success
            
            except TimeoutException as e:
                retry_count += 1
                print(f"Retry {retry_count}: Timeout waiting for details to load for ASIN {asin}")
                time.sleep(2 ** retry_count)  # Exponential backoff
            except NoSuchElementException as e:
                print(f"Element not found for ASIN {asin}: {str(e)}")
                break  # Exit the retry loop on element not found
            except Exception as e:
                print(f"Error processing ASIN {asin}: {str(e)}")
                break  # Exit the retry loop on other exceptions

        if product_name is None or date_first_available is None:
            print(f"Failed to fetch details for ASIN {asin}")
        
        driver.quit()
        return product_name, date_first_available
    
    except Exception as e:
        print(f"Error processing ASIN {asin}: {str(e)}")
        return None, None

# # Example usage
# asin = "B0077L8YFI"
product_info = get_product_info(asin)
# print(product_info)

