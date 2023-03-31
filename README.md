# Longest Common Substring (LCS) Server

This is a web application that finds the longest common substring (LCS) of a set of input strings. It is built with Python, and uses the Django Rest Framework to create a RESTful API for the LCS calculation.

# Installation

To run this app, you need to have Docker and Docker Compose installed on your machine following [this guide](https://docs.docker.com/engine/install/). Once you have those, follow these steps:

#### 1. Clone the repository:
    $ git clone https://github.com/jtsai3/LCS-server.git

#### 2. Change into the app directory containing `docker-compose.yaml`
#### 3. Build and run the Docker image: 
    $ docker compose up --build

This will start the app and you should be able to access it by visiting http://localhost:8000/lcs in your web browser.


# Usage

To use the app, follow these steps:

#### 1. Visit http://localhost:8000/lcs in your web browser.

#### 2. Enter a set of strings in the "Content" input field.

#### 3. Click the "Post" button.

#### 4. The app will return the longest common substrings of the set of strings.


# API Endpoints

The following API endpoint is available:

* `/lcs`: POST request that accepts a JSON object containing a set of strings and returns the LCS result.
Example request:

    ```
    POST /lcs HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json

    {
        "setOfStrings": [
            {"value": "comcast"},
            {"value": "communicate"},
            {"value": "commutation"}
        ]
    }

    ```
    Example response:
    ```
    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "lcs": [
            {
                "value": "com"
            }
        ]
    }
    ```
# Tests
To run the tests for this application, follow these steps:

#### 1. Make sure the Docker containers are running by running the command `docker compose up` in the root directory of the project.
#### 2. Open a new terminal window and navigate to the root directory of the project.
#### 3. Run the following command to run the tests:
```
$ docker exec -it lcs-server python manage.py test
```
#### 4. After the tests have completed, you should see a summary of the test results in your terminal.

# Acknowledgments
* This app was built as part of a coding exercise.

