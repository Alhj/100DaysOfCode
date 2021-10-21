import { GraphQLNonNull, GraphQLString} from 'graphql'
import articalModel from './Artical.mjs'
import { articalType } from './ArticalType'


const remove = {
  type: articalType,
  args:{
      id: {
        type: new GraphQLNonNull(GraphQLString)
      }
  },
  resolve: async(root, args) => {
    const removeArtical = await articalModel.findByIdAndRemove(args.id, args)
    if(!removeArtical) {
      throw new Error('error')
    }
    return removeArtical
  }
}

export {
  remove
}