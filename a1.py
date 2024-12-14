shutdown=(input("choose YES or NO:"))
def shut(down):
    if down=="yes"  :  
       return print("shutting down")
    else:
       return print("not shutting down")
num=shut(shutdown)
print(num)