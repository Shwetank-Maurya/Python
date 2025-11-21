inp='q'
while(inp!='x'):
    num=int(input("Enter the number:"))
    for i in range(10):
        print(f"{num} * {i+1} = {num*(i+1)}")
    inp=input("Enter x to exit or anything else to continue:")
    inp=inp.lower()
