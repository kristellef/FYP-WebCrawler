from lib.db import DB
import json

from lib.walletExplorerCrawler import WalletExplorerCrawler


from migrations.createTables import createTables

# Load configuration file and connect to database
with open('config.json') as json_file:
    config = json.load(json_file)

db = DB(config['DB'])

createTables(db)

crawler = WalletExplorerCrawler(db,"https://www.walletexplorer.com/wallet/EvolutionMarket/addresses","EvolutionMarket")
crawler.start()