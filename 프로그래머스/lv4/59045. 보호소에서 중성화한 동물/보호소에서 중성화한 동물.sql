-- 코드를 입력하세요
SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.ANIMAL_TYPE, ANIMAL_INS.NAME from ANIMAL_INS
                                    join ANIMAL_OUTS
                                    on ANIMAL_INS.ANIMAL_ID=ANIMAL_OUTS.ANIMAL_ID

where (not ANIMAL_INS.SEX_UPON_INTAKE like "%Spayed%" and not ANIMAL_INS.SEX_UPON_INTAKE like "%Neutered%") and (ANIMAL_OUTS.SEX_UPON_OUTCOME like "%Spayed%" or ANIMAL_OUTS.SEX_UPON_OUTCOME like "%Neutered%") 

order by ANIMAL_INS.ANIMAL_ID