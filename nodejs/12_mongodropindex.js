
var mongodb = require( "mongodb") ;

var mongoClient = mongodb.MongoClient ;

const url = "mongodb://localhost:27017/MUGS" ;

mongoClient.connect( url, function( err, client ) {
    if ( err ) {
        console.log( "Failed to connect to :", url ) ;
        process.exit( 1 )
    } else {
        console.log( "Connected to:", url ) ;
    }

    const db = client.db( "MUGS")  ;
    ;
    db.collection('mug_groups').dropIndex( { "urlname" : 1 }, function( err, res ) {
        if ( err ) {
            throw err ;
        } else {
            console.log( res );
        }
        client.close() ;
    });
    console.log( "dropIndex") ;

})

