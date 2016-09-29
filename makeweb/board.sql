create table board(
	id int primary key auto_increment,
	title varchar(100) not null,
	content text not null,
	writer varchar(20)
);