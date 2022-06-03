import scrapy

#from stackOverflowCrowler.items import StackoverflowcrowlerItem
from coleta.items import ColetaItem

class Sp1Spider(scrapy.Spider):
    name = 'sp1'
    allowed_domains = ['pt.wikipedia.org']
    start_urls = ['http://pt.wikipedia.org/']
    
    def start_requests(self):
        yield scrapy.Request('https://pt.wikipedia.org/wiki/Teorema_de_Bayes', self.parse)

    def parse(self, response):
        data = []
        for a in response.css(".shelf-product"):
            NAME_SELECTOR = ".name-product span ::text"
            PRECO_SELECTOR = ".smallRating span ::text"
            QTD_AVALIACOES = ".qtdReviews ::text"
            nome = a.css(NAME_SELECTOR).getall()
            rating = a.css(PRECO_SELECTOR).getall()
            qtd = a.css(QTD_AVALIACOES).getall()
            for n in range(0,len(nome)):                
                data.append({'nome': nome[n], 'rating': rating[n], 'numberOfRatings:': qtd[n]})
        yield ColetaItem(meuitem=data)