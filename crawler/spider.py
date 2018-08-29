from bs4 import BeautifulSoup
from urllib.parse import urljoin
from crawling import *
from general import *
from pokemon import Pokemon
import os
import json
import requests



class Spider():
    base_url = ''
    scrap_tier = 'OU'
    queue_file = '../data/queue.txt'
    crawled_file = '../data/crawled.txt'
    base_folder = '../data/'
    filename = '/extract.json'
    links = ''
    pkmn = list()

    def __init__(self, base_url, page_url):
        Spider.base_url = base_url  
        self.page_url = page_url
        self.directory = '' 
        self.pokemon = Pokemon()     
        self.data = list()
    
    def crawl(self):
        print('Initiating web crawler...')
        if not os.stat(Spider.queue_file).st_size:
            self.harvest_links()
        else:
            self.sow_links()
        self.harvest_data()

    def harvest_links(self):

        print(f'Harvesting links... ', end="\t\t", flush=True) # What's going on
        req = requests.get(self.page_url) # make request 
        soup = BeautifulSoup(req.text, 'html.parser') # parse html
        links = harvest_links(soup, Spider.base_url) # gather all <a> tags that matter from page
        set_to_file(links, self.queue_file) # write harvested links to a file
        self.sow_links()

    def sow_links(self):
        print('Sowing...', end='\t\t', flush=True)
        Spider.links = file_to_set(self.queue_file)
        print('[OK]')

    def harvest_data(self):
        print("Collecting data from website, this will take a while")
        
        i = 0
        total = len(self.links)

        for value in self.links:

            soup = BeautifulSoup(requests.get(value).text, 'html.parser').find_all('div', class_='card')
            harvest_dex(soup[0], self.pokemon)
            harvest_spread(soup[1], self.pokemon)
            harvest_ability(soup[2], self.pokemon)
            harvest_trend(soup[5], self.pokemon, 'teammates')
            harvest_trend(soup[7], self.pokemon, 'counters')

            Spider.pkmn.append(self.pokemon.__dict__)

            print(f'{round((i/total)*100, 2)}', end='\r')
            i = i+1

        self.dump()
        print('Finished!')
            
    def dump(self):
        path = Spider.base_folder        
        write_file(path + Spider.filename, json.dumps(Spider.pkmn))   


           

crawler = Spider('https://azelf.info', 'https://azelf.info/stats/gen7ou/?year=2018&month=5&glicko=1500')
crawler.crawl()