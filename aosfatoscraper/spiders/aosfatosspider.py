import scrapy
from aosfatoscraper.items import AosfatoscraperItem

class AosfatosspiderSpider(scrapy.Spider):
    name = "aosfatosspider"
    allowed_domains = ["www.aosfatos.org"]
    start_urls = ["https://www.aosfatos.org/noticias/checamos/"]

    def parse(self, response):
        news = response.css('a.entry-item-card') #Aqui estou armazenando a resposta dentro
        #de uma variável
        
        for new in news: #Estou percorrendo cada item desse css e criando um dicionário
            link = new.css('a.entry-item-card::attr(href)').get()
            newurl = "https://www.aosfatos.org" + link
            yield response.follow(newurl, callback = self.parse_newscheck_page)
        
        next_page = response.css('a.next-arrow::attr(href)').get() #esse é o link para próxima página

        if next_page is not None: #Se a proxima página existir, monta o link completo
            next_page_url = "https://www.aosfatos.org/noticias/checamos/" + next_page
            yield response.follow(next_page_url, callback = self.parse)# e chama a função novamente nele.

    def parse_newscheck_page(self, response):
        news_check_item = AosfatoscraperItem()

        link_meta = "https://www.aosfatos.org/noticias/como-funciona-a-parceria-do-aos-fatos-com-o-programa-de-verificacao-de-desinformacao-da-meta/"
        link_metodologia = "/metodologia-2015/"

        paragraphs = response.css(".ck-article p")
        ultimo_paragrafo = paragraphs[-1]
        hrefs_ultimo = ultimo_paragrafo.css("a::attr(href)").getall()
        text_ultimo = ''.join(ultimo_paragrafo.css("::text").getall())
        todos_menos_ultimo = response.css(".ck-article p")[1:-1]
        counter = -1


        while "1." not in text_ultimo:
            counter = counter - 1
            ultimo_paragrafo = paragraphs[counter]  # Muda para o penúltimo
            text_ultimo = ''.join(ultimo_paragrafo.css("::text").getall())
            todos_menos_ultimo = response.css(".ck-article p")[1:counter]    
        
        hrefs = ultimo_paragrafo.css("a::attr(href)").getall()
        texto = todos_menos_ultimo.css("*::text").getall()
        referencias = "\n".join(hrefs)
        texto = " ".join(texto)

        
        news_check_item['url'] = response.url
        news_check_item['text'] =  texto
        news_check_item['date'] = response.css(".publish-date::text").get()
        news_check_item['title'] = response.css(".ck-article > h1::text").get()
        news_check_item['fonte'] = "Aos Fatos"
        news_check_item['check'] = response.css(".inline-stamp > img:nth-child(1)::attr(alt)").get()
        news_check_item['referencias'] = referencias

        
        
        yield  news_check_item

