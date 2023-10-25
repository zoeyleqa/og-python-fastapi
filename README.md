# Python FastAPI for OG COP
---------------------
* Backend code repository for OG RMT 
* Python FastAPI framework
* Frontend code repository is og-ui
* Re-work of previous simple fastapi app using sqlmodel.

Requirments:
* Python 3.7+
* Pip


Create python virtual enviroment
> py -m venv env


If using VSCode, set Python interpreter path if it doesn't already pickup the virtual env.


Activate enviroment
> .\env\Scripts\activate (Windows)

> pip install -r requirements.dev.txt

Start server
> uvicorn main:app --reload

For VSCode, I've set it up to start on 'F5' command.

OpenAPI(Swagger): http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

![FastAPI doc page](img/Screenshot 2023-10-25 172321.png)
![FastAPI doc page param and response](img/Screenshot 2023-10-25 172409.png)
![FastAPI redoc page](img/Screenshot 2023-10-25 172526.png)
