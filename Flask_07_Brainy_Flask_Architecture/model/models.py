# region Import Lib

from flask_sqlalchemy import SQLAlchemy
import datetime

#endregion

# region Create Database

DB = SQLAlchemy()

#endregion

# region Migrate Command

"""
Database Migration İşlemi İçin Aşağıdaki İşlemleri Uygulayınız.

1. python manage.py db init

2. python manage.py db migrate

3. python manage.py db upgrade

"""

#endregion

# region Base Model

class BaseModel(DB.Model):
    
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
       
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

# endregion

# region Your Database Table Models

class TestTable(BaseModel, DB.Model):

    __tablename__ = "testtable"

    id = DB.Column(DB.Integer, primary_key = True, autoincrement=True)
    userid = DB.Column(DB.Integer, unique = True)
    username = DB.Column(DB.String(), unique = True)
    password = DB.Column(DB.String())
    companyname = DB.Column(DB.String())

    def __init__(self,userid,username,password,companyname):
        self.userid = userid
        self.username = username
        self.password =  password
        self.companyname = companyname

# endregion