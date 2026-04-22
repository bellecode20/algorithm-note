함수명: AVERAGE()는 없다, 무조건 AVG()

비교 연산: 값(문자열/숫자) 비교는 =, 빈 값 체크만 IS NULL

따옴표: 컬럼명에는 따옴표 빼기 (따옴표 쓰면 그냥 '글자'로 인식)

[수정 전] SELECT AVERAGE('FEE') ... WHERE TYPE IS 'SUV' (오류 발생)
[수정 후] SELECT AVG(FEE) ... WHERE TYPE = 'SUV' (정상 작동)

- ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID;
  쉼표로 구분

- DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d')
- YEAR(PUBLISHED_DATE) = 2021
- 이 방식이 더 나을 수도
  AND PUBLISHED_DATE >= '2021-01-01'
  AND PUBLISHED_DATE < '2022-01-01'

2. 포맷
   DATE_FORMAT(컬럼명, '%Y-%m-%d')
   %Y = 2021
   %y = 21

%m = 03
%c = 3

%d = 04
%e = 4

%H = 09 -- 24시간제
%h = 09 -- 12시간제
%i = 05 -- 분
%s = 07 -- 초

3. 여러개 검사
   WHERE MCDP_CD IN('CS','GS')

4. 문자열
   WHERE ADDRESS LIKE '강원도%'

# 템플릿

SELECT 컬럼들
FROM 중심테이블
JOIN 필요한테이블
ON 연결조건
WHERE 원본조건
GROUP BY 그룹컬럼
HAVING 집계조건
ORDER BY 정렬조건;
