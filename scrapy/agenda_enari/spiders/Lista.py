        # -*- coding: utf-8 -*-
import scrapy
from agenda_enari.items import AgendaEnariItem
import re

class ListaSpider(scrapy.Spider):
    name = 'Lista'
    allowed_domains = ['listanainternet.com.br']
    start_urls = ['http://www.listanainternet.com.br/inicio']

    def parse(self, response):
        for item in response.css("html body div.main div.cat div.row-fluid ul.span3 li.btn-cat0"):
            link = item.css("a::attr(href)").extract_first()
            yield response.follow(link, self.parse_categoria)



    def parse_categoria(self, response):
        for link in response.css("html body div.main div.container div.row-fluid div.span8 div.item div.item-inner a::attr(href)").extract():
            yield response.follow(link, self.parse_empresas)

    def parse_empresas(self, response):
        for link in response.css("html body div.main div.container div.row-fluid div.span8 div.item.item_ad div.item-inner a::attr(href)").extract():
            yield response.follow(link, self.parse_empresa)
    
    def parse_empresa(self, response):
        nome = response.css('html body div.main div.row-fluid div.span8.content div.title.blue-lis font::text').extract_first()
        endereco = response.css("html body div.main div.row-fluid div.span8.content div.contacts.row-fluid div.span7.address p::text").extract_first()
        telefone = response.css("html body div.main div.row-fluid div.span8.content div.contacts.row-fluid div.span5.phone span::text").extract_first()
        telefone = re.sub(r'\s', '', telefone)
        empresa = AgendaEnariItem(nome = nome, endereco = endereco, telefone = telefone)
        yield empresa