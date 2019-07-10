u=input("ENter unit =")
if u<=150:
 a=2.4*u
elif u>150 and u<=300:
 a=(u-150)*3+2.4*150
elif u>300:
 a=150*2.4+3*(150)+(u-300)*3.2
print "amount ",a