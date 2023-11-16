Insert into budget(budget_id,total_amount,start_day,category,currency,list_of_people_id,current_consumption,end_day)
    Values
    (1,1000,'2023-11-17','food','INR','{1,2,3}',111,'2023-12-17')
    ;

Insert into budget(budget_id,total_amount,start_day,category,currency,list_of_people_id,current_consumption,end_day)
    Values
    (2,3000,'2023-10-17','food','INR','{1,2,3}',11,'2023-11-17')
    ;

Insert into transaction
    Values
    (1,'2023-12-10',112,'INR','food',1,'SBI','nooo');

Insert into transaction
    Values
    (2,'2023-12-11',1000,'INR','food',1,'SBI','nooo');