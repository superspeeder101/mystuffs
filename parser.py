def get_in_parenthesis(data):
  indexes = []
  cindexs = []
  
  for ind, char in enumerate(list(data)):
    if len(cindexs) == 0:
      if char == "(":
        cindexs.append(ind+1)
    
    if len(cindexs) == 1:
      if char == ")":
        cindexs.append(ind)
        indexes.append(tuple(cindexs))
        cindexs = []
    
  
  out = []
  for index in indexes:
    out.append(data[slice(*index)])
  
  return out

def find_char(string, char):
  indexes = []
  for index, char_ in enumerate(list(string)):
    if char_ == char:
      indexes.append(index)
  
  return tuple(indexes)

def find_string(main_str, substr):
  slices = []
  substr_l = list(substr)
  main_str_l = list(main_str)
  substr_len = len(substr)
  
  # print(substr_l)
  
  for index, char in enumerate(main_str_l):
    if char == substr_l[0]:
      # print(main_str_l[index:index+substr_len])
      # print(main_str_l[index:index+substr_len] == substr_l)
      if main_str_l[index:index+substr_len] == substr_l:
        slices.append(slice(index,index+substr_len))
  # print(slices)  
  return slices

