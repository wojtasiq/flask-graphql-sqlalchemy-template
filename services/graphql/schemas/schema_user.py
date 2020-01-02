from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy_filter import FilterSet
from models.user import ModelUser
from services.database import db
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

    @classmethod
    def get_node(cls, info, id):
        return cls.get_query(info).filter(
            cls._meta.model.id == id
        ).first()


class UpdateUserInput(graphene.InputObjectType, UserAttribute):
    """Arguments to update a User."""


class UpdateUser(graphene.Mutation):
    """Update a person."""
    user = graphene.Field(lambda: User, description="User updated by this mutation.")

    class Arguments:
        userData = UpdateUserInput(required=True)

    def mutate(self, info, userData):
        user = db.session.query(ModelUser).get(userData['id'])
        for key, value in userData.items():
            if key != 'id':
                user.__setattr__(key, value)
        db.session.commit()
        user = db.session.query(ModelUser).get(userData['id'])

        return UpdateUser(user=user)
