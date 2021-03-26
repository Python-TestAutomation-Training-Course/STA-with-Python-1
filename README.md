# STA-with-Python-1
Lectures and homeworks

Lectures are located in slides folders (Jupyter notebook and html file)
Homeworks are in homeworks folders

Install the last version of Python

To run jupyter notebook:
- Create a virtual environment
- Install dependencies from requirements.txt with command `pip install -r requirements.txt`
- Run ```jupyter notebook```

Also lecture slide is available in html file.

## Code Style
<a href="https://pre-commit.com/">pre-commit</a>  
Install pre-commit to your project's virtual environment
```sh
pip install pre-commit
```

Copy ```.pre-commit-config.yaml```, check that it works with 
```sh
pre-commit run --all-files
```
To run it automatically on every commit, execute
```sh
pre-commit install
```
With current configuration pre-commit won't change any files, it will only report ones with problems. It uses two tools:
- <a href="https://github.com/psf/black">black</a> - code formatter for python
- <a href="https://pycqa.github.io/isort/">isort</a> - a utility that sorts imports in py files

The idea is that all of your code must pass:
```sh
isort --profile black --check . && black --check .
```
You can change yaml config to make black and isort fix your code if needed, example of a command that fixes all errors:
```sh
isort --profile black . && black .
```
(you'll have to install isort and black with ```pip``` first)