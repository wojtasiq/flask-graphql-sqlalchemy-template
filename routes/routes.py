from flask_graphql import GraphQLView
from services.graphql.schema import schema
import flask_jwt_extended


def init_auth(fn):
    def wrapper(*args, **kwargs):
        flask_jwt_extended.verify_jwt_in_request_optional()
        return fn(*args, **kwargs)

    return wrapper


def graphql_view():
    view = GraphQLView.as_view('graphql', schema=schema, graphiql=True)
    return init_auth(view)


def routes_list(app):
    app.add_url_rule('/graphql', view_func=graphql_view(), methods=['POST', 'GET'])
