# scalio

> weight tracking web app that show progression over time

`scalio` is a web app allowing you to keep track of your weight loss project over time. Click [here](https://scalioweb.cfapps.io/register) to create an account and get counting, or look below if you want to run or contribute to the project yourself!

[![Build Status](https://travis-ci.org/chiptopher/scalio.svg?branch=master)](https://travis-ci.org/chiptopher/scalio)

## Getting Started

These instrcutions will get a copy of `scalio` running locally on your machine for developmen, testing, and trial purposes.

### Dependencies
You're going to need these before you get started:
* [python](https://www.python.org/)
* [node.js](https://nodejs.org/en/)

### Building the Application
#### Backend
1. Navigate to the `api/` folder
2. Create a virtual environment with `python3 -m virtaulenv venv`, and activate it with `source venv/bin/activate`
3. Install the dependencies with `pip install -r requirements.txt`
4. Start the api with `python run.py`
#### Frontend
1. Navigate to the `web/` folder
2. Run `npm install`from the terminal to download the dependencies
3. Run `npm start` and then navigate to [localhost:4200](http://localhost:4200) and start using `scalio`.

### Running the Tests
#### Backend
From the `api/` folder, run `python -m unittest discover test` to run all of the api tests.
#### Frontend
From the `web/` folder, run `npm run unit` to run all of the front-end unit tests.

## Contributing
Guidelines for contributions can be found [here](./docs/CONTRIBUTING.md) and our Code of Conduct can be found [here](./docs/CODE_OF_CONDUCT.md). Feel free to 
[open an issue](https://github.com/chiptopher/scalio/issues) if there are problems with **guet** or you want to submit a
feature request.
