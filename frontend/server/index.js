const express = require('express')
const path = require('path')
const app = express()
const port = 3000

app.use(express.static(path.join(__dirname, '../dis')))
app.use(express.json())

app.listen(port, () => {
  console.log(`Zodiac listening at http://localhost:${port}`)
})