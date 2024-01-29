import fs from "fs"

const SAMPLES = 16384*2; 

const data = fs.readFileSync("adc.raw", {
    encoding: "binary"
})


console.log(data.length)