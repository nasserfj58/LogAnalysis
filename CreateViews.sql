CREATE VIEW ErrorAttemp AS
            (select count(log.status) as Attemp ,to_char(log.time, 'MONTH,DD,YYYY') as ErrorDate
            from log where log.status not like '200%' group by to_char(log.time, 'MONTH,DD,YYYY'));
			
 CREATE VIEW TotalAttemp AS
            (select count(log.status) as Attemp ,to_char(log.time, 'MONTH,DD,YYYY') as AttempDate
            from log group by to_char(log.time, 'MONTH,DD,YYYY'));
