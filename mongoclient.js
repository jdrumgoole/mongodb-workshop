
var mongodb = require( "mongodb") ;

var mongoClient = mongodb.MongoClient ;

const url = "mongodb://localhost:27017" ;

mongoClient.connect( url, function( err, client ) {
    if ( err ) {
        console.log( "Failed to connect") ;
        process.exit( 1 )
    } else {
        console.log( "Connected to:", url ) ;
    }

    const adminDB = client.db( "admin")  ;

    adminDB.command( { "isMaster" : 1 }, function( err, res ) {
        if (err ) {
            console.log("isMaster error")
        } else {
            console.log(res);

        }
    })
    client.close() ;
})

