Database
==========

ORM: Object Relational Mapping
-------------------------------

ORM classes are used to map the database to python objects.

.. mermaid::

    classDiagram
        A: +Int id

.. automodule:: templates.database.a
    :members:

Migrations
-----------

To generate a new database migration (new tables, new columns, deletions, updates...), change the ORM classes first. 
Then, generate the new migration using Alembic::

    uv run alembic revision --autogenerate

A new migration will appear in ``src/template/alembic/versions``. Update the file accordingly.

It's possible to decide if migrations are automatically run at startup. Otherwise, use manual updates::

    # Forward
    uv run alembic revision +1
    # Backward
    uv run alembic revision -1
