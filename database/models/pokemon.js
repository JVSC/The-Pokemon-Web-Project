var mongoose = require('mongoose'),
    Schema = mongoose.Schema;

var participantSchema= new Schema({
    dexNum: Number,
    name: String,
    slug: String,
    type: [String],
    stats: Schema.Types.Mixed,
    abilities: [Schema.Types.Mixed],
    counters: [Schema.Types.Mixed],
    teammates: [Schema.Types.Mixed],
    sets: [Schema.Types.Mixed],
    items: [Schema.Types.Mixed],
    moves: [Schema.Types.Mixed]
});

var Pokemon = mongoose.model('Pokemon', participantSchema);

module.exports = Pokemon;
