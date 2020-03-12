import requests
from bs4 import BeautifulSoup


dpv_url = "http://w3.org/ns/dpv#"

class Description:

    @staticmethod
    def descriptions(data):

        page = requests.get(dpv_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        descriptions = {x: Description.get_description(
            soup, x.replace(" ", "-").lower()) for x in data}
        return descriptions

    @staticmethod
    def get_description(soup, sectionId):

        div = soup.find("section", {"id": sectionId})
        #print(div)
        return div

