import math

def is_square(apositiveint):
  if apositiveint==1:
    return True
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def is_odd_square(x):
  if is_square(x) and x % 2 != 0:
    return True
  return False

def next_odd_square(n):
  last=n
  while True:
    if is_odd_square(last):
      return last
    last+=1

def what_ring(oddSquare):#starts at 1
  return int((math.sqrt(oddSquare)+1)/2)

def side_length(ring):
  return (2*ring)-1

def four_corners(oddSquare, ring):
  return[
    oddSquare-(side_length(ring)-1)*3,
    oddSquare-(side_length(ring)-1)*2,
    oddSquare-(side_length(ring)-1)*1,
    oddSquare
    ]

def find_offset(x, corners):
  differences=[]
  for i in corners:
    differences.append(abs(i-x))
  nearest_corner=corners[differences.index(min(differences))]
  return abs(nearest_corner-x)

def worst_case(ring):
  return 2*(ring-1)

number=int(input())
bottomRight = next_odd_square(number)
ring = what_ring(bottomRight)
offset = find_offset(number, four_corners(bottomRight, ring))
worstCase = worst_case(ring)
steps= worstCase-offset

print(number, bottomRight, ring, offset, worstCase,"answer:", steps)
