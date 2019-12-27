from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterSet
from models.user import ModelRole
import graphene


class RoleAttribute:
    id = graphene.GlobalID(description="Name of the planet.")
    name = graphene.String(description="Name of the planet.")
    label = graphene.String(description="Name of the planet.")


class RoleFilter(FilterSet):
    class Meta:
        model = ModelRole
        fields = {
            'id': [...],
            'name': [...],
            'label': [...],
        }



class Role(SQLAlchemyObjectType, RoleAttribute):
    """People node."""

    class Meta:
        model = ModelRole
        interfaces = (graphene.relay.Node,)
