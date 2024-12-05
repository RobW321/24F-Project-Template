# `database-files` Folder

TODO: Put some notes here about how this works.  include how to re-bootstrap the db. 

This folder holds all the data as tables that are involved in our NU Track website. 

Using SQL, this page allows us to extract user data from the fake data that we inserted in the NU_Track_database.sql file
We were able to re-bootstrp the db by removing the previous northwind database and editing our .env file to connect to 
our database named nutrack instead.

Now that we are using the nutrack database which contains the fake data that we inserted, we are able to write various
routes in the api folder that pull the requested data from the database. 
