import timeit

string = input("Enter string:")
start = timeit.default_timer()
print("Reversed string : ",string[::-1])
end = timeit.default_timer()
print("Time taken : ",end-start)