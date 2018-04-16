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
