def get_shortest_unique_substring(arr, str):
  '''
  arr_map = {'x' : 1,'y' : 1,'z' :1}, 
  str = "x y y z y z y x"
                   i 
       j 0 1 3 4 5 6 7  8
      ut 1 2 2 3 2 2 2  3
         2
          
  '''
  i = 0
  res = ''
  uni_cnt = 0
  seen = {}
  for ch in arr:
    seen[ch] = 0
  #sacan the str
  for j in range(len(str)):
    if str[j] not in seen:
      continue
    if seen[str[j]] == 0:
      uni_cnt += 1
    seen[str[j]] += 1
    
    while uni_cnt == len(arr):
      lens = j - i + 1
      if lens == len(arr):
        return str[i : j + 1]
      if res == '' or lens < len(res):
        res = str[i : j + 1]
      if str[i] in seen:
        seen[str[i]] -= 1
        if seen[str[i]] == 0:
          uni_cnt -= 1
      i += 1
  return res
arr = ['x', 'y', 'z']
s = 'xyyzyzyx'
res = get_shortest_unique_substring(arr, s)
print(res)

      