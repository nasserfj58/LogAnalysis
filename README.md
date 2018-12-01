
# Log Analysis Project

This repo contai 2 files, in the queriesresults you will find 
the result of the execution of the requested queries, in the logqueries you will find all the SQL commands to get the results.
**newsdata.sql is provided by udacity to complete this project**

**If you dont have news db run psql -d news -f newsdata.sql to create the db with it's tables and fill it with data**


To Get the same result, you will need to:

1. Open your terminal and go to the path of vagrant 
2. Run vagrant up
3. Run vagrant ssh to login to your VM.
4. cd/ vagrant to acsees the shared files.
5. move The downladed files to vagrant shared files
6. Run psql -d news -f CreateViews.sql   to create nedded views (it will create 2 views , one for the total requests by users and the second is for the requsts that lead to errors, each one contain the number of reauests for each day and the date)
7. run python loganalysis.py
8. type localhost:8000 on your browser to see the result for the requested questions.


To create the Views you need to run these commands:

CREATE VIEW ErrorAttemp AS
            (select count(log.status) as Attemp ,to_char(log.time, 'MONTH,DD,YYYY') as ErrorDate
            from log where log.status not like '200%' group by to_char(log.time, 'MONTH,DD,YYYY'));
			
 CREATE VIEW TotalAttemp AS
            (select count(log.status) as Attemp ,to_char(log.time, 'MONTH,DD,YYYY') as AttempDate
            from log group by to_char(log.time, 'MONTH,DD,YYYY'));






 