const mongoose = require("mongoose");

const EquityResearchAnalystSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true },
    password: { type: String, required: true }
});

const EquityResearchAnalyst = mongoose.model("equity_research_analyst", EquityResearchAnalystSchema);
module.exports = EquityResearchAnalyst;
