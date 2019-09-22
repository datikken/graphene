import graphene
import json

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return 'World'

schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        hello
    }
    '''
)

dictResult = dict(result.data.items())
some = json.dumps(dictResult, indent=2)
print(some)