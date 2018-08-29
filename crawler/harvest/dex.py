def parse_name(nametokens):
    new = []
    for token in nametokens:
        new.append(token.replace("#", '').strip())
    return new

def parse_type(typetokens):
    newToken = []
    for token in typetokens:
        token = token.string.replace(' ', '')
        newToken.append(token)
    
    return newToken

def parse_spreads(spreadtoken):
    
    newToken = []
    
    for spread in spreadtoken:
        tempSpread = {'spread':'', 'nature': '', 'usage':''}
        temtoken = parse_stats(spread.find_all(class_='value'))

        tabledata = spread.find_all('td')
        tempSpread['nature'] = tabledata[0].string
        tempSpread['usage'] = tabledata[12].string.replace("%", '')
        tempSpread['spread'] = temtoken

        newToken.append(tempSpread)
    
    return newToken
        
def parse_stats(bstoken):

    data = { 'HP': 0, 'Attack': 0, 'Defense': 0, 'SpA': 0,   'SpD': 0, 'Speed': 0 }
    i = 0

    for key in data:
        data[key] = bstoken[i].string
        i = i+1

    return data

def parse_abilities(abtoken):
    
    array = []
    
    for lists in abtoken:
        abilities = {'abilityName': '', "usage": '' }
        abilities['usage'] = lists.find('div').string.replace("%", '')
        abilities['abilityName'] = lists.contents[0]
        array.append(abilities)
    
    return array