def make_shirt(size='large',text='I love Python'):
    print('The shirt is in '+size+' scale.')
    print('And there are some words on it:')    
    print(text.title())

##size = input('The size of the shirt is:')
##text = input('Words on the shirt are:')
##
##make_shirt(size,text)

##make_shirt()
##
##make_shirt(size = 'medium')
##
##make_shirt(text = 'Hello World!')

def describe_city(city_name,country = 'China'):
    print(city_name.title()+' is in '+country.title())

describe_city('Chengdu')
describe_city(city_name = "Xi'an")
describe_city(city_name = 'reykjavik',country = 'iceland')
describe_city('london','england')
