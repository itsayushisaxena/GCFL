'''Given a series 7, 15, 32, 67 …… Find the nth term of this series.

Examples :

Input : 5 Output : 138

Input : 7 Output : 568'''

n_term = int(input())
first_term = 7
for i in range(1,n_term):
    first_term = first_term * 2 + i
print(first term)
