.PHONY: jupyterNBBaseImage goodreadsNB datascrapeNB randomizedOptimization8QueensNB

jupyterNBBaseImage:
	docker build ./docker -t local/jupyter_nb_base

goodreadsNB:
	python -m webbrowser -t "http://goodreads-notebook.localhost:8001" && docker-compose up goodreads-notebook

datascrapeNB:
	python -m webbrowser -t "http://data-scrape-notebook.localhost:8002" && docker-compose up data-scrape-notebook

randomizedOptimization8QueensNB:
	python -m webbrowser -t "http://randomized-optimization-8-queens-notebook.localhost:8003" && docker-compose up randomized-optimization-8-queens-notebook

tfLinearRegressionsNB:
	python -m webbrowser -t "http://tf-linear-regression-notebook.localhost:8004" && docker-compose up tf-linear-regression-notebook
