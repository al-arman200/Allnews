from bs4 import BeautifulSoup
import requests

class webScraping():
    technology =  requests.get('https://techna.news/')
    Sport      =  requests.get('http://www.parseek.com/Sport/')
    Political  =  requests.get('https://www.tasnimnews.com/fa/service/1/%D8%B3%DB%8C%D8%A7%D8%B3%DB%8C')
    Economic   =  requests.get('https://www.shahrekhabar.com/%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%DB%8C')
    
    technology_soup = BeautifulSoup(technology.text,'html.parser')
    Sport_soup      = BeautifulSoup(Sport.text,'html.parser')
    Political_soup  = BeautifulSoup(Political.text,'html.parser')
    Economic_soup   = BeautifulSoup(Economic.text,'html.parser')

    technology_tag_a = technology_soup.find_all('a',attrs={'class':'post-thumb'})[:8]
    Sport_tag_a      = Sport_soup.find_all('div',attrs={'class':'newslist'})[:8]
    Political_tag_a  = Political_soup.find_all('section',attrs={'class':'news-container news-box'})[1]
    Economic_tag_a   = Economic_soup.find_all('ul',attrs={'class':'news-list-items clearfix'})[1]
    
    def getNews_technology(self ):
        news = []
        for i in self.technology_tag_a:
            title = self.desTagA(i['aria-label'])
            link  = 'https://techna.news/'+i['href']
            news.append((title , link))        
        return news

    def getNews_Sport(self ):
        news = []
        for i in self.Sport_tag_a[1]:
            h = i.find_all('a')[:8]
            for j in h:
                title = self.desTagA(j.text)
                link  = 'http://www.parseek.com'+j['href']
                news.append((title , link))
        return news

    def getNews_Political(self ):
        news = []
        news1 = self.Political_tag_a.find_all('a')[1:9]
        for i in news1:
            title = self.desTagA(i.text)
            link  = 'https://www.tasnimnews.com'+i['href']
            news.append((title , link))
        return news

            
    def getNews_Economic(self ):
        news = []
        news1 = self.Economic_tag_a.find_all('a')[:8]
        for i in news1:
            title = self.desTagA(i.text)
            link  = i['href']
            news.append((title , link))
        return news

    def desTagA(self ,des):
        if len(des)>70 :
            return des[:80]
        else :
            count = 70- len(des)
            for i in range(count):
                des +=' '
            return des
            
def main():
	test = webScraping()
	E = test.getNews_Economic()
	T = test.getNews_technology()
	S = test.getNews_Sport()
	P = test.getNews_Political()
	pp= [E,T,S,P]
	for i in pp:
	    for j in i:
    		print('\n %s \n %s  \n _____________'%(j[0],j[1]))
