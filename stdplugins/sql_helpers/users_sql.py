from sqlalchemy import Column, String
from stdplugins.sql_helpers import SESSION, BASE


class userlist(BASE):
    __tablename__ = "userlist"
    userId = Column(String(14), primary_key=True)
    isBanned = Column(String(100))

    def __init__(self, userId, isBanned):
        self.userId = userId
        self.isBanned = isBanned

userlist.__table__.create(checkfirst=True)


def is_banned(userId):
    try:
        return SESSION.query(userlist).filter(userlist.userId == str(userId)).one()
    except:
        return None
    finally:
        SESSION.close()
        

def get_all_users():
    rem = SESSION.query(userlist).all()
    SESSION.close()
    return rem
