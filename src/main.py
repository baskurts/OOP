from account.account import *
from savingsaccount.savingsaccount import *

def main():
    # create an account object named a1 that has a balance of $100
    a1 = account(100.0)
    a2 = account()
    # a1 = account(100.0, 200.0, 300.0, 400.0)
    # a1 account(-100.0) a balance less than zero will result in our code raising a ValueError

    # print(a1.public) referencing a public instance variable will not result in an error 
    # print(a1.__balance) referencing a private instance variable will result in an error
    # print(a1._protected) referencing a protected instance variable will not result in an error
    # print(a1._account__balance)

    # a1.__privateMethod() referencing a private instance method will result in an error
    # a1._account__privateMethod() 
    # a1._protectedMethod() referencing a protected method will not result in an error
    # a1.publicMethod() # referencing a public method will not result in an error

    # display the balance of a1
    print("$%.2f" % (a1.getBalance()))

    #increase the balance of a1 by $50
    a1.credit(50.0)
    # a1.credit(-50.0)

    # display the balance of a1
    print("$%.2f" % (a1.getBalance()))

    # decrease the balance of a1 by $75
    a1.debit(75.0)
    # a1.debit(-75.0)
    # a1.debit(151.0)

    # display the balance of a1
    print("$%.2f" % (a1.getBalance()))

    # display if the balance for a1 is empty
    print('Is, a1 empty? ', a1.isEmpty())

    # create a second account object named a2 and initialize
    # its balance o zero
    a2 = account()

    # display the balance of a2
    print("$%.2f" % (a2.getBalance()))

    # increase the balance of a2 by $150
    a2.credit(150.0)

    # display the balance of a2
    print("$%.2f" % (a2.getBalance()))

    # decrease the balance of a2 by $75
    a2.debit(75.0)

    # display the balance of a2
    print("$%.2f" % (a2.getBalance()))

    # display if the balance of a2 is empty
    print('Is, a2 empty? ', a2.isEmpty())

    # display a string representation of a1 and a2
    print(a1)
    print(a2)

    # create an object named a3 that is equal to None
    a3 = None

    # test if a1 is equal to a3
    print('Is a1 equal to a3?', a1.__eq__(a3))

    #create a string object named a1
    s1 = 'I love Python'

    # test if a1 is equal to a3
    print('Is a1 equal to s1?', a1.__eq__(s1))

    # test if a1 is equal to a2
    print('Is a1 equal to a2?', a1.__eq__(a2))

    # change the balance in a2
    a2.credit(75.0)

    # test if a1 is equal to a2
    print('Is a1 equal to a2?', a1.__eq__(a2))

    # display the sum of the balances  in a1 and a2
    print("$%.2f" % account.sum(a1, a2))

    # display the sum of the balances  in a1 and a3
    print("$%.2f" % account.sum(a1, a3))

    # display the sum of the balances  in a1 and s1
    print("$%.2f" % account.sum(a1, s1))

    # transfer $25 out of a1 and put it into a new account named a4
    a4 = account.transfer(a1, 25.0)
    # a4 = account.transfer(a1, -25.0) this line of code results in a ValueError
    # a4 = account.transfer(a1, 2500.0) this line of code results in a ValueError
    # a4 = account.transfer(a3, 25.0) this line of code results in a ValueError
    # a4 = account.transfer(s1, 25.0)

    sa1 = savingsaccount(10000.0, .06)

    print("Balance in sa1 $%.2f" % (sa1.getBalance()))

    print("Interest in sa1 $%.2f" % (sa1.getInterest()))

    print('Is, sa1 empty? ', sa1.isEmpty())

    print(sa1)

    print('Is sa1 equal to a1?', sa1.__eq__(a1))

    print('Is sa1 equal to a3?', sa1.__eq__(a3))

    sa2 = savingsaccount(10000.0, .05)

    print('Is sa1 equal to sa2?', sa1.__eq__(sa2))

    sa2.setInterestRate(.06)

    print('Is sa1 equal to sa2?', sa1.__eq__(sa2))

    sa2.credit(1000.0)

    print("Balance in sa2 $%.2f" % (sa2.getBalance()))

    sa2.debit(1000.0)

    print("Balance in sa2 $%.2f" % (sa2.getBalance()))

    # display the balances in a1 and a4
    print("Balance in a1 $%.2f" % (a1.getBalance()))
    print("Balance in a4 $%.2f" % (a4.getBalance()))

if __name__ == "__main__":
    main()