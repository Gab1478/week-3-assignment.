 """
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

#===================================================================function
def status_of(percent):
 """returns OVERLIMIT,WARNING,or OK based on the percentage."""
 if percent >=100:
  return "OVERLIMIT"
 elif percent >=90:
  return "WARNING"
 else:
  return "OK"

 def check (value, limit):
  """Calculate and return the difference and percentage."""
  difference= value - limit
  percent= (Value / limit )*100
  return difference, percent

 def print_report(label, values, limit, difference, status):
  """Prints the report details for a given table"""
  print("Label:",label)
  print("value:", values)
  print("Limit:", limit)
  print("Difference:",difference)
  print("percentage:",round(percent, 2))
  print("Status:",status)



  


# ==================================================================== INPUT
label = input ("Enter a label:")
value=float(input("Enter a value:"))
limit= float(input("Enter a limit:"))


# ================================================================== PROCESS
diffence, percent =check(value, limit)
status= status_of(percent)

print_report(label, value, limit, difference, percent, status)
# =================================================================== OUTPUT
def print_report(label, value, limit, difference, percent, status):
 """Prints all report values inside the border."""
 print("="*34)
 print(f"{'Label:':<12}{label}")
 print(f"{'Value:':<12}{value}")
 print(f"{'Limit:':<12}{limit}")
print(f"{Difference:':<12}{difference:>8.2f}")
print(f"{'Percent:':<12}{percent:>8.2f}")
print(f"{'Status:':<12}{status}")
print("="*34
      
      
      )
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
