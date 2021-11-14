# Project: AirBnB clone
The goal of the project is to deploy on your server a simple copy of
the AirBnB website. Which is basically a clone of AirBnB.

we won’t implement all the features, only some of them to cover all
fundamental concepts of the higher level programming track.

## complete web application composed by:

- A command interpreter to manipulate and control data without a visual
interface, like in a Shell(perfect for development and debugging)
- A website(the front-end) that shows the final product to everybody:
    static and dynamic
- A database or files that store data(data=objects)
- An API that provides a communication interface between the front-end
and your data(retrieve, create, delete, update them)
## Files and Directories
- repr(models) directory will contain all classes used for the entire
project. A class, called “model” in a OOP project is the representation
of an object/instance.
- repr(tests) directory will contain all unit tests.
- repr(console.py) file is the entry point of our command interpreter.
- repr(models/base_model.py) file is the base class of all our models.
It contains common elements:
    - attributes: repr(id, created_at) and repr(updated_at)
    - methods: repr(save()) and repr(to_json())
- repr(models/engine) directory will contain all storage classes
(using the same prototype). For the moment you will have only
one: repr(file_storage.py.)
