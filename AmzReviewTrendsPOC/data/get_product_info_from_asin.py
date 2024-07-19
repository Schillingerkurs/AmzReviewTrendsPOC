from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import numpy as np
from tqdm import tqdm
import time
import os
from pathlib import Path
from dotenv import load_dotenv
import os
import requests

# Optional: Caching results
cache = {}

HERE = Path(os.getcwd()).parent.parent


# Load environment variables from .env file
load_dotenv()

def load_existing_reviews(HERE):
    # Define the file path
    interim_path = os.path.join(HERE, 'data', 'interim', 'asin.pkl')

    # Load the DataFrame from the appropriate file
    if os.path.exists(interim_path):
        df = pd.read_pickle(interim_path)
    else:
        raise Exception("No asin scraper file yet!")
    
    return df


def get_product_info(asin):
 
    # Set up Firefox options
    firefox_options = Options()
    firefox_options.headless = True  # Run Firefox in headless mode (no GUI)

    # Initialize Firefox WebDriver
    driver = Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    # URL of the Amazon product page
    url = f"https://www.amazon.com/dp/{asin}"

    # Open the page
    driver.get(url)

    # Wait for the product details section to load (adjust timeout as needed)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "detailBullets_feature_div")))
        
        # Extract the product name
        product_name = driver.find_element(By.ID, "productTitle").text.strip()
        
        # Extract the "Date First Available" text
        date_first_available = driver.find_element(By.XPATH, '//span[contains(text(), "Date First Available")]//following-sibling::span').text.strip()
        
      
        return product_name, date_first_available
    
    except TimeoutException:
        print(f"Timeout waiting for details to load for ASIN {asin}")
        return None, None
    except NoSuchElementException:
        print(f"Element not found for ASIN {asin}")
        return None, None
    finally:
        driver.quit()
    

        
        

def add_product_info(df):
    product_names = []
    dates_first_available = []
    
    for asin in tqdm(df['asin']):
        product_name, date_first_available = get_product_info(asin)
        
        if product_name is None or date_first_available is None:
            product_names.append(np.nan)
            dates_first_available.append(np.nan)
        else:
            product_names.append(product_name)
            dates_first_available.append(date_first_available)
        


    df['Product Name'] = product_names
    df['Date First Available'] = pd.to_datetime(dates_first_available, errors='coerce')  # Convert to datetime
    
    return df



def main(top_n = 30):
    df_raw  =  pd.read_pickle(HERE/ 'data'/'raw'/'hist_review_data.pkl')
    
    existing_asin = load_existing_reviews(HERE)
    
        
    top_asin_missing = (df_raw[~df_raw['asin'].isin(existing_asin['asin'].unique())]
                    ['asin'].value_counts()
                    .head(top_n).reset_index()
                    [['asin']]
                    )
 
    
 
     # Add product information to the DataFrame
    new_asin = add_product_info(top_asin_missing)
      
    
    df_out = (pd.concat([new_asin, existing_asin])
               [['asin', 'Product Name', 'Date First Available']]
               )
    
   
    
    df_out.to_pickle(HERE/'data'/'interim'/'asin.pkl')
     
    
    # df_out = existing_asin.dropna(subset = ['Product Name'])
     # Display the updated DataFrame
    print(len(df_out), "asins stored")




if __name__ == "__main__":
    main()

    

