#Write the boiler plate code for using beautifulsoup
# import the library
from bs4 import BeautifulSoup
import requests
from bs4 import Tag
exhaustiveList = []
# specify the url
for j in range(1,29):
    for i in range(1, 100):
        if len(str(j)) == 1:
            url = 'https://results.eci.gov.in/PcResultGenJune2024/candidateswise-S' + str(j) + '0' + str(i)+ '.htm'
        else:
            url = 'https://results.eci.gov.in/PcResultGenJune2024/candidateswise-S' + str(j) +str(i)+ '.htm'

        # query the website and return the html to the variable ‘page’
        page = requests.get(url)
        
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page.text, 'html.parser')
        constituency_list = soup.find_all('span')
        try:
            constituency = constituency_list[4].text
            
            constituency = constituency[4:]
            # Take out the <div> of name and get its value
            name_box = soup.find('div', attrs = {'class': 'cand-box'})
            leaderName = name_box.find('h5')
            partyName = name_box.find('h6') 

            info = name_box.find('div', attrs = {'class': 'status won'})
            info_list = info.find_all('div')
        
                # name = name_box.text.strip() # strip() is used to remove starting and trailing
            
            candidate = [constituency,leaderName.text, partyName.text, info_list[0].text.capitalize(), info_list[1].text]
            exhaustiveList.append(candidate)    
            
        except:
            break
            
            
        


