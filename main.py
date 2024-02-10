import requests
from bs4 import BeautifulSoup
import os
import webbrowser










def main():

    info = requests.get(input("Input your desired NY times recipe URL: ")).text
    soup = BeautifulSoup(info, 'html.parser')
    
    html = str(soup)
    path = os.path.abspath('temp.html')
    url = 'file://' + path
    with open(path, 'w') as f:
        f.write(html)
        webbrowser.open(url)
    
    print(soup)

    

    # this is pretty cool... Use for later???
    # print(soup.get_text())



main()