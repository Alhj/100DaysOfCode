import {GraphQLSchema, GraphQLObjectType} from 'graphql'
import { articalQuery } from './articalQuery'
import { addArtical, uppdateArtical, remove } from './ArticalMutation'

const bookSchema = new GraphQLSchema({
  query: articalQuery,
  mutation: new GraphQLObjectType({
    name: 'Mutation',
    fields: {
      addArtical,
      uppdateArtical,
      remove
    }
  })
})

export {
  bookSchema
}