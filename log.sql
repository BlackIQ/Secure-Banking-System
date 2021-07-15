CREATE TABLE log(
    username varchar(35),
    time_of_action varchar (25),
    action varchar(80),
    status varchar(30),
    amount FLOAT,
    from_account bigint unsigned,
    to_account bigint unsigned

);

