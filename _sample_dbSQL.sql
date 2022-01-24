create database `musicfy_db`;

create table `user_tbl` (
    `uid` int not null auto_increment,
    `usertype` varchar(10) not null,
    `username` varchar(30) not null,
    `password` varchar(16) not null,
    primary key (uid)
);

create table `audio_tbl` (
    `aid` int not null auto_increment,
    `audio_name` varchar(50) not null,
    `uid` int not null, -- Artist / Uploader
    `audio_path` varchar(255) not null, -- Reason of not storing as BLOB: Performance overhead
    -- `num_dislike` int, -- like dislike in other table,∴against normalisation
    -- `num_like` int,
    primary key (aid),
    foreign key (uid) references user_tbl(uid)
);

-- Primary key = aid+uid from two other tables
create table `like_tbl` (
    `aid` int not null,
    `uid` int not null,
    `like_status` tinyint(2) -- 0 = didn't react, 1 = like, 2 = dislike
    foreign key (aid) references audio_tbl(aid),
    foreign key (uid) references user_tbl(uid),
    constraint PK_likes primary key (aid,uid)
);

-- For each category, create 1 table (normalisation)
-- Primary key use audioID (aid)
create table `cat_lofi` (
    `aid` int not null,
    `category_status` tinyint(1), -- 0 = not in category, 1 = in category
    primary key (aid),
    foreign key (aid) references audio_tbl(aid)
);

create table `cat_meme` (
    `aid` int not null,
    `category_status` tinyint(1), -- 0 = not in category, 1 = in category
    primary key (aid),
    foreign key (aid) references audio_tbl(aid)
);

create table `cat_jazz` (
    `aid` int not null,
    `category_status` tinyint(1), -- 0 = not in category, 1 = in category
    primary key (aid),
    foreign key (aid) references audio_tbl(aid)
);


insert into `user_tbl` (uid, usertype, username, password)
values ('1','admin','admin','admin'),
('2','artist','imartist','artist'),
('3','listener','listener','listener');

insert into `audio_tbl` (aid, audio_name, uid, audio_path)
values (1, 'Star Wars 3', 1, 'audio_files/StarWars3.wav'),
(2, 'Lone Sojounrer', 1, 'audio_files/Lone_Sojourner.mp3'),
(3, 'The Moon Song', 1, 'audio_files/The_Moon_Song.mp3'),
(4, '2113', 1, 'audio_files/two_one_one_three.mp3'),
(5, 'Letting Go', 1, 'audio_files/letting_go.mp3');


insert into `cat_lofi` (aid, category_status)
values (5,1);

insert into `cat_jazz` (aid, category_status)
values (5,1);

insert into `cat_meme` (aid, category_status)
values (4,1);

insert into `like_table` (aid, uid, like_status)
value (1,1,2),
(2,1,1),
(3,1,1),
(4,1,1),
(5,1,1);