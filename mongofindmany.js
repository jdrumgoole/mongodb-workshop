var MongoClient = require('mongodb').MongoClient

var url = 'mongodb://localhost:27017/MUGS';

var cursorPrintURL = function ( err, doc ) {
    if ( err ) {
        throw err;
    } else if (doc) {
        console.log( doc.urlname );
    };
};


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
    cursor = db.collection('mug_groups').find({}) ;

    cursor.each( ( err, doc ) => ( cursorPrintURL( err, doc ))) ;

    // Close the client
    client.close();

    // Declare success
    console.log("Called find()");
});


