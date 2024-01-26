import express from 'express';
import bodyParser from 'body-parser';
import fs from 'fs';
import cors from "cors"

const app = express();
const port = 5003; // default port to listen

const buffer: Uint16Array[] = []

app.use(
  bodyParser.raw({
    // inflate: true,
    type: '*/*'
  })

);

app.use(cors())

// route to handle samples from the ADC - 16 bit single channel samples
app.post('/adc_samples', (req, res) => {
  // tslint:disable-next-line:no-console
  console.log(`Got ${req.body.length} ADC bytes`);
  // buffer.push(req.body)
  fs.appendFile('adc.raw', req.body, () => {
    res.send('OK');
  });
});

// route to handle samples from the I2S microphones - 32 bit stereo channel samples
app.post('/i2s_samples', (req, res) => {
  // tslint:disable-next-line:no-console
  console.log(`Got ${req.body.length} I2S bytes`);
  fs.appendFile('i2s.raw', req.body, () => {
    res.send('OK');
  });
});

app.get("/samples", async(req, res)=>{
  res.send(buffer.shift())
})


// start the Express server
app.listen(port, '0.0.0.0', () => {
  // tslint:disable-next-line:no-console
  console.log(`server started at http://0.0.0.0:${port}`);
});
