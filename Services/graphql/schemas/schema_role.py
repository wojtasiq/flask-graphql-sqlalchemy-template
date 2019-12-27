from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterSet, FilterableConnectionField
from models.user import ModelRole, ModelUser
from services.graphql.schemas.schema_user import UserFilter
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


class RoleNestedFilters(FilterableConnectionField):
    filters = {
        ModelUser: UserFilter(),
    }


class Role(SQLAlchemyObjectType, RoleAttribute):
    """People node."""

    class Meta:
        model = ModelRole
        interfaces = (graphene.relay.Node,)
        connection_field_factory = RoleNestedFilters.factory
