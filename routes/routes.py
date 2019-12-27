from flask_graphql import GraphQLView
from services.graphql.schema import schema


def routes_list(app):
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
