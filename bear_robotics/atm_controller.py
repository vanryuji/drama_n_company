"""
요구사항
- Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
    - 카드넘버와 PIN 넘버는 주어짐
    - 주어진 정보로 계좌를 선택
    - 잔액 확인, 인출, 입금 기능 가능
- 테스트 코드도 필요함
"""


from pprint import pprint


# 은행에 저장된 고객 및 계좌 정보
user_card_number = '1111222233334444'
user_pin_number = '0000'
user_accounts = [
    {'account_index': 1, 'account_number': '11-22-33-44', 'account_name': '생활비'},
    {'account_index': 2, 'account_number': '11-22-33-55', 'account_name': '전재산'}
]
user_accounts_detail = {
    1: {'account_index': 1, 'account_number': '11-22-33-44', 'account_name': '생활비', 'balance': 123},
    2: {'account_index': 2, 'account_number': '11-22-33-55', 'account_name': '전재산', 'balance': 456}
}


# Bank API
def list_accounts(card_number, pin_number):
    """
    Bank API
    계좌 리스트 조회

    :param card_number: 카드 번호
    :param pin_number: 핀 코드
    :return: {
        'success': False,
        'data': [{'account_index': 1, 'account_number': '11-22-33-44', 'account_name': '생활비'}] or [],
        'error_message': None
    }
    """

    response = {
        'success': False,
        'data': [],
        'error_message': None
    }

    if card_number == user_card_number and pin_number == user_pin_number:
        response['success'] = True
        response['data'] = user_accounts
    else:
        response['error_message'] = '카드와 PIN이 일치하지 않습니다'

    return response


def retrieve_account(card_number, pin_number, account_index):
    """
    Bank API
    계좌 상세 조회

    :param card_number: 카드 번호
    :param pin_number: 핀 코드
    :param account_index: 계좌 인덱스
    :return: {
        'success': False,
        'data': {
            'account_index': 1,
            'account_number': '11-22-33-44',
            'account_name': '생활비',
            'balance': 1234
        } or {},
        'error_message': None
    }
    """

    response = {
        'success': False,
        'data': {},
        'error_message': None
    }

    if card_number == user_card_number and pin_number == user_pin_number:
        if account_index in user_accounts_detail:
            response['success'] = True
            response['data'] = user_accounts_detail[account_index]
        else:
            response['error_message'] = '요청한 계좌가 존재하지 않습니다'
    else:
        response['error_message'] = '카드와 PIN이 일치하지 않습니다'

    return response


def withdraw(card_number, pin_number, account_index, amount):
    """
    Bank API
    출급하기

    :param card_number: 카드 번호
    :param pin_number: 핀 코드
    :param account_index: 계좌 인덱스
    :param amount: 입금할 금액
    :return: {
        'success': False,
        'error_message': None
    }
    """

    response = {
        'success': False,
        'error_message': None
    }

    if not (card_number == user_card_number and pin_number == user_pin_number):
        response['error_message'] = '카드와 PIN이 일치하지 않습니다'
        return response

    if account_index not in user_accounts_detail:
        response['error_message'] = '요청한 계좌가 존재하지 않습니다'
        return response

    account = user_accounts_detail[account_index]
    if amount > account['balance']:
        response['error_message'] = '잔액보다 많은 금액은 인출할 수 없습니다'
        return response

    account['balance'] -= amount
    response['success'] = True

    return response


def deposit(card_number, pin_number, account_index, amount):
    """
    Bank API
    입금하기

    :param card_number: 카드 번호
    :param pin_number: 핀 코드
    :param account_index: 계좌 인덱스
    :param amount: 입금할 금액
    :return: {
        'success': False,
        'error_message': None
    }
    """

    response = {
        'success': False,
        'error_message': None
    }

    if not (card_number == user_card_number and pin_number == user_pin_number):
        response['error_message'] = '카드와 PIN이 일치하지 않습니다'
        return response

    if account_index not in user_accounts_detail:
        response['error_message'] = '요청한 계좌가 존재하지 않습니다'
        return response

    user_accounts_detail[account_index]['balance'] += amount
    response['success'] = True

    return response


class ATMController(object):
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def list_accounts(self):
        """
        Bank API를 이용하여 card_number와 연결된 모든 계좌를 리스팅함

        :return: [{'account_index': 1, 'account_number': '11-22-33-44', 'account_name': '생활비'}] or [],
        """

        return list_accounts(self.card_number, self.pin_number)['data']

    def retrieve_account(self, account_index):
        """
        Bank API를 이용하여 계좌 상세 정보를 조회함

        :param account_index: 계좌 index
        :return: {
            'account_index': 1,
            'account_number': '11-22-33-44',
            'account_name': '생활비',
            'balance': 1234
        } or {}
        """

        return retrieve_account(self.card_number, self.pin_number, account_index)['data']

    def withdraw(self, account_index, amount):
        """
        Bank API를 이용하여 계좌에서 인출

        :param account_index: 계좌 index
        :param amount: 인출 금액
        :return: True or False
        """

        return withdraw(self.card_number, self.pin_number, account_index, amount)['success']

    def deposit(self, account_index, amount):
        """
        Bank API를 이용하여 계좌에 입금

        :param account_index: 계좌 index
        :param amount: 입금 금액
        :return: True or False
        """

        return deposit(self.card_number, self.pin_number, account_index, amount)['success']


if __name__ == '__main__':
    atm = ATMController(user_card_number, user_pin_number)

    print('## 고객 계좌 리스트 ##')
    pprint(atm.list_accounts())

    print('\n## 2번 계좌 조회 ##')
    pprint(atm.retrieve_account(2))

    print('\n## 2번 계좌에서 1000달러 인출')
    print(atm.withdraw(2, 1000))

    print('\n## 2번 계좌에서 100달러 인출')
    print(atm.withdraw(2, 100))

    print('\n## 2번 계좌 조회 ##')
    pprint(atm.retrieve_account(2))

    print('\n## 2번 계좌에서 1000달러 입금 ##')
    pprint(atm.deposit(2, 1000))

    print('\n## 2번 계좌 조회 ##')
    pprint(atm.retrieve_account(2))

