
import math
def kmph_to_mps(kmph): 
  
    x = (250/9) * kmph
    y = math.floor(x)
    return y

kmph = float(input())
      
print(int(kmph_to_mps(kmph)))