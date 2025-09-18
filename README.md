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
python-multipart
"python-jose[cryptography]"

command to generate SECRET_KEY for json
```openssl rand -hex 32


## for postgresSQL dependency
pip3 install psycopg2-binary

### for data migrations
pip3 install alembic
# Sub commands for alembic
    alembic init <folder name>
    alembic revision -m <message>
    alembic upgrade <revision #>
    alembic downgrade -1

# to install pytest
    pip3 install pytest

# Pytest Basics
    Validate integers:
        assert 1==1
        assert 1!=1
        assert 1>1
        assert 1<1
        assert 1>=1
        assert 1>=1
    Validate instances:
        assert isInstance('this is string', str)    # value, type
        assert not isInstance('10', int)
    Validate Boolean:
        assert validate is True
        assert ('hello' == 'welcome') is False
    Validate types:
        assert type('Hello' is str)
        assert type('Hello' is not int)
    Validate Types:
        num_list = [1,2,3,4,5]
        any_list = [True, False]
        assert 1 in num_list
        assert 7 not in num_list
        assert all(num_list)
        assert not any(any_list)

    pytest --disable-warning


pip3 freeze > requirements.txt
pip3 install -r requirements.txt