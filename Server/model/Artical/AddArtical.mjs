import { GraphQLNonNull, GraphQLString} from 'graphql'
import articalModel from './Artical.mjs'
import { articalType } from './ArticalType'

const addArtical = {
  type: articalType,
  args: {
    title: {
      type: new GraphQLNonNull(GraphQLString)
    },
    author: {
      type: new GraphQLNonNull(GraphQLString)
    }
  },
  resolve: async(root, args) => {
    const uModel = new articalModel(args)
    const newArtical = await uModel.save()
    if(!newArtical)
    {
      throw new Error('error')
    }
    return newArtical
  }
}

export {
  addArtical
}