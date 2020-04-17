# Offline library with books taken from [tululu.org](https://tululu.org/)

This app creates offline library with books taken from [tululu.org](https://tululu.org/).
Bootstrap is used as UI framework.

You can see it on [GitHub Pages](https://esinmy.github.io/books_library_restyle_2/pages/).

### Installation

Before you run this offline library, you need Python 3.x and a few additional libs.  
To install these libs, simply use pip and requirements.txt:
```
pip install -r requirements.txt
```

### How to run

Simply use this command in your terminal:
```
python3 render_website.py
```
By default settings, the offline website will be available 
on your machine via [this link](http://localhost:10000/pages/).

### Environment variables and command line arguments

User can provide host, port and json file (library summary).
There are two ways to do it: environment variables and command line arguments.
**Command line arguments have higher priority than environment variables.**

#### Environment variables
Create `.env` file in the root folder and write variables following this format: `VARIABLE_NAME=value`.
 
Variable names:
- `HOST` — host, e.g. `127.0.0.10`. By default, `localhost`.
- `PORT` — port, e.g. `7007`. By default, `10000`.
- `JSON_FILE` — path to json file, e.g. `C:\my_great_file.json`. By default, `books.json`.
 

#### Command line arguments

Host, port and json file can be set using optional arguments `--host`, `--port` and `--json_path` respectively.  

For example, to run a server on `localhost:5000`:
```
python3 render_website.py --port 5000
```

To read the file `boooooks.json` located in the root:
```
python3 render_website.py --json_file boooooks.json
```

For convenience, shortcuts `-H` instead of `--host`, `-P` instead of `--port` and `-J` instead of `---json_path`.

### Project's goal

The code is written for educational purposes in the online course for web developers [dvmn.org](https://dvmn.org/).