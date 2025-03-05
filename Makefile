<<<<<<< HEAD
PYTHON_NB_FILES := $(shell find . -name "*.ipynb")
PYTHON_PY_FILES := $(shell find . -name "*.py")

.PHONY: jupyterNBBaseImage goodreadsNB datascrapeNB randomizedOptimization8QueensNB tfLinearRegressionsNB mnistHandwrittenNB
=======
# Variables
DOCKER_COMPOSE_CMD := docker-compose up
WEB_BROWSER_CMD := python -m webbrowser -t
>>>>>>> e20b6bd (formatting)

# Notebook URLs
GOODREADS_URL := "http://goodreads-notebook.localhost:8001"
DATASCRAPE_URL := "http://data-scrape-notebook.localhost:8002"
RANDOMIZED_OPTIMIZATION_URL := "http://randomized-optimization-8-queens-notebook.localhost:8003"
TF_LINEAR_REGRESSION_URL := "http://tf-linear-regression-notebook.localhost:8004"
MNIST_HANDWRITTEN_URL := "http://mnist-handwritten-notebook.localhost:8005"
PRACTICAL_ML_TUT_URL := "http://practical-ml-tut-notebook.localhost:8006"
TIMESERIES_AIRBNB_URL := "http://timeseries_airbnb_nb.localhost:8007"

# Phony targets
.PHONY: help jupyterNBBaseImage formatPythonNB formatPythonPY \
        goodreadsNB datascrapeNB randomizedOptimization8QueensNB \
        tfLinearRegressionsNB mnistHandwrittenNB practicalMLtutNB \
        timeseriesAirbnbNB

# Help
help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Build
jupyterNBBaseImage: ## Build the base image for the jupyter notebooks
	docker build ./docker -t local/jupyter_nb_base


formatPythonNB:
	nbqa black .
	nbqa ruff check --fix .

formatPythonPY:
	ruff format .
	ruff check --fix .

goodreadsNB:
	python -m webbrowser -t "http://goodreads-notebook.localhost:8001" && docker-compose up goodreads-notebook

formatPythonPY: ## Format the Python files
	ruff format .
	ruff check --fix .

# Open Notebooks
datascrapeNB: ## Open the datascrape notebook in the browser
	$(WEB_BROWSER_CMD) $(DATASCRAPE_URL) && $(DOCKER_COMPOSE_CMD) data-scrape-notebook

goodreadsNB: ## Open the goodreads notebook in the browser
	$(WEB_BROWSER_CMD) $(GOODREADS_URL) && $(DOCKER_COMPOSE_CMD) goodreads-notebook

mnistHandwrittenNB: ## Open the mnist handwritten notebook in the browser
	$(WEB_BROWSER_CMD) $(MNIST_HANDWRITTEN_URL) && $(DOCKER_COMPOSE_CMD) mnist-handwritten-notebook

practicalMLtutNB: ## Open the practical ml tut notebook in the browser
	$(WEB_BROWSER_CMD) $(PRACTICAL_ML_TUT_URL) && $(DOCKER_COMPOSE_CMD) practical-ml-tut-notebook

randomizedOptimization8QueensNB: ## Open the randomized optimization 8 queens notebook in the browser
	$(WEB_BROWSER_CMD) $(RANDOMIZED_OPTIMIZATION_URL) && $(DOCKER_COMPOSE_CMD) randomized-optimization-8-queens-notebook

tfLinearRegressionsNB: ## Open the tf linear regressions notebook in the browser
	$(WEB_BROWSER_CMD) $(TF_LINEAR_REGRESSION_URL) && $(DOCKER_COMPOSE_CMD) tf-linear-regression-notebook

timeseriesAirbnbNB: ## Open the timeseries airbnb notebook in the browser
	$(WEB_BROWSER_CMD) $(TIMESERIES_AIRBNB_URL) && $(DOCKER_COMPOSE_CMD) timeseries_airbnb_nb
