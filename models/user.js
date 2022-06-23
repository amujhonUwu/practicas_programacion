const mongose = requiere("mongose");
const UserScheme = new mongose.Schema(
    {
        _id:{ 
            type:Bigint 
        },
        nombre:{
            type:String
        },
        apellido:{
            type:String
        },
        edad:{
            type:Bigint
        }
    }
);

module.export = mongose.model("/models/user.js", UserScheme);