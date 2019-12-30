from graphene_sqlalchemy_filter import FilterableConnectionField
import graphene
import services.graphql.schemas.schema_user as schema_user
import services.graphql.schemas.schema_role as schema_role
import services.graphql.schemas.schema_security as schema_security
import flask_jwt_extended


class Query(graphene.ObjectType):
    """Query objects for GraphQL API."""

    node = graphene.relay.Node.Field()
    user = graphene.relay.Node.Field(schema_user.User)
    users = FilterableConnectionField(schema_user.User, filters=schema_user.UserFilter())
    role = graphene.relay.Node.Field(schema_role.Role)
    roles = FilterableConnectionField(schema_role.Role, filters=schema_role.RoleFilter())

    def resolve_user(self, info):
        flask_jwt_extended.verify_jwt_in_request_optional()
        user = flask_jwt_extended.get_jwt_identity()
        # user = flask_jwt_extended.current_user()
        print(user)
        if user is None:
            return []
        query = schema_user.User.get_query(info)  # SQLAlchemy query
        return query.all()


class Mutation(graphene.ObjectType):
    updateUser = schema_user.UpdateUser.Field()
    login = schema_security.Login.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
