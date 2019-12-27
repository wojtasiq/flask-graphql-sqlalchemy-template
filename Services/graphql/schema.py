from graphene_sqlalchemy_filter import FilterableConnectionField
import graphene
import services.graphql.schemas.schema_user as schema_user
import services.graphql.schemas.schema_role as schema_role


class Query(graphene.ObjectType):
    """Query objects for GraphQL API."""

    node = graphene.relay.Node.Field()
    user = graphene.relay.Node.Field(schema_user.User)
    users = FilterableConnectionField(schema_user.User, filters=schema_user.UserFilter())
    role = graphene.relay.Node.Field(schema_role.Role)
    roles = FilterableConnectionField(schema_role.Role, filters=schema_role.RoleFilter())


schema = graphene.Schema(query=Query)
