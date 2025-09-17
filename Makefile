# simple makefile to simplify repetetive build env management tasks under posix
CTAGS ?= ctags

all: clean test

clean-pyc:
	@find . -name "*.pyc" | xargs rm -f

clean-so:
	@find . -name "*.so" | xargs rm -f
	@find . -name "*.pyd" | xargs rm -f

clean-build:
	@rm -rf build

clean-ctags:
	@rm -f tags

clean-cache:
	@find . -name "__pycache__" | xargs rm -rf

clean: clean-build clean-pyc clean-so clean-ctags clean-cache
	@echo "Cleaning build, pyc, so, ctags, and cache"

clean-test: clean-build clean-pyc clean-ctags clean-cache
	@echo "Cleaning build, pyc, ctags, and cache"

test: clean-test
	@python -m pytest --cov=visbrain --cov-report=term-missing

test-html: clean-test
	@python -m pytest --cov=visbrain --cov-report=html --showlocals --durations=10 --html=report.html --self-contained-html

flake: clean-test
	@ruff check .

examples: clean
	@for i in examples/brain/*.py examples/objects/*.py;do \
		echo "-----------------------------------------------"; \
		echo $$i; \
		echo "-----------------------------------------------"; \
		python $$i --visbrain-show=False; \
		echo "\n"; \
	done

examples-full: clean
	@for i in examples/*/*.py; do \
		echo "-----------------------------------------------"; \
		echo $$i; \
		echo "-----------------------------------------------"; \
		python $$i --visbrain-show=False; \
		echo "\n"; \
	done

pypi: build_dist
	@twine upload --verbose dist/*


# clean dist
clean_dist:
	@rm -rf build/
	@rm -rf visbrain.egg-info/
	@rm -rf dist/
	@echo "Dist cleaned"

# build dist
build_dist: clean_dist
	python -m build
	@echo "Dist built"

# check distribution
check_dist:
	twine check dist/*

# upload distribution
upload_dist: build_dist
	twine upload --verbose dist/*
