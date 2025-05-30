/*****************************************************
 * @software: PyCharm
 * @author: Lionel Johnson
 * @contact: https://fairy.host
 * @organization: https://github.com/FairylandFuture
 * @datetime: 2025-05-29 10:59:54 UTC+08:00
 *****************************************************/

-- 用户组
create table if not exists webserver.app_rbac_group (
	id int auto_increment primary key,
	name varchar(64) not null comment '用户组名',
	parent_id int not null default 0 comment '父用户组ID',
	description varchar(256) default '' comment '描述',

	existed boolean not null default true comment '是否存在',
	created_at datetime not null default current_timestamp comment '创建时间',
	updated_at datetime not null default current_timestamp on update current_timestamp comment '更新时间',

	unique key uk_name_parent_id (name, parent_id)
) default charset utf8mb4 comment '用户组表';

-- 用户
create table if not exists webserver.app_rbac_user (
	id int auto_increment primary key,
	name varchar(64) not null comment '名称',
	username varchar(64) not null comment '用户名',
	password varchar(128) not null comment '密码',
	email varchar(128) not null comment '邮箱',
	phone varchar(11) not null comment '手机号',
	group_id int not null default 1 comment '用户组ID',

	existed boolean not null default true comment '是否存在',
	created_at datetime not null default current_timestamp comment '创建时间',
	updated_at datetime not null default current_timestamp on update current_timestamp comment '更新时间',

	unique key uk_username (username),
	unique key uk_email (email),
	unique key uk_phone (phone)
) default charset utf8mb4 comment '用户表';

-- 角色
create table if not exists webserver.app_rbac_role (
	id int auto_increment primary key,
	name varchar(64) not null comment '角色名',
	description varchar(256) default '' comment '描述',

	existed boolean not null default true comment '是否存在',
	created_at datetime not null default current_timestamp comment '创建时间',
	updated_at datetime not null default current_timestamp on update current_timestamp comment '更新时间'
) default charset utf8mb4 comment '角色表';

-- 用户->角色关联表, 1:N
create table if not exists webserver.app_rbac_user_role (
	id int auto_increment primary key,
	user_id int not null comment '用户ID',
	role_id int not null comment '角色ID',

	existed boolean not null default true comment '是否存在',
	created_at datetime not null default current_timestamp comment '创建时间',
	updated_at datetime not null default current_timestamp on update current_timestamp comment '更新时间',

	unique key uk_user_role (user_id, role_id)
) default charset utf8mb4 comment '用户角色关联表';

-- 权限
create table if not exists webserver.app_rbac_permission (
	id int auto_increment primary key,
	name varchar(64) not null comment '权限名',
	description varchar(256) default '' comment '描述',
	code varchar(64) not null comment '权限代码',
	path varchar(256) not null comment 'API路径',
	/* TODO: 完善权限信息, 是否需要添加WEB字段的详细权限拆分 */

	existed boolean not null default true comment '是否存在',
	created_at datetime not null default current_timestamp comment '创建时间',
	updated_at datetime not null default current_timestamp on update current_timestamp comment '更新时间'
) default charset utf8mb4 comment '权限表';

-- 角色->权限关联表, N:N
create table if not exists webserver.app_rbac_role_permission (
	id int auto_increment primary key,
	role_id int not null comment '角色ID',
	permission_id int not null comment '权限ID',

	existed boolean not null default true comment '是否存在',
	created_at datetime not null default current_timestamp comment '创建时间',
	updated_at datetime not null default current_timestamp on update current_timestamp comment '更新时间',

	unique key uk_role_permission (role_id, permission_id)
) default charset utf8mb4 comment '角色权限关联表';

-- 初始化默认用户组
insert into webserver.app_rbac_group
	(name, parent_id, description)
values
	('默认用户组', 0, '默认用户组');

-- 初始化默认用户
insert into webserver.app_rbac_user
	(name, username, password, email, phone)
values
	('管理员', 'admin', '', 'admin@example.com', '13312341234');

-- 初始化默认角色
insert into webserver.app_rbac_role
	(name, description)
values
	('管理员', '系统管理员'),
	('普通用户', '普通用户');

-- 管理员添加权限
insert into webserver.app_rbac_user_role
	(user_id, role_id)
values
	(1, 1); -- 管理员用户添加管理员角色

-- 初始化默认权限
insert into webserver.app_rbac_permission
	(name, description, code, path)
values
	('全部权限', '系统所有权限', 'system', '/*');

-- 管理员添加权限
insert into webserver.app_rbac_role_permission
	(role_id, permission_id)
values
	(1, 1); -- 管理员角色添加全部权限
