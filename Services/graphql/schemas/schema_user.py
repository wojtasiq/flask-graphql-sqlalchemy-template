from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterSet
from models.user import ModelUser
import graphene


class UserAttribute:
    id = graphene.GlobalID(description="Name of the person.")
    email = graphene.String(description="Name of the person.")
    password = graphene.String(description="Name of the person.")


class UserFilter(FilterSet):
    class Meta:
        model = ModelUser
        fields = {
            'id': [...],
            'email': [...],
        }


class User(SQLAlchemyObjectType, UserAttribute):
    """People node."""

    class Meta:
        model = ModelUser
        interfaces = (graphene.relay.Node,)
