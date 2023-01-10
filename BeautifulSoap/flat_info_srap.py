from bs4 import BeautifulSoup
import requests
from csv import writer

html_content=requests.get('https://www.nobroker.in/flats-for-sale-in-pune_pune').content
soup=BeautifulSoup(html_content,'html.parser')
flats = soup.find_all('div',class_='bg-white rounded-4 bg-clip-padding overflow-hidden my-1.2p mx-0.5p tp:border-b-0 shadow-defaultCardShadow tp:shadow-cardShadow tp:mt-0.5p tp:mx-0 tp:mb:1p hover:cursor-pointer nb__2_XSE')
with open('BeautifulSoap/flats-Info_record.csv','w') as f:
    thewriter= writer(f)
    headers=['Flat_link','Adress','Rate','Type','Built_up_area']
    thewriter.writerow(headers)
    for flat in flats:
        link=flat.find('a',class_='overflow-hidden')['href']
        link='https://www.nobroker.in' + link
        adress=flat.find('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95").text.replace('\n','')
        rate=flat.find('div',class_="font-semi-bold heading-6").span.text.replace('\n','')
        type=flat.find('div',class_="flex flex-1 pl-0.5p").div.next_sibling.div.text.replace('\n','')
        builtup_area=flat.find('div',id="unitCode").text.replace('\n','')
        info=[link,adress,rate,type,builtup_area]
        thewriter.writerow(info)
