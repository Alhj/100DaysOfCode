import { Schema, model } from "mongoose";


const articalSchema = new Schema({
  title:{
    type: String,
    required: true
  },
  author:{
    type:String,
    require: true
  }
})

const model = model('Artical', articalSchema)

module.exports = model