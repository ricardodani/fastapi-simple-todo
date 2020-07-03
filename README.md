# fastapi-simple-todo

## Author

Ricardo Lapa Dani @ricardodani

## Introduction

This project was developed for learning purposes only.
It's a full complete TODO List API with documentation, based on Python 3.6+ type hinting system,
FastAPI framework, TortoiseORM and a Relational database (SQLite or PostgreSQL for production).
This project adopts the Clean Architecture priciples, I also tried to apply all good software engineering related to Python good practices and clen code.

## Requirements

* Python 3.6+
* Poetry

## Installation

  ```poetry install --dev```
 
## Testing

  ```pytest app/```
  
## Running

  ```uvicorn app.main:app --reload```

## Technologies used

- Python 3.8
- FastAPI async python web framework
- Tortoise async python ORM
- Pytest test environment
- Poetry python package manager

## Why FASTApi and TortoiseORM ?

As the name suggests, FastAPI is one of the fastest Python Web Frameworks around. It's modern, uses the new Python Typing hinting feature to do validations of data and saves a lot of code.
Also it's perfomance is proven by various benchmarks. By allowing async programming through async/await syntax, I could use a ORM (based in Django) called Tortoise, that is fast and also Asynchronous.

## Clean Architecture

As mentioned, this project was constructed used a very famous code pattern: Clean Architecture.
In this aproach, the responsabilities of each layer are very strict of its particular objectives:

* Endpoints -> API Views that receives parameters, checks it's input validity, authentication, and delegates it to a UseCase classes, that will work with business logic
* UseCases -> Receives validated data from the endpoint views and perform the business logic, doing calculations and acessing resources, then, returning it to the view
* Repositories -> It's a form of resource that communicates with the database, in this project, here we use the TortoiseORM to make operations
* Schemas -> Data classes that are smart enough to make validations and serializations across all of the layers

Respecting this architecture gives the code base a very transparent and consise logic. Without hidden stuff.

## License

Apache 2.0
