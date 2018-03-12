var MongoClient = require('mongodb').MongoClient,
    assert = require('assert');

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
    db.collection('mug_groups').findOne({}, function(err, doc ) {

        // Print the documents returned
        console.log( doc ) ;
        // Close the client
        client.close();
    });



    // Declare success
    console.log("findOne");
});


