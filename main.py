import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('demo_cache')


class SiteScraper(object):

    def __init__(self, current_url):
        self.url = current_url
        self.data = []

    def make_request(self):
        return requests.get(self.url).text

    def make_soup(self):
        return BeautifulSoup(self.make_request(), 'html.parser')

    def get_title(self):
        for item in self.make_soup().find('h1'):
            self.data.append(item)
        return self.data

    def get_para(self):
        para = self.make_soup().find(attrs="mw-parser-output").p
        result_list = []
        for all in para:
            result_list.extend(all.stripped_strings)
        return [" ".join(result_list)]

    def get_sommaire(self):
        title = self.make_soup().find(class_="toctitle").get_text()
        div = self.make_soup().find(class_="toc")
        ul = div.findChildren("ul", recursive=False)
        for child in ul:
            list = child.get_text().strip()
        return title + "\n" + list

    def get_list_title(self):
        item = self.make_soup().find(id="List_of_Available_Champions").text
        return item

    def get_champion_list_legend(self):
        table = self.make_soup().find(class_="champions-list-legend").tbody
        rows = table.find_all('tr')
        data = []
        for i in rows:
            table_data = i.children
            result = [j.text.replace("\n", "") for j in table_data]
            data.append(result)
        return data

    def get_champion_list(self):
        table = self.make_soup().find(class_="article-table").tbody
        rows = table.find_all('tr')
        data = []
        for i in rows:
            table_data = i.children
            result = [j.text.replace("\n", "") for j in table_data]
            data.append(result)
        return data

    def get_scrapped_title(self):
        item = self.make_soup().find(id="List_of_Scrapped_Champions").text
        return item

    def get_scrapped(self):
        div = self.make_soup().find(class_="columntemplate")
        ul = div.findChildren("ul", recursive=False)
        for child in ul:
            list = child.get_text().strip()
        return list

    def get_trivia(self):
        item = self.make_soup().find(id="Trivia").text
        return item

    def get_urf(self):
        item = self.make_soup().find_all(attrs={"title": "Urf"})
        return item[1].text


if __name__ == "__main__":
    get_para = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_para()
    get_title = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_title()
    get_sommaire = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_sommaire()
    get_list_title = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_list_title()
    get_champion_list_legend = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_champion_list_legend()
    get_champion_list = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_champion_list()
    get_scrapped_title = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_scrapped_title()
    get_scrapped = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_scrapped()
    get_trivia = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_trivia()
    get_urf = SiteScraper(r'https://leagueoflegends.fandom.com/wiki/List_of_champions').get_urf()

    for i in get_title:
        print(i)
    for i in get_para:
        print(i)
    print(get_sommaire)
    print(get_list_title)
    for i in get_champion_list_legend:
        print(i)
    for i in get_champion_list:
        print(i)
    print(get_scrapped_title)
    print(get_scrapped)
    print(get_trivia)
    print(get_urf)
