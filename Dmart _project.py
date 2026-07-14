from datetime import datetime
print('='*50)    
print('='*12,"Dmart",'='*12)
print('='*50)    
print('='*12,'Bill','='*12)
bill_no = int(input('enter your bill no :'))    
print(f'bill no : {bill_no}')
bill_date = datetime.now()
print(f'date    :  {bill_date}')
customer_name = (input('enter your name'))
print("Customer Name: ",customer_name)
print('='*50)
a = 0
print(f'Product_name\tQty\tunit_price\tamount')
for i in range (1,100):
 product_name = (input('enter your product name'))
 quantity = int(input('enter your quantity'))
 amount = float(input('enter your amount'))
 bill_amount = amount*quantity 
 a += bill_amount
 add_items = input('enter more items yes/no : ')
 print(f'{product_name}\t	{quantity}\t{amount}\t	{bill_amount}')
 if add_items != "yes":
     break  

gst = a*0.18 

bill = gst + a
discount = a*0.40
dicounted_bill = a- discount
total_amount = gst+ a    
if a < 2000 :
     print('='*50)
     print  ('='*12,'nvoice','='*12)
     print(f'bill amount  : {a}')   
     print(f'gst amount   : {gst} ') 
     print(f"total amount : {bill} ")
else :
     print('='*50)
     print ('='*12,'invoice','='*12)
     print(f'bill amount      :    {a}')   
     print(f'discount amount  :    {discount}')
     print(f'gst amount       :    {gst} ') 
     print(f"total amount after dicount : {dicounted_bill +gst} ") 