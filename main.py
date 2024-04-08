def fib_recursive(n, counts):
  if n == 0:
    counts[n] += 1
    return 0
  if n == 1:
    counts[n] += 1
    return 1
  else:
    counts[n] += 1
    return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)
    

    
def fib_top_down(n, fibs):
  if n == 0:
    fibs[n] = 0
    return 0
  if n == 1:
    fibs[n] = 1
    return 1
  else:
    if fibs[n-1] == -1:
      fibs[n-1]  = fib_top_down(n-1, fibs)
    if fibs[n-2] == -1:
      fibs[n-2] = fib_top_down(n-2, fibs)
    print(fibs)
    return fibs[n-1] + fibs[n-2]

#print(fib_top_down(10, [-1] * 11))

def fib_bottom_up(n):
  lst = [0] * (n+1)
  for i in range(len(lst)):
    if i == 0:
      lst[i] = 0
    elif i == 1:
      lst[i] = 1
    else:
      lst[i] = lst[i-1] + lst[i-2]
  return lst[n]
print(fib_bottom_up(10))
    


def fib_bottom_up_better(n):
    ###TODO
    pass

