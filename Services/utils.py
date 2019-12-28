from graphql_relay.node.node import from_global_id


def input_to_dictionary(input):
    """Method to convert Graphene inputs into dictionary"""
    dictionary = {}
    for key in input:
        # Convert GraphQL global id to database id
        if key == 'id':
            input[key] = from_global_id(input[key])
            input[key] = from_global_id(input[key])
        dictionary[key] = input[key]
    return dictionary