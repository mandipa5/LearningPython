expenses = {
  'January' : 1000,
  'February' : 1200,
  'March' : 2300,
  'April' : 2999,
  'May' : 1943,
  'June' : 1299,
  'july' : 4969,
  'august' : 2300,
  'september' : 2312,
  'october' : 2345,
  'november' : 2865,
  'december' : 3412
}
total = sum(expenses.values())
print(f"Total bill of electricity is: {total}")
print(f"Average bill of electricity is: {total/12}")

##If you want bill of certain month
#print(f"bill of september is {expenses['september]'}")