# -*- coding:utf-8 -*-


import luhn
import sys


class Account(object):
    def __init__(self, name, card_number, limit_credit):
        """
        account 생성자
        :param name: name
        :param card_number: card number
        :param limit_credit: 한도
        """

        self.__name = name
        self.__card_number = card_number
        self.__limit_credit = limit_credit
        self.__credit = 0
        self.__is_luhn10_err = self.__validate_card_number()

    def __validate_card_number(self):
        """
        카드번호를 Luhn 10 algorithm으로 검증
        :return: True or False
        """

        return not luhn.verify(self.__card_number)

    def charge(self, credit):
        """
        credit 만큼 충전
        :param credit: 적립 금액
        :return:
            - -1: Luhn 10 검증 실패
            - 0: 충전 실패
            - 1: 충전 성공
        """

        if self.__is_luhn10_err:
            return -1

        if self.__limit_credit < (self.__credit+credit):
            return 0
        else:
            self.__credit += credit
            return 1

    def credit(self, credit):
        """
        credit 만큼 사용
        :param credit: 사용 금액
        :return: True or False
        """

        if self.__is_luhn10_err:
            return False
        self.__credit -= credit
        return True

    def __str__(self):
        return '{}: error'.format(self.__name) if self.__is_luhn10_err else '{}: ${}'.format(self.__name, self.__credit)


class AccountManager(object):
    def __init__(self):
        self.__accounts = dict()  # key: Account.name, value: Account obj

    def create_new_account(self, name, card_number, limit_credit):
        """
        새로운 account를 만듬
        :param name: name
        :param card_number: card number
        :param limit_credit: 한도
        :return: True or False
        """

        if self.get_account(name) is not None:
            return False
        self.__accounts[name] = Account(name, card_number, limit_credit)
        return True

    def get_account(self, name):
        """
        이름에 해당하는 Account instance 반환
        :param name:
        :return: Account instance or None
        """

        try:
            return self.__accounts[name]  # KeyError
        except KeyError:
            return None

    def show_all_accounts(self):
        """
        모든 account를 출력, 알파벳순(이름)
        """

        names = self.get_all_names()
        for name in names:
            sys.stdout.write(str(self.get_account(name)) + '\n')

    def get_all_names(self):
        """
        모든 account 이름 반환, 알파벳순(이름)

        :return: 모든 account 이름
        """

        names = list(self.__accounts.keys())
        names.sort()
        return names
