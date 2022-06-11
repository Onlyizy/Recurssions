def F_num(n):
  if n<=1:
    return n
  return F_num(n-1)+F_num(n-2)
