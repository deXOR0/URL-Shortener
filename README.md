<br/>
<p align="center">
  <h3 align="center">URL Shortener</h3>

  <p align="center">
    <a href="https://www.awesa.xyz/">Visit URL Shortener</a>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=Flask&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57.svg?style=for-the-badge&logo=SQLite&logoColor=white" />
  <img src="https://img.shields.io/badge/Jinja-B41717.svg?style=for-the-badge&logo=Jinja&logoColor=white" />
  <img src="https://img.shields.io/badge/Bootstrap-7952B3.svg?style=for-the-badge&logo=Bootstrap&logoColor=white" />
</p>

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](https://media.discordapp.net/attachments/846612997836505088/1072945697621549126/image.png?width=1202&height=676)

A simple URL Shortener with auto-generated and custom-made slug options. Supports password protection on shorted url.

## Built With

URL Shortener is built using Python and the Flask framework. The template I'm using here is taken from the [Flask-CS](https://github.com/deXOR0/Flask-CS) starter template.

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [SQLite](https://www.sqlite.org/index.html)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
* [bcrypt](https://pypi.org/project/bcrypt/)

## Getting Started

To get started, clone this repository through your favorite Git client, or by using 
```
git clone https://github.com/deXOR0/URL-Shortener.git
```

### Prerequisites

Make sure you have these set up before you run the application
* Python 3.9.x
* pip
* venv

### Installation

1. Create a virtual environment inside the project's directory
    ```
    python -m venv venv
    ```

2. Activate the virtual environment
   ```
   source venv/bin/activate
   ```
   For Windows users
   ```
   . venv\Scripts\activate
   ```

3. Install the dependencies
   ```
   python -m pip install -r requirements.txt
   ```

## Usage

To run the application you can start a local server with hot reloading enter the command
```
python run.py runserver --debug
```

## License

Distributed under the MIT License. See [LICENSE](https://github.com/deXOR0/URL-Shortener/blob/main/LICENSE.md) for more information.

## Authors

* **Atyanta Awesa Pambharu** - *Full-Stack Developer* - [Atyanta Awesa Pambharu](https://github.com/deXOR0/) - *Built the front end and back end of the application*

## Acknowledgements

* [CodingGarden](https://github.com/CodingGarden/miniature-umbrella)
* [Corey Schaffer](https://www.youtube.com/watch?v=44PvX0Yv368&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=5)
