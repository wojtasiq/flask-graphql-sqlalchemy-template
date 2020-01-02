import graphene
import flask_jwt_extended
from models.user import ModelUser, ModelRole
from services.database import db
from argon2 import PasswordHasher, exceptions


class Login(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()
    refresh_token = graphene.String()
    ok=graphene.Boolean()

    def mutate(self, info, password, email):

        user = ModelUser.query.filter_by(email=email).first()
        if user:
            ph = PasswordHasher()
            try:
                correct_pass = ph.verify(user.password, password)
            except exceptions.VerifyMismatchError:
                return Login(ok=False)

            if correct_pass:
                token = flask_jwt_extended.create_access_token(identity=user.email)
                refresh_token = flask_jwt_extended.create_refresh_token(identity=user.email)

                return Login(token=token, refresh_token=refresh_token, ok=True)

        return Login(ok=False)


class Register(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, password, email):
        user = ModelUser.query.filter_by(email=email).first()

        if user:
            return Register(ok=False)

        user = ModelUser()
        user.email = email
        ph = PasswordHasher()
        user.password = ph.hash(password)
        user.roles.append(ModelRole.query.filter_by(name='user').first())

        db.session.add(user)
        db.session.commit()

        return Register(ok=True)
