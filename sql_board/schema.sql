create table info(
	id integer primary key autoincrement,
	title varchar(50) not null,
	writer varchar(20) not null,
	content text not null
);