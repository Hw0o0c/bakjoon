n = int(input())
card = set()
for i in map(int, input().split()):
    card.add(i)

m = int(input())
m_card = [x for x in map(int,input().split())]
for i in m_card:
    if i in card:
        print(1, end=" ")
    else:
        print(0, end=" ")