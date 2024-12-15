Fullstack Website Template - Angular Frontend, Python FastAPI Backend
=======================================================================

To use this template, rename all mentions of "template" with the name of your project.

Backend
--------

HTTP Web Backend using the following technologies:

* Python 3.11+
* `Poetry <https://python-poetry.org/>`_ to manage Python Virtual Environment and dependencies.
* `Docker <https://www.docker.com/>`_ to manage deployment in production and database in development.
* `Postgresql <https://www.postgresql.org/>`_ as database choice.
* `SQLAlchemy <https://www.sqlalchemy.org/>`_ as ORM (Object Relational Mapper) library.
* `Alembic <https://alembic.sqlalchemy.org/en/latest/>`_ to manage database migrations.
* `Strawberry <https://strawberry.rocks/>`_ as GraphQL API Framework.
* `FastAPI <https://fastapi.tiangolo.com/>`_ as Asynchronous Web Framework.
* `Uvicorn <https://www.uvicorn.org/>`_ as Asynchronous Web Server.
* `Pytest <https://docs.pytest.org/en/8.0.x/>`_ as Test Framework.
* `Sphinx <https://www.sphinx-doc.org/en/master/>`_ to generate documentation from codebase.

Frontend
---------

Single Page App frontend using the following technologies:

* Angular 19+
* Angular Material

Setup
-------

You first need to create 2 configuration files:

- Create `./docker/docker.env` file with as structure similar to `./docker/docker.example.env`
- Create `./templates-backend/src/settings.ini` file with a structure similar to `./templates-backend/src/settings.example.ini`

If you wish to use docker-postgresql in dev, start it using the .dev compose file::

    cd docker
    docker compose -f docker-compose.dev.yaml --env-file docker.env up
    # Optional, make a backup of production database
    # On server:
    sudo rsync -av --no-perms --delete --chown=$(whoami) ../template_postgres_data/ ~/template_postgres_save
    sudo chown -R $(whoami):$(whoami) ../template_postgres_save
    # On machine:
    sudo rsync -avz --stats --delete $(whoami)@<server>:~/template_postgres_save/ ../template_postgres_data
    # On server:
    sudo rm -rf ~/template_postgres_save

To run the backend, using poetry::

    # Make sure you have poetry
    python -m pip install pipx
    python -m pipx install poetry
    # Install dependencies
    cd templates-backend
    poetry install --with docs,tests
    # Run tests
    cd src
    poetry run pytest
    # Get information about the virtual environment (to setup in your ide)
    poetry env info
    # Run
    cd src
    poetry run python main.py
    # Generate documentation
    cd docs
    poetry run sphinx-build . _build
    # If you want to remove your venv associated
    poetry env remove python

To generate a new database migration, use alembic::

    poetry run alembic revision --autogenerate

Production
------------

If everything is properly setup (configuration files), its only a git pull and restart::

    cd docker
    git pull
    docker compose build
    docker compose down
    docker compose --env-file docker.env up --build -d
