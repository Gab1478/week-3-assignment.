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



  


# ==================================================================== INPUT
label = input ("Enter a label:")
value=float(input("Enter a value:"))
limit= float(input("Enter a limit:"))


# ================================================================== PROCESS
difference= value - limit
percent=(value/limit)*100

if percent >= 100:
  status="OVERLIMIT"
elif percent >=90:
  status ="WARNING"
else:
  status ="OK"

print("Difference:", difference)
print("percentage:", percent)
print("status:", status)
status= status_of(percent)

# =================================================================== OUTPUT
def print_report(label, value, limit, difference, percent, status):
 """Prints all report values inside the border."""
 print("="*34)
 print(f"value: {value:.2f}")
 print(f"Limit: {limit:.2f}")
 print(f"Status: {status}")
      
      
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
