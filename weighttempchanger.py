#weight=int(input("input your weight\n"))
#output=input("select Kg or Lbs\n")

#def converted(weight):

 #   if output.lower()=="kg":
 #       convert=weight*2.20462262185
   #     print(f"your weight in kg is {convert}")
  #  else:
  #      output.lower()=="Lbs:
        #convert=weight/2.20462262185
        #print(f"your weight in lbs is {convert}")
#

#a=converted(weight)

temp=int(input("enter temperature\n"))
output=input("Fahrenheit(F) or Celsius(C)\n")

if output.upper()=="C":
  con=(temp*9/5) +32
  print(f"{con} Fahrenheit")
else:
  output.upper()=="F"
  con=(temp-32)*5/9
  print(f"{con} Celsius")