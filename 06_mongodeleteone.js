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

    db = client.db( "test" ) ;
    db.collection('test').deleteOne({ "hello" : "World!"}, function(err, res ) {

        if ( err ) {
            console.log( err ) ;
            process.exit( 1 )
        } else {
            console.log( `deleted ${ res.deletedCount } document` ) ;;
        }
        // Close the client
        client.close();
    });
    console.log( "deleteOne") ;



    // Declare success
    console.log("Called deleteOne()");
});


