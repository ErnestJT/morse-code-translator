import requests
from typing import ItemsView
from bs4 import BeautifulSoup


def retrieve_morse_alphabet() -> ItemsView:
    website_response = requests.get('https://morsecode.world/international/morse2.html')
    website_response.encoding = 'utf-8'
    website_html = website_response.text

    soup = BeautifulSoup(website_html,'html.parser')
    tables = soup.select('div table.dotdash')[:5]
    
    morse_code: dict[str,str] = {}
    for table in tables:
        words = table.select('tr')[1:]
        
        for word in words:
            char = word.select('td span.morse.tile')
            morse = word.select('td')
            
            if not char:
                continue
            char = char[0].get_text()
            morse = morse[1].get_text()
    
            morse_code.update({char:morse})
    morse_code.update({' ':'/'})
    
    return morse_code.items()
