# -*- coding: utf-8 -*-

# Scrapy settings for lfpscrappy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'lfpscrappy'

SPIDER_MODULES = ['lfpscrappy.spiders']
NEWSPIDER_MODULE = 'lfpscrappy.spiders'

FEED_EXPORTERS_BASE = {
    'json': 'scrapy.contrib.exporter.JsonItemExporter',
    'csv': 'scrapy.contrib.exporter.CsvItemExporter'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lfpscrappy (+http://www.yourdomain.com)'
