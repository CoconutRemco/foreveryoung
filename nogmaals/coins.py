# name of student:Remco Mol 
# number of student:99071124
# purpose of program:making sure the change is right
# function of program:returning spare change in coins
# structure of program:structure is based on ifs and whiles 

toPay = int(float(input('Amount to pay: '))* 100) #this makes it easier for program to understand
paid = int(float(input('Paid amount: ')) * 100) #makes it easier for program to understand
change = paid - toPay #this wil see how many you have to get back

cr500=0
cr300=0
cr200=0
cr50=0
cr20=0
cr10=0
cr5=0
cr2=0
cr1=0

if change > 5: #if the change is bigger than 5 you get paid in 5s
  coinValue = 500 #this wil see if you get paid in 5s or 3s
elif change > 3:
  coinValue = 300
elif change > 2:
  coinValue = 200
elif change > 0:
  coinValue = 50
else:
  print("Nothing to return")
  
while change > 0 and coinValue > 0: #This will make sure you have to return coins
    nrCoins = change // coinValue #this wil count how many coins

    if nrCoins > 0: #if its 0 you get nothing
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #this prints the maximum coins you have to retunr
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #this askes how many you returned
      change -= nrCoinsReturned * coinValue #this wil make sure it is right
      print("Number of coins retunerd: " + str(nrCoinsReturned) + str(coinValue))

# comment on code below:If the value is the same as 1 of the coins you will get paid in the coins with less value 
    if coinValue == 500:
      cr500=nrCoinsReturned
      coinValue = 300
    elif coinValue == 300:
      cr300=nrCoinsReturned
      coinValue = 200
    elif coinValue == 200:
      cr200=nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      cr50=nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      cr20=nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      cr10=nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      cr5=nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      cr2=nrCoinsReturned
      coinValue = 1
    else:
      cr1=nrCoinsReturned
      coinValue = 0

if change > 0: #this wil make sure you have returned the correct amount
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')

  print("5 euro muntstukken "+ str(cr50))