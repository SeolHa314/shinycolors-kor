import express from 'express'
import cors from 'cors'
import stringify from 'querystring';

var app = express()

app.use(cors())

app.get('/shinycolors/translate', (req, res, next) => {
    var reqType = req.query('type')
    var filename = "unknown"

    switch(reqType) {
        case "json" :
            var param = req.query("data")
            var jsonData = JSON.parse(param)

            for(var i in jsonData) {
                if("id" in i) {
                    filename = stringify(i['id'])
                    break
                }
            }
            break
        case "url" :
            var param = req.query('data')
            var filename = param.slice(param.lastIndexOf('/') + 1)
            var data = fetch(param).then((response) => {return response.text()})
            var jsonData = JSON.parse(data)
            break
    }

    
})