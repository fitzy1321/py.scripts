#!/usr/bin/env python3

# Code from https://graphql.org/code/#python

import graphene
from graphene.types import schema


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name


schema = graphene.Schema(query=Query)
result = schema.execute('{ hello }')
print(result.data['hello'])  # 'Hello World'
