import unittest
from BankAccount import BankAccount
from BankAccount import AccountType

class BankAccountAnswerTest (unittest.TestCase) :
    STARTING_BALANCE = 100
    
    def setUp(self) : 
        self.account = BankAccount(BankAccountAnswerTest.STARTING_BALANCE, AccountType.CHECKING)
    
    def tearDown(self):
        cur_balance = self.account.getBalance()
        difference = 100 - cur_balance

        if(difference > 0) : self.account.deposit(difference)
        elif(difference < 0) : self.account.withdraw(difference)

    def test_deposit(self) :
        #get balance...
        beforeDeposit = self.account.getBalance()

        #set amount to deposit...
        depositAmount = 100

        #deposit that amount
        self.account.deposit(depositAmount)

        #this should be the expected amount in the bank...
        expected = beforeDeposit + depositAmount
		
        #this is the actual balance we have
        actual = self.account.getBalance()
		
		#this will return true or false if the amount we expected is the same
		#as the actual amount for our balance
        self.assertEqual(expected, actual)


    def test_withdraw(self) :
        #get balance...
        beforeDeposit = self.account.getBalance()

        #set amount to withdraw...
        withdrawAmount = 20

        #withdraw that amount
        self.account.withdraw(withdrawAmount)

        #this should be the expected amount in the bank...
        expected = beforeDeposit - withdrawAmount
		
        #this is the actual balance we have
        actual = self.account.getBalance()
		
		#this will return true or false if the amount we expected is the same
		#as the actual amount for our balance
        self.assertEqual(expected, actual)

    def test_deposit_negative_amount(self) :
        negative_dep = -100

        #get our balance before deposit...
        beforeDeposit = self.account.getBalance()

        #deposit some negative amount
        self.account.deposit(negative_dep)

        #Check that negative amount wasn't deposited, should still be the same
        #balance before deposit happened
        self.assertEqual(self.account.getBalance(), beforeDeposit)

	
	#here we will check to see when we create a balance we don't set it to a negative
	#number at the start
    def testAccountNegativeStartingBalance(self) :
        account = BankAccount(-100, AccountType.CHECKING);
		

    #    this method checks if the condition we pass to it is true
	#	first run will be false, go back to BankAccount class and fix code
	#	so it doesn't set a negative balance
        self.assertTrue(account.getBalance() >= 0)
		
    """"
	we deal with cases when a negative number is passed to withdraw()
	method and make sure we don't withdraw a negative number and 
	add to the balance instead of removing from it
    """
    def testNegativeWithdrawal(self) :
        negativeWithdraw = -20

        #get balance before withdraw
        beforeWithdrawal = self.account.getBalance()

        #...withdraw some negative amount...
        self.account.withdraw(negativeWithdraw)

		# ...assert negative number cannot be passed to withdraw, or
		# else this will actually deposit to the account
        self.assertEqual(beforeWithdrawal, self.account.getBalance())
	
	#this tests that we check if an overdraft doesn't happen with a
	#custom exception 
    def testOverdraft(self) :
		# will check that an OverdraftException is thrown when we try to withdraw too much
        overDraftAmount = 200
        self.assertRaises(Exception, self.account.withdraw, overDraftAmount)

if __name__ == '__main__' :
    unittest.main()