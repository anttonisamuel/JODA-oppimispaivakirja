import scrapy


class RedditScraperSpider(scrapy.Spider):
    name = 'reddit_scraper'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/dogs/']

    def parse(self, response):
        links = response.xpath("//img/@src")
        html = ""

        for link in links:
            url = link.get()

            if any(extension in url for extension in [".jpg"]):
                html += """<a href="{url}" target="_blank"><img src="{url}" height="25%" width="25%"/><a/>""".format(url=url)

                with open("dogs.html", "a") as page:
                    page.write(html)
                    page.close()
