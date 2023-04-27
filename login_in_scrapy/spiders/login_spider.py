import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class login(scrapy.Spider):
    name = 'login'
    start_urls= [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
                                                'csrf_token' : token,
                                                'username' : 'ptushar123@gmail.com',
                                                'password' : '12345'   
                                            },
                                         callback=self.start_scraping   
                                         )


    def start_scraping(self , response):
        open_in_browser(response)
        status="sucessfull"
        yield {"status": status}

