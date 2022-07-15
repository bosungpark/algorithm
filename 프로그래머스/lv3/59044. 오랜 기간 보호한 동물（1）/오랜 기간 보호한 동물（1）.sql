-- 코드를 입력하세요
SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME from ANIMAL_INS
                                            
where ANIMAL_INS.ANIMAL_ID not in (select ANIMAL_ID from ANIMAL_OUTS) 

order by ANIMAL_INS.DATETIME
limit 3