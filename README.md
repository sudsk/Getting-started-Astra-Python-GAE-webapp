# Getting started with Datastax Astra, Google App Engine, and Python drivers

This project is designed to learn Datastax Astra in a fun way.

In this project we build a web application called “Bookshelf” displaying books of different categories. The application allows CRUD operations on the books. 

Public dataset used: [Kaggle Book Covers dataset](https://www.kaggle.com/lukaanicin/book-covers-dataset)

Contributors: A listing of contributors to this repository linked to their github profile:
* [Suds Kumar](https://github.com/sudsk)

## Objectives
To demonstrate how to integrate Google App Engine application with Datastax Astra using Python drivers
  
## Project Layout
* main.py - The main application file which contains all the logic for the web application
* storage.py - Google cloud storage client application
* astra.py - Datastax Astra client application
* app.yaml - Google App Engine config
* requirements.txt - Python libraries required
* templates/form.html - Create a book form 
* templates/view.html - View a book 
* templates/list.html - Listing of books
* templates/base.html - Base html file

## How this Works
A description of how this sample works and how it demonstrates the objectives outlined above

## Setup and Running

### Prerequisites
* Datastax Astra
* Google Cloud Storage
* Google App Engine
* Python 3.7
* Datastax bulk loader

### Initial bulk load
```
~/dsbulk-1.7.0$ bin/dsbulk load -url Art-Photography.csv -k killrvideo -t books_by_isbn -b "secure-connect-killrvideocluster.zip" -u <user> -p <password> -header true
Username and password provided but auth provider not specified, inferring PlainTextAuthProvider
A cloud secure connect bundle was provided: ignoring all explicit contact points.
A cloud secure connect bundle was provided and selected operation performs writes: changing default consistency level to LOCAL_QUORUM.
Operation directory: ~/dsbulk-1.7.0/logs/LOAD_20210217-105956-433941
total | failed | rows/s | p50ms |  p99ms | p999ms | batches
  982 |      0 |    418 | 61.23 | 130.02 | 152.04 |    2.12
Operation LOAD_20210217-105956-433941 completed successfully in 1 second.
Last processed positions can be found in positions.txt
```
### Running Webapp providing CRUD operations
To run this application use the following command:

`python3 main.py`

This will produce the following output:

```
* Serving Flask app "main" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
INFO:werkzeug: * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

