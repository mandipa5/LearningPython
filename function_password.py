import random

def generate_password():
  alphabet = ' a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
  alphabet_upper = alphabet.upper()
  numbers = '1,2,3,4,5,6,7,8,9'

  all_combined = alphabet + alphabet_upper + numbers
  all_combined_list = all_combined.split(",")
  ##print(all_combined_list)

  random1 = random.choice(all_combined_list)
  random2 = random.choice(all_combined_list)
  random3 = random.choice(all_combined_list)
  random4 = random.choice(all_combined_list)
  random5 = random.choice(all_combined_list)
  random6 = random.choice(all_combined_list)
  random7 = random.choice(all_combined_list)
  random8 = random.choice(all_combined_list)
  random9 = random.choice(all_combined_list)
  random10 = random.choice(all_combined_list)

  password = random1 + random2 + random3 + random4 + random5 + random6 +random7 +random8 +random9 + random10

  print(f"Generated password is: {password}")
generate_password()
    