# fbot
Simple Facebook Bot

# Requirements
* python 3+
* fbchat

# Usage
**Edit ```config.cfg``` file before running**
```
pip install -r requirements.txt
python main.py
```
or
```
docker build -t fbot .
docker run fbot
```

# Generating OpenWeatherMap API Key
* Go to ```https://home.openweathermap.org/api_keys```
* Create an account
* Enter key name and click ```generate```
* Copy your key to ```config.cfg``` file
* Enjoy

# Known issues
* Time inside docker container isn' t synchronized with host
