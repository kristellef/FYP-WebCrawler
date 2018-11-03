import requests
import lxml.html as lh
import re
import math

class WalletExplorerCrawler(object):

    def __init__(self,db,url,siteName):
        self.url = url
        self.siteName = siteName
        self.addressesCount = 0
        self.db=db

    def start(self):

    #  Query first page
        actualUrl=self.url
        totalNumberAddresses = self.queryOnePage(actualUrl)
        numberPages = math.ceil(totalNumberAddresses / 100)
        print(totalNumberAddresses,numberPages)
        if (self.addressesCount < totalNumberAddresses):
            for i in range(2,numberPages+1):
                actualUrl = self.url + '?page=' + str(i)
                self.queryOnePage(actualUrl)


    def queryOnePage(self,url):

        #query the page
        page = requests.get(url)
        #parse HTML
        doc = lh.fromstring(page.content)
        #find the rows of the table and store
        tr_elements = doc.xpath('//tr')
        addresses=[]
        for line in tr_elements[1:]:
            addresses.append(line[0].text_content())
        self.addressesCount += len(addresses)
        self.saveAddresses(addresses)

        # Find total number of addresses and return
        s_elements = doc.xpath('//small')
        totalPageNumber = re.findall('\d+', s_elements[0].text_content())

        return (int(''.join(totalPageNumber)))

    def saveAddresses(self,addresses):

        queries=[]
        query = """
                INSERT INTO addresses (address, name) VALUES ('{0}', '{1}');
            """

        for address in addresses:
            queries.append(query.format(address,self.siteName))

        self.db.execute(queries,False);












