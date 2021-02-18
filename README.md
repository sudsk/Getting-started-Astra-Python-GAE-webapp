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
# Bulk load to books_by_isbn table
~/dsbulk-1.7.0$ bin/dsbulk load -url books.csv -k killrvideo -t books_by_isbn -b "secure-connect-killrvideocluster.zip" -u <user> -p <password> -header true

# Bulk load to books_by_category table
~/dsbulk-1.7.0$ bin/dsbulk load -url books.csv -k killrvideo -t books_by_category -b "secure-connect-killrvideocluster.zip" -u <user> -p <password> -header true
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

