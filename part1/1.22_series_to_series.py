import pandas as pd

#시리즈 vs 시리즈
student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90, '영어': 80})

print(student1)
print('\n')
print(student2)
print('\n')

#같은 인덱스를 가진 원소끼리 계산 -> 새 시리즈 반환
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))
print('\n')

result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
#.DataFrame: 하나의 데이터 프레임으로 합침
print(result)