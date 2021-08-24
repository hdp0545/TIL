SELECT RANK() OVER(ORDER BY TOTAL DESC, LAST_SOLVED_TIME ASC) AS RANKING
     , C.NAME                 AS NAME
     , SUM(D.POINT)           AS TOTAL
		 , MAX(D.SOLVED_DATE)     AS LAST_SOLVED_TIME
  FROM USERS C
  JOIN (SELECT A.ID
	           , (SELECT SCORE FROM QUIZZES WHERE IDX=A.IDX) AS POINT
	           , A.SOLVED_DATE
    	    FROM SOLVE_LOGS A
		      JOIN (SELECT ID	 
                     , IDX 
                     , MAX(SOLVED_DATE) AS SOLVED_DATE
				          FROM SOLVE_LOGS
				         WHERE SOLVED_DATE BETWEEN str_to_date('2018-09-05 08:00:00', '%Y-%m-%d %H:%i:%S') AND str_to_date('2018-09-05 12:00:00', '%Y-%m-%d %H:%i:%S')
			        	 GROUP BY ID, IDX) B
				    ON A.ID = B.ID
				   AND A.IDX = B.IDX
				   AND A.SOLVED_DATE = B.SOLVED_DATE
				 WHERE A.SOLVED = TRUE) D
	  ON C.ID = D.ID
 GROUP BY C.ID
 ORDER BY 1
;