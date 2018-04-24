# Encymon
Personnal Encyclopedia 

Python 2.7 and mongoDB 3.4

## Memo 

###MongoDB Version 3.4 and earlier : 
https://docs.atlas.mongodb.com/driver-connection/#python-driver-example

### pymongo 3.4.0
If you have something like : 

> pymongo.errors.ConfigurationError: `ssl_cert_reqs` is not ssl.CERT_NONE and no system CA certificates could be loaded. `ssl_ca_certs` is required.

you can go to https://api.mongodb.com/python/current/examples/tls.html to solve your problem. 

##  ./config.database.txt
Something like that : 
>mongodb://kay:myRealPassword@mycluster0-shard-00-00.mongodb.net:27017,mycluster0-shard-00-01.mongodb.net:27017,mycluster0-shard-00-02.mongodb.net:27017/admin?ssl=true&replicaSet=Mycluster0-shard-0&authSource=admin