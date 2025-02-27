const express = require("express")
const mongoose = require('mongoose')
const cors = require("cors")
const Equity_research_analyst_Model = require('./model/Equity_research_analyst')

const app = express()
app.use(express.json())
app.use(cors())

mongoose.connect("mongodb+srv://JeevaHaritha:jeevaharitha2020@harithajeeva.y4kv6.mongodb.net/Equity_research_analyst");

app.post('/login', (req,res) => {
    const {email,password} = req.body;
    Equity_research_analyst_Model.findOne({email: email})
    .then(user => {
        if(user){
            if(user.password === password){
                res.json("Success")
            }
            else{
                res.json("The password is incorrect")
            }
        }
        else{
            res.json("No record exists")
        }
    })
})

app.post('/register',(req,res) => {
    Equity_research_analyst_Model.create(req.body)
    .then(auth => res.json(auth))
    .catch(err => res.json(err))
})

app.listen(3001,() => {
    console.log("Server Connected")
})