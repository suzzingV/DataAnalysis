import pandas as pd
import numpy as np

student1 = pd.Series({'국어': np.nan, '영어':80, '수학': 90})
student2 = pd.Series({'수학': 80, '국어': 90})

print(student1)
print('\n')
print(student2)
print('\n')

addition = student1 + student2
substraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
#어느 한쪽에만 인덱스 존재하고 다른 쪽에는 짝 지을 수 있는 동일한 인덱스 없음 -> NaN
print(type(division))
print('\n')

result = pd.DataFrame([addition, substraction, multiplication, division],
                      index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)