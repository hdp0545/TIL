# with

with 절은 여러번 사용되는 쿼리를 임시 테이블에 저장하는 역할을 한다.

```mysql
 SELECT deptno, SUM(sal) AS SUM
 	FROM emp
 	GROUP BY deptno
 	HAVING SUM(sal) > ( SELECT AVG(SUM(sal))
 						FROM emp
 						GROUP BY deptno ) ; 
```

위의 코드는 `SUM(sal)`이 2번 사용된다.

따라서 with절을 사용하면

```mysql
 WITH sum_sal AS ( SELECT deptno, SUM(sal) AS SUM
 					FROM emp
 					GROUP BY deptno )
 SELECT *
 FROM sum_sal
 WHERE sum > ( SELECT AVG(sum) FROM sum_sal ) ; 

```

이런식으로 쿼리의 호출을 한번만 할 수 있다.

> WITH 절의 집합은 문장 실행 시 가장 먼저 실행되며 해당 결과를 임시 데이터로 저장한다. 문제는 이 러한 임시 데이터의 반복 접근이 일어날 때마다 물리적인 I/O 가 증가되어 오히려 성능이 저하될 가능 성도 있다. 

1. WITH 절은 반복되는 쿼리의 결과를 문장 시작 전 액세스하여 임시 테이블로 저장, 재 사용을 목적 으로 한다.

2. 문장 안에 WITH 절의 Subquery 가 두 번 이상 사용되면 임시 테이블이 생성되며, 한 번 사용되면 Inline View 형식으로 실행된다. 

3. WITH 절의 임시 테이블 형식의 사용은 Physical I/O를 동반할 수 있으므로 그 크기가 크지 않은 경우에 유리하다. 

4. MATERIALIZE, INLINE 힌트를 이용하여 형식 지정 가능

   ```mysql
   WITH sum_sal AS ( SELECT /*+ materialize */ deptno, SUM(sal) AS SUM
    					FROM emp
    					GROUP BY deptno )
    SELECT *
    FROM dept d, sum_sal s
    WHERE d.deptno = s.deptno ; 
   ```

   위의 방식은 템프테이블에 저장하여 무조건 사용

   ```mysql
   WITH sum_sal AS ( SELECT /*+ inline */ deptno, SUM(sal) AS SUM
    					FROM emp
   					GROUP BY deptno )
    SELECT *
    FROM sum_sal
    WHERE sum > ( SELECT AVG(sum) FROM sum_sal ) ; 
   ```

   위의 방식은 `sum_sal`에 무조건 with 안의 코드를 넣어서 실행



# group by

2가지의 결과를 모두 나타낼 수 있는 방법은 

```mysql
 SELECT deptno, SUM(sal) AS sum_sal
 FROM emp
 GROUP BY deptno
 UNION ALL
 SELECT NULL, SUM(sal)
 FROM emp
 ORDER BY deptno ;
```

보다는

```mysql
 SELECT deptno, job, SUM(sal) AS sum_sal
 FROM emp
 GROUP BY ROLLUP(deptno, job);
```

롤업은 둘 이상의 그래핑을 할 때 사용되는 함수이다.

```mysql
GROUP BY ROLLUP(DEPTNO, JOB)
```

위 식은

```mysql
GROUP BY DEPTNO, JOB
GROUP BY DEPTNO
GROUP BY ()
```

으로 나온 결과를 UNION ALL한 것과 같은 결과를 뽑아낸다.

---

만약 `GROUP BY JOB`의 결과 또한 필요하다면 `CUBE()`를 사용할 수 있음

```mysql
GROUP BY CUBE(DEPTNO, JOB)
```

위의 결과는 

```mysql
GROUP BY DEPTNO, JOB
GROUP BY DEPTNO
GROUP BY JOB
GROUP BY ()
```

로 생길 수 있는 모든 조합이 생김

만약 다양한 조작이 하고 싶다면

```MYSQL
GROUP BY DEPTNO, ROLLUP(JOB)
```

등의 방식을 통해

```MYSQL
GROUP BY DEPTNO, JOB
GROUP BY DEPTNO
```

등의 조작이 가능함.



# 분석함수

시험에는 안나온다.

GRUOP BY 함수는 그룹당 하나씩 실행되는 함수이다.

```mysql
SELECT E.*, SUM(SAL)
FROM EMP
```

위의 함수는 당연히 에러가 난다.

그 이유는 `E.*`의 단일행 함수와 `SUM(sal)`이 개수가 차이나게 되고 GROUP BY 로 E의 항의 갯수를 줄이않는 한 계속 에러가난다.

```mysql
SELECT E.*, SUM(SAL) OVER()
FROM EMP
```

하지만 위의 분석함수를 활용해 `SUM(SAL)`을 늘려서 



# CASE WHEN

시험에는 안나온다.





# MODEL

안중요하다. 파이썬 마냥 칼럼명[주소] = 칼럼명[밸류]이런식으로 저장 가능함.



5조인 서브쿼리 활용

WITH 절

그룹함수 활용

계층 질의

INDEX 사용하는 SQL

TOPN질의