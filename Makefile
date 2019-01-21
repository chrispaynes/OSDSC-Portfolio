.PHONY: goodreadsNB

goodreadsNB:
	docker-compose up goodreads-notebook

datascrapeNB:
	docker-compose up data-scrape-notebook
