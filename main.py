def missingnumber():
  # For finding the missing number
  for i in range(1,n+1):
    if(not str(i) in arr):
      print(f"\n{i} is missing.")
      break;

def noerrors():
  # For detecting invalid inputs
  if(not len(arr)==n-1):
    return False
  for i in range(0,len(arr)):
    if(arr[i] in arr[i+1:len(arr)] or int(arr[i])>n):
      return False
  return True

print("Missing Number Finder!!\n\n")
n=int(input("Enter the n\n"))
s=input("Enter the sequence\n")
arr=s.split(" ")
if(noerrors()):
  missingnumber()
else:
  print("\nError")
