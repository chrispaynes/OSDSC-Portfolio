PYTHON_NB_FILES := $(shell find . -name "*.ipynb")
PYTHON_PY_FILES := $(shell find . -name "*.py")

.PHONY: jupyterNBBaseImage goodreadsNB datascrapeNB randomizedOptimization8QueensNB tfLinearRegressionsNB mnistHandwrittenNB

jupyterNBBaseImage:
	docker build ./docker -t local/jupyter_nb_base


formatPythonNB:
	nbqa black .
	nbqa ruff check --fix .

formatPythonPY:
	ruff format .
	ruff check --fix .

goodreadsNB:
	python -m webbrowser -t "http://goodreads-notebook.localhost:8001" && docker-compose up goodreads-notebook

datascrapeNB:
	python -m webbrowser -t "http://data-scrape-notebook.localhost:8002" && docker-compose up data-scrape-notebook

randomizedOptimization8QueensNB:
	python -m webbrowser -t "http://randomized-optimization-8-queens-notebook.localhost:8003" && docker-compose up randomized-optimization-8-queens-notebook

tfLinearRegressionsNB:
	python -m webbrowser -t "http://tf-linear-regression-notebook.localhost:8004" && docker-compose up tf-linear-regression-notebook

mnistHandwrittenNB:
	python -m webbrowser -t "http://mnist-handwritten-notebook.localhost:8005" && docker-compose up mnist-handwritten-notebook

practicalMLtutNB:
	python -m webbrowser -t "http://practical-ml-tut-notebook.localhost:8006" && docker-compose up practical-ml-tut-notebook

timeseriesAirbnbNB:
	python -m webbrowser -t "http://timeseries_airbnb_nb.localhost:8007" && docker-compose up timeseries_airbnb_nb
