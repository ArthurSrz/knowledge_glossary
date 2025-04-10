---
facet of:
  - "[[exception handling]]"
  - "[[database application]]"
instance of: "[[change]]"
wikidata entity id: Q395307
---
In [database](https://en.wikipedia.org/wiki/Database "Database") technologies, a **rollback** is an operation which returns the database to some previous state. Rollbacks are important for database [integrity](https://en.wikipedia.org/wiki/Data_integrity "Data integrity"), because they mean that the database can be restored to a clean copy even after erroneous operations are performed.[[1]](https://en.wikipedia.org/wiki/Rollback_\(data_management\)#cite_note-1) They are crucial for recovering from database server crashes; by rolling back any [transaction](https://en.wikipedia.org/wiki/Database_transaction "Database transaction") which was active at the time of the crash, the database is restored to a consistent state.

The rollback feature is usually implemented with a [transaction log](https://en.wikipedia.org/wiki/Database_log "Database log"), but can also be implemented via [multiversion concurrency control](https://en.wikipedia.org/wiki/Multiversion_concurrency_control "Multiversion concurrency control").