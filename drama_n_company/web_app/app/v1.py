import datetime
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


from db.db import User, get_session, __test_init_db, Dispatch, cvt_result


def create_user(email, passwd, driver):
    """
    :param email:
    :param passwd:
    :param driver:
    :return: True or False
    """

    try:
        session = get_session()
        user = User(email=email, passwd=passwd, driver=driver)
        session.add(user)
        session.commit()  # sqlalchemy.exc.IntegrityError
    except IntegrityError:
        return False
    return True


def login(email, passwd):
    """
    :param email:
    :param passwd:
    :return: True or False
    """

    try:
        session = get_session()
        session.query(User).\
            filter(User.email == email, User.passwd == passwd).one()  # sqlalchemy.orm.exc.NoResultFound
    except NoResultFound:
        return False
    return True


def validate_customer(email):
    """
    :param email:
    :return: True or False
    """

    user = get_user(email)
    if user is None:
        return False
    if user.driver == 't':
        return False
    return True


def request_dispatch(email, address):
    """
    :param email:
    :param address:
    :return: True or False
    """

    session = get_session()
    dispatch = Dispatch(customer=email, address=address)
    session.add(dispatch)
    session.commit()
    return True


def get_user(email):
    """
    :param email:
    :return: db.db.User or None
    """

    try:
        session = get_session()
        user = session.query(User).filter(User.email == email).one()  # sqlalchemy.orm.exc.NoResultFound
    except NoResultFound:
        return None
    return user


DISPATCH_TYPE_WAIT = 'wait'
DISPATCH_TYPE_COMPLETE = 'complete'


def get_dispatches(dispatch_type=None):
    """
    :param dispatch_type: None, wait or complete
    :return: [{...}]
    """

    session = get_session()
    if dispatch_type is None:
        return cvt_result(session.query(Dispatch).order_by(desc(Dispatch.id)).all())
    elif dispatch_type == DISPATCH_TYPE_WAIT:
        return cvt_result(session.query(Dispatch).
                          filter(Dispatch.driver == None).
                          order_by(desc(Dispatch.id)).
                          all())
    elif dispatch_type == DISPATCH_TYPE_COMPLETE:
        return cvt_result(session.query(Dispatch).
                          filter(Dispatch.driver != None).
                          order_by(desc(Dispatch.id)).
                          all())
    else:
        return []


def validate_driver(email):
    """
    :param email:
    :return: True or False
    """

    user = get_user(email)
    if user is None:
        return False
    if user.driver == 'f':
        return False
    return True


def response_dispatch(dispatch_id, email):
    """
    :param dispatch_id:
    :param email:
    :return: True or False
    """

    session = get_session()
    result = session.query(Dispatch).filter(Dispatch.id == dispatch_id, Dispatch.driver == None).\
        update({Dispatch.driver: email, Dispatch.res_time: datetime.datetime.now()})
    session.commit()
    if result > 0:
        return True
    else:
        return False


def __test_create_duplicate_user():
    __test_init_db()
    print('result of create_user():', create_user('a@gmail.com', 'aa', 'f'))
    session = get_session()
    pprint.pprint(session.query(User).all())


def __test_create_user():
    __test_init_db()
    print('result of create_user():', create_user('c@gmail.com', 'cc', 'f'))
    session = get_session()
    pprint.pprint(session.query(User).all())


def __test_login():
    __test_init_db()
    print('result of login():', login('a@gmail.com', 'aa'))


def __test_wrong_login():
    __test_init_db()
    print('result of login():', login('a@gmail.com', 'bb'))


def __test_request_dispatch():
    __test_init_db()
    print('result of request_dispatch():', request_dispatch('b@gmail.com', 'gangnam-gu'))
    pprint.pprint(get_session().query(Dispatch).all())


def __test_get_user():
    __test_init_db()
    user = get_user('a@gmail.com')
    print('result of get_user():', user)
    print('result of get_user():', user.email)


def __test_get_wrong_user():
    __test_init_db()
    user = get_user('aa@gmail.com')
    print('result of get_user():', user)


def __test_get_all_dispatches():
    result = get_dispatches()
    pprint.pprint(result)
    print(result[0]['address'])


def __test_get_all_wait_dispatches():
    result = get_dispatches('wait')
    pprint.pprint(result)
    print(result[0]['address'])


def __test_get_all_complete_dispatches():
    result = get_dispatches('complete')
    pprint.pprint(result)
    print(result[0]['address'])


def __test_get_all_dispatches_with_wrong_param():
    result = get_dispatches('complete11111')
    pprint.pprint(result)


def __test_response_dispatch():
    __test_init_db()
    print(response_dispatch(3, 'aa@gmail.com'))
    pprint.pprint(get_dispatches())
    print(response_dispatch(3, 'a@gmail.com'))


if __name__ == '__main__':
    import pprint

    # __test_create_duplicate_user()
    # __test_create_user()
    # __test_login()
    # __test_wrong_login()
    # __test_get_user()
    # __test_get_wrong_user()
    # __test_request_dispatch()
    # __test_request_wrong_dispatch()
    # __test_get_all_dispatches()
    # __test_get_all_wait_dispatches()
    # __test_get_all_complete_dispatches()
    # __test_get_all_dispatches_with_wrong_param()
    # __test_response_dispatch()
