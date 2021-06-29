CREATE TABLE confidentiality(
	ID INT primary key,
    confidentiality_level varchar(30)
);

CREATE TABLE integrity(
	ID INT primary key,
    integrity_level varchar(30)
);

CREATE TABLE account_type(
    ID INT primary KEY,
    title varchar(30)
);

INSERT INTO account_type(ID,title) values
                (1, 'Short-term deposit'),
                (2, 'Long-term deposit'),
                (3, 'Current'),
                (4, 'Interest-free');

INSERT INTO confidentiality(ID, confidentiality_level) values
				(1 , 'Unclassified'),
                (2 , 'Confidential'),
                (3 , 'Secret'),
                (4 , 'TopSecret');

INSERT INTO integrity(ID, integrity_level) values
				(1 , 'UnTrusted'),
                (2 , 'SlightlyTrusted'),
                (3 , 'Trusted'),
                (4 , 'VeryTrusted');


CREATE TABLE users(
	ID INT primary key auto_increment,
    username varchar(30) unique,
    password_hash varchar(64),
    salt varchar(16),
    confidentiality_level int,
    integrity_level int,
    number_of_attempts int,
    is_block int default 0,
    foreign key (confidentiality_level) references confidentiality(ID),
	foreign key (integrity_level) references integrity(ID)
);

CREATE TABLE accounts(
    -- ID INT primary key auto_increment,
    account_no bigint unsigned not null auto_increment primary key,
    owner_id INT,
    account_type_id INT,
    confidentiality_level INT default 4, 
    integrity_level INT default 1,       
    amount FLOAT,
    foreign key (owner_id) references users(ID),
    foreign key (account_type_id) references account_type(ID),
    foreign key (confidentiality_level) references confidentiality(ID),
    foreign key (integrity_level) references integrity(ID)
    
)auto_increment=1000000000;

CREATE TABLE account_user(
    account_no bigint unsigned,
    user_id INT,
    confidentiality_level INT default 4,
    integrity_level INT default 1,
    foreign key (user_id) references users(ID),
    foreign key (account_no) references accounts(account_no),
    foreign key (confidentiality_level) references confidentiality(ID),
    foreign key (integrity_level) references integrity(ID)

);


