# Author : Adrian Shikwambana  
# Project : Database Migration  
Project Instructions https://umuzi-org.github.io/tech-department/projects/python-specific/sqlalchemy-migrations/  
1. git clone the project  
2. create a virtual environment:  
    mkvirtualenv -p $(which python3.7) db_migration
3. Activate the virtual environment:  
    workon db_migration
# Executing the project:  
1. Source the envirnoment variables using the terminal:  
    source env.sh
2. cd into the project and cd into the composition folder to start up postgresql using the docker-compose script:  
    docker-compose up or for installing docker-compose see https://docs.docker.com/compose/install/  
3. run the setup script to enable project modules importing:  
    python setup.py develop
4. Open the project, read the instructions and hapy coding.