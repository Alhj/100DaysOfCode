import Mongoose from "mongoose";
const Schema = Mongoose.Schema;

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

const model = Mongoose.model('Artical', articalSchema)

export default model