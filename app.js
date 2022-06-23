
const http = require("express");
const init_db = require("./db")

const app = express()
const path = ""
const host = 'localhost';
const port = 8000;


app.get("/",(req, res)=>{
    res.sendfile(path.join(__dirname + "/index.html"))
})


app.listen(port, () => {
    console.log("Server is running on http://${host}:${port}");
});

init_db();