# -*- coding:utf-8 -*-

# TODO : hangul support refactoring for (sqlite + sqlalchemy)
# supporting for hangul encoding
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base


# for support foreign key in sqlite
# https://docs.sqlalchemy.org/en/13/dialects/sqlite.html?highlight=sqlite#foreign-key-support
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(20), unique=True, nullable=False)
    passwd = Column(String(20), nullable=False)
    driver = Column(String(1), nullable=False)  # 't' or 'f'
    # TODO : check constraint for driver
    # TODO : fixed size???

    def __repr__(self):
        return "<User(id=%d, email='%s', driver='%s')>" % (self.id, self.email, self.driver)


class Dispatch(Base):
    __tablename__ = 'dispatches'

    id = Column(Integer, primary_key=True)
    customer = Column(String(20), ForeignKey('users.email'), nullable=False)
    req_time = Column(DateTime, default=datetime.datetime.now, nullable=False)
    address = Column(String(100), nullable=False)
    driver = Column(String(20), ForeignKey('users.email'))
    res_time = Column(DateTime)

    def __repr__(self):
        return "<Dispatch(id=%d, customer='%s', req_time='%s', address='%s', driver='%s', res_time='%s')>" %\
               (self.id, self.customer, self.req_time, self.address, self.driver, self.res_time)


db_path = 'sqlite:///{}/db.db'.format(os.path.dirname(os.path.abspath(__file__)))
engine = create_engine(db_path, echo=True, convert_unicode=True)


def get_session():
    """
    :return: sqlalchemy.orm.scoping.scoped_session
    """
    return scoped_session(sessionmaker(bind=engine))


def cvt_result(result):
    """
    :param result:
    :return: [{...}] or {...}
    """
    if type(result) == list:
        list_result = list()
        for r in result:
            tmp = r.__dict__
            del tmp['_sa_instance_state']
            list_result.append(tmp)
        return list_result
    else:
        tmp = result.__dict__
        del tmp['_sa_instance_state']
        return tmp


def __test_init_db():
    import pprint

    print('before creating, tables:', engine.table_names())
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(engine)
    print('after creating, tables:', engine.table_names())

    db_session = get_session()
    a_user = User(email='a@gmail.com', passwd='aa', driver='t')
    db_session.add(a_user)
    b_user = User(email='b@gmail.com', passwd='bb', driver='f')
    db_session.add(b_user)
    db_session.commit()
    pprint.pprint(db_session.query(User).all())

    dispatch1 = Dispatch(customer='b@gmail.com', address=unicode('노원구'), driver='a@gmail.com', res_time=datetime.datetime.now())
    db_session.add(dispatch1)
    dispatch2 = Dispatch(customer='b@gmail.com', address=unicode('동대문구'), driver='a@gmail.com', res_time=datetime.datetime.now())
    db_session.add(dispatch2)
    dispatch3 = Dispatch(customer='b@gmail.com', address=unicode('강남구'))
    db_session.add(dispatch3)
    db_session.commit()
    pprint.pprint(db_session.query(Dispatch).all())
    print(db_session.query(Dispatch).filter(Dispatch.address == unicode('노원구')).all())


if __name__ == '__main__':
    __test_init_db()


