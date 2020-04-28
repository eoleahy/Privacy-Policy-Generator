# Privacy Policy Generator

4th year Final Year project. This generator creates privacy policies that are embedded with RDFa annotations to make them machine readable. The input is supplied via JSON and is rather strict on layout, so follow the sample file provided.
A live version of this server can be found at https://eoleahy.pythonanywhere.com/.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. Python 3.8 or greater
2. pip

A full list of dependencies are in the [requirements.txt](requirements.txt) file.

### Installing

Install pipenv with:
```
pip install --user pipenv
```

Create a new pipenv virtual environment:
```
pipenv shell
```

When you are in the shell, install dependencies using:
```
pipenv install
```
If the dependencies have succesfully installed, run the server with:
```
python app/app.py
```
Visit the homepage at localhost:5000.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgments

* W3Schools for the accordion.
* Harshvardhan Pandit and Dave Lewis for supervising this project.
