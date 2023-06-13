def div(a,b):
    d = 0
    print("Before TRY -Step-1")
    try:
        print("Inside TRY - Step-2")
        d = a // b
        print("Inside TRY Step-3")
    except Exception as e:
        print("Inside EXCEPT Step-4")
        print("Error is:",e)
        print("Inside EXCEPT Step-5")
    finally:
        print("Division of {},{} is {}".format(a,b,d))
        print("In FINNALLY Step-6")
    return d

res = div(10,0)
