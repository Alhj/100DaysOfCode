import { GraphQLObjectType, GraphQLNonNull } from 'graphql'
import { GraphQLID, GraphQLString } from 'graphql'


const articalType = new GraphQLObjectType({
  name:'Artical',
  fields: () => {
    return {
      id: {
        type: new GraphQLNonNull(GraphQLID),
      },
      title: { type: GraphQLString },
      author: { type: GraphQLString }
    }
  }
})

export default articalType
