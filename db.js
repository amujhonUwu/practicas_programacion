const mongose = require("mongose")
const DB_URL = "mongodb://localhost:2701/"

module.exports = ()=>{
    const connect = ()=>{
        mongose.connect(
            DB_URL,{
                keepAlive:true,
                useNewUrlParser:true,
                useUnifiedTopology:true,
            },
            (err) => {
                if (err){
                    console.log('DB: Error de conexión.')
                }
                else{
                    console.log('DB: Conexión satisfactoria.')
                }
            }
        )
    }
    connect();
}