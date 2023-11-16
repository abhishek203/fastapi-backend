
drop table if exists people CASCADE;
create table people(
    id int,
    pname varchar,
    primary key(id)

);

drop table if exists budget CASCADE;
create table budget(
    budget_id int,
    total_amount float,
    start_day date,
    category varchar,
    currency varchar,
    list_of_people_id integer[],
    current_consumption float,
    end_day date,
    primary key(budget_id)
);

drop table if exists transaction CASCADE;
create table transaction(
    t_id int,
    tran_day date,
    amount float,
    currency varchar,
    category varchar,
    person_id int,
    fip_name varchar,
    descrpiton varchar,
    primary key(t_id)
);