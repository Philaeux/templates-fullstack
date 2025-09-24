from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

# ORM MAPPING
strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()

# How to add an orm mapping to strawberry type
from templates.database.a import A


@strawberry_sqlalchemy_mapper.type(A)
class AGql:
    pass
