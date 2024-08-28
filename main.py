print("                            ***Welcome T0 Bilal Calculator***")
firstnumber=int(input("inter first number:"))
secondnumber=int(input("inter second number:"))
operator=(input("which operation you have to perform:"))

if operator =="+":
 print("Addition Answer=",firstnumber+secondnumber)
 
elif operator =="-":
  print("Subtraction Answer=",firstnumber-secondnumber)
 
elif operator =="*":
  print("Multiplication Answer=",firstnumber*secondnumber)
 
elif operator =="/":
  print("Division Answer=",firstnumber/secondnumber)
 
elif operator =="**":
  print("Power of two nimbers is=",firstnumber**secondnumber)  
 
elif operator =="%":
  print("Reminder Answer=",firstnumber%secondnumber)
 
elif operator =="//":
  print("Modules Answer=",firstnumber//secondnumber)
 
else:
  print("Invalid operation")

print("                          Thanks for using our calculator") 
 


