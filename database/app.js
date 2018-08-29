var     mongoose    = require('mongoose'),   
        Pokemon     = require('./models/pokemon'),
        data        = require('../data/extract');
        
mongoose.connect('mongodb://jota:skylane07@ds133622.mlab.com:33622/sitedex', { useNewUrlParser: true })

data.forEach(pkmn => {
    Pokemon.create(pkmn, (err, saved)=>{
        if (err)
            console.log(err)
    })
})



