# SimplePageObjectPattern
Simple object oriented Python scripts based on Pytest + Selenium

Review
------

Simple example of Page Object Pattern (selemium + pytest). No custom helpers included.

Requirements
------------

pytest-selenium==2.0.1
pytest==5.2.2
pytest-base-url==1.4.2
pytest-html==1.14.0
pytest-metadata==1.10.0
pytest-variables==1.9.0
selenium==3.0.2

NOTE: install "pytest-selenium" first, because this package install all pytest module packages but with latest versions, then override other packages

You can use CMD and link requirements.txt:

```bash
pip install -r requirements
```

Download driver
---------------

Download driver that compare to your browser and it's version

How to run tests
----------------

1) Unpack all archive content with main folder
   
2) Unpack execution file from downloaded driver archive in the folder from 1st step or use --driver-path <path\to\driver> if you have it installed in other directory

3) Run CMD, link the directory and trigger python module

```bash
pytest -v --driver <Chrome/Firefox/Etc> --driver-path <path\to\driver>
```

Additional credits
------------------

Pytest configuration file based on @TimurNurlygayanov (https://github.com/TimurNurlygayanov) conftest.py
