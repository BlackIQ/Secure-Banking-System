CREATE TABLE confidentiality(
	ID INT primary key,
    confidentiality_level varchar(30)
);

CREATE TABLE integrity(
	  ID INT primary key,
    integrity_level varchar(30)
);

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
