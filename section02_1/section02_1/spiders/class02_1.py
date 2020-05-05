# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = "test2"
    allowed_domains = ["blog.scrapinghub.com"]
    start_urls = ["https://blog.scrapinghub.com/"]

    def parse(self, response):
        """
        :param : response
        :return : Title Text
        """

        # 2가지(Css selector, xpath)
        # getall() <-> get(), extract() <-> extract_first()

        # 예제1(Css selector)
        # 출력 옵션
        # -o 파일명.확장자, -t 파일타입(json, jsonlines, jl, csv, xml, marshal, pickle)
        for text in response.css("div.post-header > h2 > a::text").getall():
            # return type : Request, BaseItem, Dictionary, None
            yield {"text": text}

        # 예제2(xpath)
        # for i, text in enumerate(
        #     response.xpath('//div[@class="post-header"]/h2/a/text()').getall()
        # ):
        #     yield {"number": i, "text": text}
