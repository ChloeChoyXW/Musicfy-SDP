create database `musicfy_db`

create table `user_tbl` (
    `uid` int not null auto_increment,
    `usertype` varchar(10) not null,
    `username` varchar(30) not null,
    `password` varchar(16) not null,
    primary key (uid)
)

create table `audio_tbl` (
    `aid` int not null auto_increment,
    `audio_name` varchar(50) not null,
    `uid` int not null, -- Artist / Uploader
    `audio_path` varchar(255) not null, -- Reason of not storing as BLOB: Performance overhead
    `num_dislike` int,
    `num_like` int,
    primary key (aid),
    foreign key (uid) references user_tbl(uid)
)

insert into `user_tbl` (uid, usertype, username, password)
values ('1','admin','admin','admin'),
('2','artist','imartist','artist'),
('3','listener','listener','listener')

insert into `audio_tbl` (aid, audio_name, uid, audio_path, num_like, num_dislike)
values (1, 'Star Wars 3', 1, 'audio_files/StarWars3.wav', 1, 0),
(2, 'Lone Sojounrer', 1, 'audio_files/Lone_Sojourner.mp3', 1, 0),
(3, 'The Moon Song', 1, 'audio_files/The_Moon_Song.mp3', 1, 0)