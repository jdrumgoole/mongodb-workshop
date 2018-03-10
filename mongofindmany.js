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
    db.collection('mug_groups').find({}).toArray( function( err, docs ) {

    if ( err ) {
        console.log( err );
        process.exit( 1 ) ;
    } else {
        for ( var i = 0; i < docs.length; i++)
        {
            console.log(docs[i].urlname)
        }
    }

    // Close the client
        client.close();
    })

    // Declare success
    console.log("Called find()");
});


