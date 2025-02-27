const mongoose = require('mongoose')

const Equity_research_analyst_Schema = new mongoose.Schema({
    name: String,
    email: String,
    password: String
})

const Equity_research_analyst_Model = mongoose.model("equity_research_analyst",Equity_research_analyst_Schema)
module.exports = Equity_research_analyst_Model