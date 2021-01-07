# Keyboard typer
## Description
Program for bypassing <b>ATF - psaní všemi deseti</b> program. It may also work for other programs, but it hasn't been tested. Text is written in random time from 50 - 100ms per letter. These values can be changed in `config.json` file.

## Setup
- download and install Python 3 from https://www.python.org/downloads/
- open cmd or Terminal (Linux)
- install `pynput` library by typing `pip install pynput`
- after that navigate to root of this project and run `app.py` by typing `python3 app.py`

## Usage
- `config.json` - configuration file where you can configure min and max typing speed <span style="color:red">in miliseconds</span>
- `text.txt`    - this file contains text which you want to be typed <span style="color:red">(WARNING, SPACES ARE ALSO TYPED)</span>
- `app.py`      - program file, login part of this project

------------------------------------------------------------------------

# CZ version
## Popis
- Program pro obcházení programu <b>ATF - psaní všemi deseti</b>. Může fungovat také pro jiné programy, nicméně tahle kompabilita není garantovaná. Text je psán rychlostí 50 - 100ms za sekundu. Tyto hodnoty mohou být překonfigurovány v `config.json` souboru.

## Prvotní spuštění
- stáhněte si a nainstalujte Python 3 překladač z https://www.python.org/downloads/
- otevřete si příkazový řádek nebo Terminal (Linux)
- nainstalujte si knihovnu `pynput` spuštěním příkazu `pip install pynput`
- poté běžte do kořenového adresáře projektu
- spusťte program spuštěním příkazu `python3 app.py`

## Nastavení
- `config.json` - konfigurační soubor ve kterém se nastavuje minimální a maximální rychlost psaní <span style="color:red">v milisekundách</span>
- `text.txt`    - sem napiště co chcete aby program napsal za text <span style="color:red">(POZOR NA MEZERY, TY PÍŠE TAKY)</span>
- `app.py`      - soubor, ve kterém je logika celého projektu
