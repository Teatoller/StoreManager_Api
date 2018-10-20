Project Title
# StoreManager_Api
Brief Description

API endpoints for Store Manager APP
Badges:
[![Build Status](https://travis-ci.org/Teatoller/StoreManager_Api.svg?branch=ft-Add-login-Authentification-161336680)](https://travis-ci.org/Teatoller/StoreManager_Api) [![Coverage Status](https://coveralls.io/repos/github/Teatoller/StoreManager_Api/badge.svg?branch=ft-Add-login-Authentification-161336680)](https://coveralls.io/github/Teatoller/StoreManager_Api?branch=ft-Add-login-Authentification-161336680) [![Maintainability](https://api.codeclimate.com/v1/badges/4f1085444fc1a8c3122e/maintainability)](https://codeclimate.com/github/Teatoller/StoreManager_Api/maintainability)
#### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

Installation
The development version can be downloaded from its page at GitHub.

#### Create a project folder and a env folder within:

$ mkdir myproject
$ cd myproject
$ python3 -m venv env

$ git clone https://github.com/Teatoller/StoreManager_Api
$ cd StoreManager_Api

$ export FLASK_APP=run.py
$ flask run

* Running on http://127.0.0.1:5000/

### Prerequisites
What things you need to install

$ pip Install Flask
$ pip install flask-restful
$ pip instal flask-jwt-extended
$ pytest --cov-report term-missing --cov=app

A step by step series of examples that tell you how to get a development env running

1. Open postman
2  Copy the link 'http://127.0.0.1:5000/' below the terminal when $ 'flask run'.
3. Add endpoint after the .5000/*****

Example 

a. In Postman in the field adjacent tp "PARAM" ENTER 'http://127.0.0.1:5000/product'

b. In body area on server side use this is the format;

{
	"name": "Nescafe"
	"price": 15
	"quantity": 1
	"category": "Beverage"
}

c. The product will display on the browser side of Postman.

d .Try and different product items.
e. Now, change the;

i. POST TO GET 
ii. Change route to 'http://127.0.0.1:5000/products' and then send. 

iii. You should see returned all the products you posted.

NB. Ensure the content-header JSON(application/json)

This are the endpoint routes you may want to try:

#### Fetch all products
GET /products

#### Get all available products.
GET /products

#### Fetch a single product record
Get a specific product using the product’s id.
GET /<productId>

Fetch all sale records
GET /sales

Get all sale records. This endpoint eill eventually be accessible to only the store owner/admin.
GET /sales

GET /sales/<saleId>
Fetch a single sale record

Get a specific sale record using the sale record Id. This endpoint will eventually be accessible only to the store owner/admin and the creator (store attendant) of the specific sale record.

POST /products

Create a product
Create a new product record. This endpoint will eventually be accessible only to the store owner/admin.

POST /sales
Create a sale order

Create a sale record. This endpoint is accessible to only the store attendant.

Versioning
This is v1 built with Flask restful

Authors
Steven Ennis as part of fulfilment in Andela Pre-Bootcamp.