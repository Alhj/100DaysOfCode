import { GraphQLNonNull, GraphQLString} from 'graphql'
import articalModel from './Artical.mjs'
import { articalType } from './ArticalType'

const uppdateArtical = {
  type:articalType,
  args:{
    id:{
      type: new GraphQLNonNull(GraphQLString)
    },
    title:{
      type: new GraphQLNonNull(GraphQLString)
    },
    author:{
      type: new GraphQLNonNull(GraphQLString)
    }
  },
  resolve: async(root, args) => {
    const updateArtikel = await articalModel.findByIdAndUpdate(args.id, args)
    if(!updateArtikel)
    {
      throw new Error('error')
    }
    return updateArtikel
  }
}

export {
  uppdateArtical
}