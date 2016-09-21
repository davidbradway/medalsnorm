# Medalsnorm

Maps of 2016 Olympic medals, normalized by various metrics such as GDP and Population

## Try it online now

Select Python 3 kernel

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/davidbradway/medalsnorm)

## Try it on your own machine

- Requirements: `pip install lightning-python pandas numpy jupyter`
- `git clone git@github.com:davidbradway/medalsnorm.git`
- `cd medalsnorm`
- `jupyter notebook`
- Open 'MedalsNorm.ipynb' and run all cells

## Try other financial metrics

- Install Quandl python module `pip install quandl`
- [Get a Quandl API key](https://www.quandl.com/blog/getting-started-with-the-quandl-api "link for API key for Quandl")
- Put that key in your system (not user) environment variables as "QUANDLKEY"
- Look on Quandl website for the URL strings to request other data and adapt the Python code in `medalsnorm.py`
