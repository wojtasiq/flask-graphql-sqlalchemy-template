import graphene
import flask_jwt_extended


class Login(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()
    refresh_token = graphene.String()

    def mutate(self, info, password, username):
        token = flask_jwt_extended.create_access_token(identity='wojtasiq')
        refresh_token = flask_jwt_extended.create_refresh_token(identity='wojtasiq')

        return Login(token=token, refresh_token=refresh_token)


# class RefreshMutation(graphene.Mutation):
#     class Arguments(object):
#         refresh_token = graphene.String()
#
#     result = graphene.Field(RefreshUnion)
#
#     @mutation_jwt_refresh_token_required
#     def mutate(self, info, refresh_token):
#         return RefreshMutation(
#             RefreshField(acces_token=create_access_token(get_jwt_identity()), message="Refresh success"))
#
#
# class RegisterMutation(graphene.Mutation):
#     class Arguments(object):
#         id = graphene.String()
#         username = graphene.String()
#         password = graphene.String()
#         description = graphene.String()
#
#     result = graphene.Field(ResponseMessageField)
#
#     @staticmethod
#     def mutate(root, info, **kwargs):
#         AccountModel(**kwargs).save()
#
#         return RegisterMutation(ResponseMessageField(is_success=True, message="Successfully registered"))
