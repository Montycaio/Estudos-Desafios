x1, y1 = map(float, input().split())

x2, y2 = map(float, input().split())


formula = lambda x1,x2,y1,y2: ((x2-x1)**2+(y2-y1)**2)**0.5

print(f"{formula:.4f}")