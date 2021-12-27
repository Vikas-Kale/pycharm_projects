from datetime import datetime
import smtplib
import sqlite3
from email.message import EmailMessage


class BaseConfig:
    """
    All common things for configurations are:
        - database
        - smtp
        - message logging
    """

    def setup_db_conn(self):
        try:
            conn = sqlite3.connect('bank.db')
            conn.execute(
                'create table IF NOT EXISTS customer(account_no int, password text, name text, email text, amount INTEGER, account_type text, account_pin text)')
            conn.execute(
                'create table IF NOT EXISTS employee(account_no int, password text,name text, email text, amount INTEGER, account_type text, account_pin text)')
        except Exception as e:
            print("Error Occured ", e)
            assert False
        else:
            return conn

    def setup_smtp(self):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('kalevikas7798@gmail.com', '9422119274')
        return smtp

    def send_mail(self, smtp_obj, usr_subject, usr_message):
        try:
            message = EmailMessage()
            message['Subject'] = "".format(usr_subject)
            message['From'] = 'kalevikas7798@gmail.com'
            message['To'] = 'vkale4938@gmail.com'
            message.set_content("""
            <html>
            <body>
                {}
            </body>
            </html>
            """.format(usr_message), subtype='html')

            smtp_obj.send_message(message)
            smtp_obj.quit()
        except Exception as e:
            print("Error occured : ", e)
            assert False
        else:
            print("############ Mail Send ############")


class Bank(BaseConfig):
    BANK_NAME = 'SBI'

    def __init__(self):
        """
        Call required methods
        """
        smtp = self.setup_smtp()
        conn = self.setup_db_conn()

    def _generate_account_no(self):
        """
        Generate account number and return it.
        """
        return self.BANK_NAME + datetime.now().strftime('%d%Y%M%S')

    def _auth(self, account_no, account_pin):
        """
        Validate the user
        """
        try:
            result = self.conn.execute(
                "select * from customer where account_no= '{}' and account_pin={}".format(account_no, account_pin))
            if len(result) == 0:
                assert False, 'No record found'
        except Exception as e:
            print("Error occured: ", e)
            assert False, "Error while fetching account details"
        else:
            print("Account number is ", account_no)

    def check_balance(self, username, account_pin):
        """
        Validate user and password and print total avaliable balance in bank.
        """
        pass

    def create_account(self):
        """
        Override this method inside a child class Customer.
        """
        pass

    def is_account_valid(self, account_type):
        assert account_type.lower in ['saving', 'current'], "Account Type Is Not Valid"

    def print_all_customers_data(self):
        print(self.conn("select * from customer").fetchall())

    def print_all_employee_data(self):
        print(self.conn("select * from employee").fetchall())


class Customer(Bank):
    def create_account(self, name, email, account_pin, account_type, amount):
        """
        create_account:
            Returns
                - Account Number
        """
        self.is_account_valid(account_type)
        account_no = self._generate_account_no()
        try:
            self.conn.execute(
                'insert into customer values({},{},{},{},{})'.format(account_no, name, email, amount, account_type,
                                                                     account_pin))
        except Exception as e:
            print("Error occured: ", e)
            assert False, "Error while creating account"
        else:
            print("Account number is ", account_no)

    def _check_balance(self, account_no, account_pin):
        """
        Check balance based on account_no and password.
        If one of the value is flase return not valid user.
        """
        self._auth(account_no, account_pin)

    def deposit(self, account_no, account_pin, amount):
        """
        Deposit amount based on account no
        """
        self._auth(account_no, account_pin)
        if amount > 0:
            result = self.conn.execute("select amount from customer where account_no={} ")
            amt = result.fetchall()[0][0]
            print("Before deposit your ammount is ", amount)
            amount = amt + amount
            self.conn.execute("update customer set amount= {} where account_no={} ".format(amount))
        else:
            print("Amount is not valid")

    def _withdraw(self, account_no, account_pin, amount):
        """
        withdraw amount based on account no
        """
        self._auth(account_no, account_pin)
        if amount > 0:
            result = self.conn.execute("select amount from customer where account_no={} ")
            amt = result.fetchall()[0][0]
            print("Before deposit your ammount is ", amount)
            if amt < 500:
                print("Amount is less than 500 you cannot withdraw")
                assert False, 'Amount is less'
            amount = amt - amount
            self.conn.execute("update customer set amount= {} where account_no={} ".format(amount))
        else:
            print("Amount is not valid")


class Employee(Bank):
    def create_account(self, name, email, account_pin, account_type, amount):
        """
        create_account:
            Returns
                - Account Number
        """
        self.is_account_valid(account_type)
        account_no = self._generate_account_no()
        try:
            self.conn.execute(
                'insert into employee values({},{},{},{},{})'.format(account_no, name, email, amount, account_type,
                                                                     account_pin))
        except Exception as e:
            print("Error occured: ", e)
            assert False, "Error while creating account"
        else:
            print("Account number is ", account_no)

    def _check_balance(self, account_no, account_pin):
        """
        Check balance based on account_no and password.
        If one of the value is flase return not valid user.
        """
        self._auth(account_no, account_pin)

    def deposit(self, account_no, account_pin, amount):
        """
        Deposit amount based on account no
        """
        self._auth(account_no, account_pin)
        if amount > 0:
            result = self.conn.execute("select amount from employee where account_no={} ")
            amt = result.fetchall()[0][0]
            print("Before deposit your ammount is ", amount)
            amount = amt + amount
            self.conn.execute("update employee set amount= {} where account_no={} ".format(amount))
        else:
            print("Amount is not valid")

    def _withdraw(self, account_no, account_pin, amount):
        """
        withdraw amount based on account no
        """
        self._auth(account_no, account_pin)
        if amount > 0:
            result = self.conn.execute("select amount from employee where account_no={} ")
            amt = result.fetchall()[0][0]
            print("Before deposit your ammount is ", amount)
            if amt < 500:
                print("Amount is less than 500 you cannot withdraw")
                assert False, 'Amount is less'
            amount = amt + amount
            self.conn.execute("update employee set amount= {} where account_no={} ".format(amount))
        else:
            print("Amount is not valid")


def main():
    cust = Customer()
    emp = Employee()
    bnk = Bank()
    while True:
        print("########### WELCOME TO SBI BANK ###########")
        print("Are you Customer ? Employee")
        usr_input = input("Type Customer C or Type Employee E: ")
        if usr_input == "c" or usr_input == "C":
            print("Select one of the option to continue")
            print("1. Create account\t\t2. Check Balance\t\t")
            print("3. Deposit Amount\t\t4. Withdraw Amount")
            print("5. Close Account\t\t6. Exit")
            usr_choise = input("Enter your choise: ")
            if usr_choise == 1:
                print("Make sure that you should not be already member of SBI Bank")
                name = input("Enter your name: ")
                email = input("Enter your email id: ")
                balance = input("Enter your opening balance: ")
                account_type = input("Enter your account type: ")
                account_pin = input("Enter your pin")
                cust.create_account(name, email, balance, account_type, account, pin)
                self.send_mail(self.send_mail)
                print("############### Account created ###############")

            elif usr_choise == 2:
                account_no = input("Enter your account: ")
                account_pin = input("Enter your pin")
                cust._check_balance(account_no, account_pin)

            elif usr_choise == 3:
                account_no = input("Enter your account: ")
                account_pin = input("Enter your pin")
                amount = int(input("Enter a amount: "))
                if amount > 0:
                    cust.deposit(account_no, account_pin, amount)
                else:
                    print("Amount is not valid")

            elif usr_choise == 4:
                account_no = input("Enter your account: ")
                account_pin = input("Enter your pin")
                amount = int(input("Enter a amount: "))
                if amount > 0:
                    cust._withdraw(account_no, account_pin, amount)
                else:
                    print("Amount is not valid")

            elif usr_choise == 5:
                account_no = input("Enter your account: ")
                account_pin = input("Enter your pin")
                print("Thanks for using SBI Bank!")
            elif usr_choise == 6:
                break
            else:
                print("Enter a valid input")
        elif usr_input == "e" or usr_input == "E":
            print("Select one of the option to continue")
            print("1. Create account\t\t2. Check Balance\t\t")
            print("3. Deposit Amount\t\t4. Withdraw Amount")
            print("5. Close Account")
            usr_choise = input("Enter your choise: ")
            if usr_choise == 1:
                print("Welcome to SBI Employee Portal")
                name = input("Enter your name: ")
                email = input("Enter your email id: ")
                balance = input("Enter your opening balance: ")
                account_type = input("Enter your account type: ")
                account_pin = input("Enter your pin")
                emp.create_account(name, email, balance, account_type, account, pin)
                print("Congratulations now your are employee of SBI Bank")
            elif usr_choise == 2:
                account_no = input("Enter your account: ")
                account_pin = input("Enter your pin")
                emp._check_balance(account_no, account_pin)

            elif usr_choise == 3:
                account_no = input("Enter your account: ")
                account_pin = input("Enter your pin")
                amount = int(input("Enter a amount: "))
                if amount > 0:
                    emp.deposit(account_no, account_pin, amount)
                else:
                    print("Amount is not valid")

            elif usr_choise == 4:
                account_no = input("Enter your account: ")
                account_pin = input("Enter your pin")
                amount = int(input("Enter a amount: "))
                if amount > 0:
                    cust._withdraw(account_no, account_pin, amount)
                else:
                    print("Amount is not valid")

            elif usr_choise == 5:
                pass
            elif usr_choise == 6:
                break
            else:
                print("Enter a valid input")
        elif usr_input == "b" or usr_input == "B":
            print("Select one of the option to continue")
            print("1. Show All Customer Details\t\t2. Show All Employee Details\t\t")
            print("3. Exit")
            usr_choise = input("Enter your choise: ")
            if usr_choise == 1:
                bnk.print_all_customers_data()
            elif usr_choise == 2:
                bnk.print_all_employee_data()
            elif usr_choise == 3:
                break
            else:
                print("Enter a valid input")
        else:
            print("Not a valid input")
            break


if __name__ == '__main__':
    main()
