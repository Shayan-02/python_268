create table customers (
	c_id int primary key,
	c_name nvarchar(30) not null,
	c_pid int
);
create table test2 (
	t_id int identity(1,1),
	t_name nvarchar(30) not null,
	t_pid int,
	primary key(t_id, t_pid)
)

