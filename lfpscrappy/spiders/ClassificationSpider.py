import scrapy
from ..items import TeamClassification

# 3rd party imports
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import FormRequest


class ClassificationSpider(Spider):
    name = "classificationspider"
    allowed_domains = ["lfp.es"]
    start_urls = ['http://www.lfp.es']

    args_pattern = r'?'

    def parse(self, response):
        # Build season IDs
        season_ids = ["0"+str(x) for x in range(28,100)]
        season_ids += ["10"+str(x) for x in range(0,10)]
        season_ids += ["1"+str(x) for x in range(10,14)]
        for season in season_ids:
            yield FormRequest.from_response(response,
                                        url="http://www.lfp.es/includes/ajax.php",
                                        formname='estadisticas_historicas',
                                        formdata={
                                                'input_competicion':'Primera',
                                                'input_temporada': str(season),
                                                'input_temporada_nombre': str(season),
                                                'action':'estadisticas_historicas',
                                                'tipo':'clasificacion'
                                        },
                                        callback=self.parse_classification)

    def parse_classification(self, response):
        sel = Selector(response)
        title = sel.xpath('//div[@class="flotar_izquierda"]/text()').extract()[0].split(' ')
        season = int(title[4][:-1])
        round_number = int(title[6][:-1])
        table_rows = sel.xpath('//tr')
        for row in table_rows:
            item = TeamClassification()
            table_columns = row.xpath('td')
            if len(table_columns)>0:
                item['season'] = season
                item['round'] = round_number
                item['rank'] = int(table_columns[0].xpath('text()').extract()[0][:-1])
                item['name'] = table_columns[1].xpath('span/text()').extract()[0]
                item['points'] = int(table_columns[2].xpath('text()').extract()[0])
                yield item