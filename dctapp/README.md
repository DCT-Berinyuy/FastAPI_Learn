### Schema
**A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.**
### Data "schema"
- The term "schema" might also refer to the shape of some data, like a JSON content.

# Recap, step by step
*Step 1: import FastAPI*
- FastAPI is a Python class that provides all the functionality for your API.
# Step 2: create a FastAPI "instance"
- Here the app variable will be an "instance" of the class FastAPI.
- This will be the main point of interaction to create all your API.
# Step 3: create a path operation
- "Path" here refers to the last part of the URL starting from the first /.
# Operation
- "Operation" here refers to one of the HTTP "methods".
POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.

## Path Parameters
- You can declare path "parameters" or "variables" with the same syntax used by Python format strings:
- Path parameters with types
- Data conversion
- Data validation

## Pydantic
- All the data validation is performed under the hood by Pydantic
## Order matters
## Predefined values

## Recap
With FastAPI, by using short, intuitive and standard Python type declarations, you get:

Editor support: error checks, autocompletion, etc.
Data "parsing"
Data validation
API annotation and automatic documentation
And you only have to declare them once.
