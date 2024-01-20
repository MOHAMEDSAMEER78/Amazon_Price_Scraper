from bs4 import BeautifulSoup
import requests


def scraping(link):
    try:
        soup = BeautifulSoup(link.text, 'html.parser')
        
        product_name_tag = soup.find("span", class_="a-size-large product-title-word-break")  # Adjust the class/tag as needed
        product_name = product_name_tag.text.strip()

        #product_price_tag = soup.find("span", class_="a-size-large product-title-word-break")  # Adjust the class/tag as needed
        #product_price = product_price_tag.text.strip() if product_price_tag else "Price not found"
        #print("Product Price:", product_price)
        return product_name

    except requests.exceptions.HTTPError as e:
        return f"An HTTP error occurred: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
