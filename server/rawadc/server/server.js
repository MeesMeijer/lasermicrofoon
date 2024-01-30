const {createServer} = require("http")
const express = require("express")
const app = express()
const server = createServer(app)
const { Server } = require("socket.io")
const ws = new Server(server, {
    cors: {
      origin: "*"
    },
  });
const fs = require('fs')

const cors = require("cors")
const { v4 } = require("uuid");

const path = require("path")

const FILES_DIR =  "./files/"
const RECORDING_DIR = './files/recording/'


var recoding = false 


app.use(
    express.raw({
      // inflate: true,
      type: '*/*'
    })
);

app.use(cors())

app.all("*", (req, res, next)=>{
    const date = new Date().toLocaleTimeString(["nl-NL"], {
        hourCycle: "h24", hour: '2-digit', minute: "2-digit"
    })
    console.log(`[${req.method}] ${date} - ${req.originalUrl} with length: ${req.body.length}`)
    next()
})

app.route("/")
.get(async(req,res)=>{
    return res.render("index.ejs")
})

app.route("/adc_samples")
.post(async(req,res)=>{
    console.log(`Got ${req.body.length} samples.`)

    const connectedSockets = await ws.fetchSockets()
    if (connectedSockets.length > 0){
        ws.emit("LIVE_CHUNK", req.body)
    }

    fs.appendFile('adc.raw', req.body, () => {
        res.send('OK');
    });
})


ws.on("connection", (socket) => {
    console.log(socket.id); // ojIckSD2jqNzOqIrAGzL

    // chuck {id, uuid}
    socket.on("GET_CHUNK", async(chuck)=>{

    })

    socket.on("START_RECORDING", async()=>{
        
    })
    
    socket.on("disconnect", (reason) => {
        console.log("disconnect", reason)

        // stop the recording and save it. 
    });
});
  

server.listen(5003, "192.168.2.7", ()=>{
    console.log("http://192.168.2.7:5003")
})