## This is a basic Fastapi project for my task in the HNG12 Internship

#### Aim
- The aim of the project is to build a basic api endpoint that accepts a get request and returns the following:
    - email
    - current_datetime
    - github_url

### Steps on running the project
- To Run the project, kindly follow the instructions:
    - Fork and clone the [Github Repo](https://github.com/Kingsley-Opara/hng11_stage0)
    - ```
            cd ./stage0
        ```
    - Create a virtual environment by using the command:
        - ```py
                python -m venv venv
            ```
    - Activate the virtual environment using the command:
        - windows:
            - ```
                    ./venv/scripts/activate
                ```
        - for mac and linux users:
            ```
                ./venv/bin/activate
        
            ```
    - Install all the dependencies used for the project using the command
        - ```py
                pip install -r requirements.txt
            ```
    - To run the project:
        - ```py
                uvicorn app.main:app --reload
            ```
        