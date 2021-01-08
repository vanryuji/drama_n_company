from unittest import TestCase

import atm_controller


class ATMControllerTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.invalid_card_number = '9999888877776666'
        cls.valid_card_number = '1111222233334444'

        cls.pin_number = '0000'

        cls.invalid_account_index = 100
        cls.valid_account_index = 1

    def setUp(self):
        atm_controller.user_card_number = '1111222233334444'
        atm_controller.user_pin_number = '0000'
        atm_controller.user_accounts = [
            {'account_index': 1, 'account_number': '11-22-33-44', 'account_name': '생활비'},
            {'account_index': 2, 'account_number': '11-22-33-55', 'account_name': '전재산'}
        ]
        atm_controller.user_accounts_detail = {
            1: {'account_index': 1, 'account_number': '11-22-33-44', 'account_name': '생활비', 'balance': 123},
            2: {'account_index': 2, 'account_number': '11-22-33-55', 'account_name': '전재산', 'balance': 456}
        }

    def test_list_accounts_with_invalid_card(self):
        atm = atm_controller.ATMController(self.invalid_card_number, self.pin_number)
        expected_value = []
        self.assertListEqual(expected_value, atm.list_accounts())

    def test_list_accounts(self):
        atm = atm_controller.ATMController(self.valid_card_number, self.pin_number)
        expected_value = [
            {'account_index': 1, 'account_number': '11-22-33-44', 'account_name': '생활비'},
            {'account_index': 2, 'account_number': '11-22-33-55', 'account_name': '전재산'}
        ]
        self.assertListEqual(expected_value, atm.list_accounts())

    def test_retrieve_account_with_invalid_card(self):
        atm = atm_controller.ATMController(self.invalid_card_number, self.pin_number)
        expected_value = {}
        self.assertDictEqual(expected_value, atm.retrieve_account(self.valid_account_index))

    def test_retrieve_account_with_invalid_account_index(self):
        atm = atm_controller.ATMController(self.valid_card_number, self.pin_number)
        expected_value = {}
        self.assertDictEqual(expected_value, atm.retrieve_account(self.invalid_account_index))

    def test_retrieve_account(self):
        atm = atm_controller.ATMController(self.valid_card_number, self.pin_number)
        expected_value = {'account_index': 1, 'account_number': '11-22-33-44', 'account_name': '생활비', 'balance': 123}
        self.assertDictEqual(expected_value, atm.retrieve_account(self.valid_account_index))

    def test_withdraw_with_invalid_card(self):
        atm = atm_controller.ATMController(self.invalid_card_number, self.pin_number)
        self.assertFalse(atm.withdraw(self.valid_account_index, 10))

    def test_withdraw_with_invalid_account_index(self):
        atm = atm_controller.ATMController(self.valid_card_number, self.pin_number)
        self.assertFalse(atm.withdraw(self.invalid_account_index, 10))

    def test_withdraw_with_more_money_than_saved(self):
        atm = atm_controller.ATMController(self.valid_card_number, self.pin_number)
        self.assertFalse(atm.withdraw(self.valid_account_index, 1000000))

    def test_withdraw(self):
        atm = atm_controller.ATMController(self.valid_card_number, self.pin_number)
        self.assertTrue(atm.withdraw(self.valid_account_index, 10))

        expected_value = 113
        self.assertEqual(expected_value, atm.retrieve_account(self.valid_account_index)['balance'])

    def test_deposit_with_invalid_card(self):
        atm = atm_controller.ATMController(self.invalid_card_number, self.pin_number)
        self.assertFalse(atm.deposit(self.valid_account_index, 10))

    def test_deposit_with_invalid_account_index(self):
        atm = atm_controller.ATMController(self.valid_card_number, self.pin_number)
        self.assertFalse(atm.deposit(self.invalid_account_index, 10))

    def test_deposit(self):
        atm = atm_controller.ATMController(self.valid_card_number, self.pin_number)
        self.assertTrue(atm.deposit(self.valid_account_index, 1000))

        expected_value = 1123
        self.assertEqual(expected_value, atm.retrieve_account(self.valid_account_index)['balance'])
