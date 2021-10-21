import {GraphQLObjectType, GraphQLList} from 'graphql'
import articalModel from './Artical.mjs'
import { articalType } from './ArticalType'

const articalQuery = new GraphQLObjectType({
  name:'articalQuery',
  fields: () => {
    return {
      Articals: {
        type: new GraphQLList(articalType),
        resolve: async ()=> {
          const articals = await articalModel.find()
          if(!articals)
          {
            throw new Error('error while fetching data')
          }
          return articals
        }
      }
    }
  }
})


export{
  articalQuery
}
