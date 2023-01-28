ifeq '$(findstring ;,$(PATH))' ';'
  UNAME := Windows
else
	UNAME := $(shell uname 2>/dev/null || echo Unknown)
	UNAME := $(patsubst CYGWIN%,Cygwin,$(UNAME))
	UNAME := $(patsubst MSYS%,MSYS,$(UNAME))
	UNAME := $(patsubst MINGW%,MSYS,$(UNAME))
endif

PYTHON = /usr/local/bin/python3
PIP = pip3 # pip for Windows 

.PHONY = setup install install-poetry install-brew-packages install-pip-packges run

###################################################################################################################

setup: install-poetry install

install: 
	poetry update

install-poetry:
	curl -sSL https://install.python-poetry.org | python3 -
	# if fail go here to debug https://python-poetry.org/docs/

install-brew-packages:
	brew install tesseract

install-pip-packages: 
	${PIP} install datetime
	${PIP} install requests
	${PIP} install opencv-python
	${PIP} install pytesseract

run:
	poetry run python main.py
