var MongoClient = require('mongodb').MongoClient

var url = 'mongodb://localhost:27017/MUGS';

MongoClient.connect(url, function(err, client) {

    if ( err ) {
        console.log( err );
        process.exit( 1 ) ;
    } else {
        console.log("Successfully connected to server: ", url );
    }

    //console.log( db ) ;
    // Find some documents in our collection

    db = client.db( "MUGS" ) ;
    db.collection('mug_groups').aggregate(
            [
                { $group : { _id : { country : "$country" }, cnt : { $sum : 1 } } },
                { $sort : { cnt : -1 } },
                { $limit : 5 }
            ]
    ).toArray( function( err, docs ) {

        if ( err ) {
            console.log( err );
        } else {
            for ( var i = 0; i < docs.length; i++)
            {
                console.log(docs[i]._id.country + " : " + docs[i].cnt)
            }
        }

        // Close the client
            client.close();
        })

    // Declare success
    console.log("aggregate");
});


