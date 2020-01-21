ALTER TABLE practice
	ADD PRIMARY KEY(email)

ALTER TABLE practice
	ADD target VARCHAR(20)

ALTER TABLE practice
	ADD FOREIGN KEY(target)
	REFERENCES practice1(email)
	
CREATE TABLE 부서 (
 부서번호 INT,
 부서이름 VARCHAR(10),
 PRIMARY KEY(부서번호)
);

`부서`CREATE TABLE 사원 (
 사원번호 INT,
 사원이름 VARCHAR(10),
 소속부서 INT,
 PRIMARY KEY(사원번호),
 FOREIGN KEY(소속부서) REFERENCES 부서(부서번호)
);

#주석
--Create database mydb

CREATE TABLE practice1(
	email VARCHAR(20),
	pw VARCHAR(20),
	age INT,
	PRIMARY KEY(email)
);

CREATE TABLE practice(
	email VARCHAR(20),
	pw VARCHAR(20),
	age INT
);

CREATE TABLE test1(
	NUM INT,
	NAME VARCHAR(10),
	AGE INT,
	EMAIL VARCHAR(50),
	PHONE VARCHAR(20),
	PRIMARY KEY(NUM)
);

CREATE TABLE DEPT(
	DEPTNO TINYINT,
	DNAME VARCHAR(14),
	LOC VARCHAR(13)
);

ALTER TABLE DEPT
	ADD PRIMARY KEY(DEPTNO)

CREATE TABLE EMP (
	EMPNO INT,
	ENAME VARCHAR(10),
	JOB VARCHAR(9),
	MGR INT,
	HIREDATE DATETIME,
	SAL INT,
	COMM INT,
	DEPTNO TINYINT,
	PRIMARY KEY(EMPNO),
	FOREIGN KEY(DEPTNO) REFERENCES DEPT(DEPTNO)
);

ALTER TABLE test1
	DROP AGE;
	
ALTER TABLE test1
	MODIFY EMAIL VARCHAR(100)
	
