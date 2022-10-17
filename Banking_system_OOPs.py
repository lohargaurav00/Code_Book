class Account:
    
       def __init__(self,owner,balance):
              self.owner = owner
              self.balance = balance
       
       def __str__(self):
              return f"Account Owner: {self.owner} \nAccount Balance: ${self.balance}"
              
       def deposit(self,rupees):
               self.balance = self.balance + rupees
               print("Doposit Accepted:",rupees)
               print("Your current balance:",self.balance)

       def withdraw(self,rupees):
              if self.balance > rupees:
                     self.balance = self.balance - rupees
                     print("withdrawel succesful:",rupees) 
                     print("Your current balance:",self.balance)
              else:
                     print("Not enough money to withdraw")
                     print("Your current balance:",self.balance)

# 1. Instantiate the class
acct1 = Account('Gaurav',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
