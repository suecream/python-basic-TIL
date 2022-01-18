BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'kim','superlove133@gmail.com','010-5749-9926','kim.com','2021-05-20 01:11:53');
INSERT INTO "users" VALUES(2,'park','khj990213@naver.com','031-397-9926','park.com','2021-05-20 01:12:38');
INSERT INTO "users" VALUES(3,'lee','lee@naver.com','010-1234-2353','lee.com','2021-05-20 01:11:41');
INSERT INTO "users" VALUES(4,'cho','cho@naver.com','010-2134-2664','cho.com','2021-05-20 01:11:41');
INSERT INTO "users" VALUES(5,'yoon','yoon@google.com','010-6623-4121','google.com','2021-05-20 01:11:41');
COMMIT;
