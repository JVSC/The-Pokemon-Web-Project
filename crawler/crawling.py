from urllib.parse import urljoin
import harvest.dex as dex

def harvest_links(soup, baseUri):
    links = list()
    targets = soup.find_all(class_='pokemon-line')

    # Looping through table content and harvesting...
    for target in targets: 
        tableheads = target.find_all('th') 
        usage = tableheads[2].contents[0].string.replace('%', '').strip()

        if (float(usage) > 0.8):
            links.append(urljoin(baseUri, tableheads[1].a['href'])) # collecting links
        
    print('[OK]') # Tell when done

    return links   

def harvest_dex(soup, pokemon):
    # tokenize-ish process
    nametokens = soup.find(class_='card-header').string.split(' : ')
    typetokens = soup.find(class_='pokemon-bs').find_all(class_='tag')
    stattokens = soup.find_all(class_='bs_number')
    # parsing
    stattokens = dex.parse_stats(stattokens)
    nametokens = dex.parse_name(nametokens)
    typetokens = dex.parse_type(typetokens)
    # setting attrs
    pokemon.slug = nametokens[1].lower()
    pokemon.name = nametokens[1]
    pokemon.dexNum = nametokens[0]
    pokemon.type = typetokens
    pokemon.stats = stattokens  
    
def harvest_spread(soup, pokemon):
    # grab data
    spreadtoken = soup.find_all(class_='card-text')
    # parse it
    pokemon.sets = dex.parse_spreads(spreadtoken)

def harvest_ability(soup, pokemon):
    # grab it
    abtoken = soup.find_all('li')
    # parse it
    pokemon.abilities = dex.parse_abilities(abtoken)

def harvest_trend(soup, pokemon, trend):
    data = []
    for li in soup.find_all('li'):
        member = { 'tag':'', 'frequency':'' }
        member['tag'] = li.contents[0].string.lower()
        member['frequency'] = li.contents[1].string.replace('%', '')
        data.append(member)

    if trend is 'teammates':
        pokemon.teammates = data
    else: 
        pokemon.counters = data