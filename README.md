## Notes

Many projects are using the same mysql client and using a default database name 'littlelemon' with different tables, when running on local dev environment sometimes the migrations may fail or unable to detect newly added tables.
If no migrations are made when starting a new course, try to drop the 'littlelemon' database and create a new one in mysql, then make migrations again.
