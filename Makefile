.PHONY: goodreadsNB

goodreadsNB:
	docker-compose up goodreads-notebook

datascrapeNB:
	docker-compose up data-scrape-notebook

randomizedOptimization8QueensNB:
	docker-compose up randomized-optimization-8-queens-notebook
