import base64
import logging
import requests
import json
import time
import xml
import os
import traceback


class AutismchildorganizationspiderSpider(scrapy.Spider):
    name = "autismchildorganizationspider"
    allowed_domains = ["maps.google.com"]
    start_urls = ["https://maps.google.com"]

    def parse(self, response):
        pass
