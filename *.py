today="2022.05.19"
terms=["A 6", "B 12", "C 3"]
privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

terms_record=dict()
today_global=None
answer=[]

def solution(today, terms, privacies):
    global terms_record, today_global, answer

    answer = []
    # 약관 전역변수로 저장
    for t in terms:
        term, months=t.split()
        terms_record[term]=int(months)

    # 통일된 기준으로 컨버전
    today_global=converter(today, 0)
    for idx, p in enumerate(privacies, start=1):
        p=converter(p, idx)

    print("today=",today_global)
    print("privacies=",privacies)
    
    return answer

def converter(date, idx):
    date, *term=date.split()
    year,month,day=map(lambda x: int(x.lstrip("0")), date.split("."))

    res=day + month*28 + 28*12*year
    
    if term:   
        if today_global>=res+(terms_record[term[0]]*28):
            answer.append(idx)
    return res
print(solution(today, terms, privacies))
