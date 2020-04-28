import requests
from bs4 import BeautifulSoup


dpv_url = "http://w3.org/ns/dpv#"


class Description:


    @staticmethod
    def descriptions(data):
        
        """
        Fetches the DPV markup for the widget descriptions by sending a request to
        the DPV webpage

        @type data: list 
        @param data: A list of all the categories the program will fetch the descriptions for

        @rtype: dictionary
        @return: The keys in this dictionary are the categories specified in the data parameter,
        the values are the markup for each key.
        """
        page = requests.get(dpv_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        descriptions = {x: Description.get_description(
            soup, x.replace(" ", "-").lower()) for x in data}
        return descriptions

    @staticmethod
    def get_description(soup, sectionId):

        """
        Parses the DPV markup for each key.

        @type soup: BeautifulSoup object
        @param soup: A nested data structure of the document.

        @type sectionId: String
        @param sectionId: A key which finds the document node containing the appropriate markup.

        @rtype div: String
        @return div: The markup of section's div.
        """

        div = soup.find("section", {"id": sectionId})
        #print(div)
        return div

