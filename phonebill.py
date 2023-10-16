name = input("What's your name? ")
# -------- Task 1 --------
# Complete the code to ask user for their mobile operator name (like EE or O2)
operator = 

# -------- Task 1 --------

# Ask the user for the number of messages they've sent
text = input("How many texts have you sent this month? ")
# Convert the text (string) to integer
text = int(text)

# -------- Task 2 --------
# Ask the user to enter the call minutes they've used, and convert that to a number


# -------- Task 2 --------

# Calculate text bill
text_bill = text * 0.05
# Calculating text bill with VAT
text_bill_vat = text_bill + text_bill * 0.2

# -------- Task 3 --------
# Calculate the call bill (without and with VAT)


# -------- Task 3 --------

# Print out the result of text bill
print("Your text bill is ", text_bill)
print("Your text bill after VAT is ", text_bill_vat)

# -------- Task 4 --------
# Print out the result of call bill


# -------- Task 4 --------

# -------- Task 5 --------
# Complete these two lines of code
# Total bill should be the sum of text and call bill
total_bill = text_bill + 
total_bill_vat = text_bill_vat + 
# -------- Task 5 --------

print(name, " your total bill is", total_bill)
print(name, " your total bill is", total_bill_vat)
print("Please pay your ", operator, " bill in time.")