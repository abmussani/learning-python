# learning-python
Whatever I will gonna learn related to python, will dump it here

'''
python3 -m venv fastapienv

to activate the environment
source fastapienv/bin/activate

to deactivate the environment
deactivate


to install uvicorn and fastapi
pip install "uvicorn[standard]" 
'''


'''
pydantic is used for data validation and settings management using python type annotations
pydantic -> 
    - BaseModel for requests
    - ** to convert from request to concrete python class
        new_book = Book(**book_request.model_dump())
    - Field() for validation
        - min_length
        - max_length
        - gt (greater than)
        - lt (less than)
        - ge (greater than or equal to)
        - le (less than or equal to)
'''

starlette

passlib
bcrypt==4.0.1
