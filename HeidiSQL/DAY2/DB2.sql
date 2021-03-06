SELECT * FROM EMP
SELECT * FROM DEPT

SELECT EMP.ENAME, DEPT.DEPTNO, DEPT.DNAME
	FROM EMP
	JOIN DEPT
	ON DEPT.DEPTNO = EMP.DEPTNO
	
SELECT *
	FROM EMP
	JOIN DEPT
	ON DEPT.DEPTNO = EMP.DEPTNO

SELECT EMP.ENAME, EMP.COMM, EMP.SAL, DEPT.LOC
	FROM EMP
	JOIN DEPT
	ON DEPT.DEPTNO = EMP.DEPTNO
	WHERE EMP.COMM IS NOT NULL
	
SELECT SUM(EMP.SAL), DEPT.DNAME
	FROM EMP
	JOIN DEPT
	ON DEPT.DEPTNO = EMP.DEPTNO
	WHERE DEPT.LOC = 'NEW YORK' OR DEPT.LOC = 'DALLAS'
	GROUP BY DEPT.DNAME
	
SELECT E1.EMPNO, E1.ENAME, E1.MGR, E2.ENAME
	FROM EMP E1
	JOIN EMP E2
	ON E1.MGR = E2.EMPNO
	
SELECT *
	FROM IT_MEMBER IT
	LEFT JOIN COURSE02 CO
	ON IT.COURSE_NO = CO.COURSE_NO
	
SELECT *
	FROM IT_MEMBER IT
	RIGHT JOIN COURSE02 CO
	ON IT.COURSE_NO = CO.COURSE_NO
	
SELECT *
	FROM EMP
	WHERE SAL >= (
		SELECT SAL
			FROM EMP
			WHERE ENAME = 'ALLEN')
	
SELECT ENAME, JOB, DEPTNO FROM EMP
	WHERE DEPTNO = (
		SELECT DEPTNO FROM EMP
			WHERE MGR IS NULL)
	
SELECT * FROM EMP
	WHERE SAL < (
		SELECT AVG(SAL) FROM EMP
			WHERE DEPTNO = (
				SELECT DEPTNO FROM EMP
					WHERE COMM = 0
			)
		)