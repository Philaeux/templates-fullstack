FastAPI
========

GraphQL
--------

Schema
^^^^^^^

Schema defined for the GraphQL endpoint:

.. automodule:: templates.graphql.schema
    :members:

Types Input & Output
^^^^^^^^^^^^^^^^^^^^^^

Generic api types:

.. automodule:: templates.graphql.types.generic
    :members:


Generated Types
^^^^^^^^^^^^^^^^

These types are generated from ORM objects. When a query/mutation return an ORM type, it's automatically turned into a GraphQL type.

.. automodule:: templates.graphql.types.generated
    :members:

REST API
----------

It is possible to create classic REST endpoints instead of using the GraphQL endpoint. A demonstration function is the hello_world.

I recommend using REST for the OAuth process, using 2 functions ``oauth_login`` and ``oauth_callback`` per provider (Google, Reddit...).
