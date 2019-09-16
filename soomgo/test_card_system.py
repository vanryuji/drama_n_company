import unittest
import sys

import card_system


class CardSystemTest(unittest.TestCase):
    def setUp(self):
        self.cmd = 'Add'
        self.name = 'Jane'
        self.card_number = '4111111111111111'
        self.wrong_card_number = '1234567890123456'
        self.credit = 1000
        self.data = [
            ('Add', 'Jane', '4111111111111111', 1000),
            ('Add', 'Evan', '5454545454545454', 3000),
            ('Add', 'Daniel', '1234567890123456', 2000),
            ('Charge', 'Jane', 500),
            ('Charge', 'Jane', 800),
            ('Charge', 'Evan', 7),
            ('Credit', 'Evan', 100),
            ('Credit', 'Daniel', 200),
        ]

    def test_create_account(self):
        jane = card_system.Account(self.name, self.card_number, self.credit)
        jane.charge(20)
        jane.credit(10)
        self.assertEqual(str(jane), 'Jane: $10')

    def test_complex_transactions(self):
        jane = card_system.Account(self.name, self.card_number, self.credit)
        jane.charge(1000)
        jane.charge(600)
        jane.credit(1200)
        self.assertEqual(str(jane), 'Jane: $-200')

    def test_create_account_with_wrong_card_number(self):
        jane = card_system.Account(self.name, self.wrong_card_number, self.credit)
        self.assertEqual(str(jane), 'Jane: error')

    def test_multiple_accounts(self):
        mgr = card_system.AccountManager()
        for data_ in self.data:
            if data_[0] == 'Add':
                mgr.create_new_account(data_[1], data_[2], data_[3])
            elif data_[0] == 'Charge':
                mgr.get_account(data_[1]).charge(data_[2])
            else:  # Credit
                mgr.get_account(data_[1]).credit(data_[2])

        result = list()
        names = mgr.get_all_names()
        for name in names:
            result.append(str(mgr.get_account(name)))
        answer = ['Daniel: error', 'Evan: $-93', 'Jane: $500']
        self.assertListEqual(result, answer)

if __name__ == '__main__':
    unittest.main()
