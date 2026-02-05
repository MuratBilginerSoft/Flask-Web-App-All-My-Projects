# region Import Lib

import os

# endregion

# region Database Config Info

if os.name == "nt": # Eğer İşletim Sistemi Windows İse

   sqliteConfig = { 
      'sqlitePath' : '\\assets\\database\\', # Testte Bu Satır Kullanılacak
      'sqliteDb' : 'testdatabase.db'
   }
  

elif os.name == "posix": # İşletim Sistem Linux İse

   sqliteConfig = {
      'sqlitePath' : '/assets/database/', #Canlıda Bu Satır Kullanılacak 
      'sqliteDb' : 'testdatabase.db'
   }

# endregion

# region DB Url Path

DB_URL = "sqlite:///" + os.getcwd() + sqliteConfig['sqlitePath'] + sqliteConfig['sqliteDb']

# endregion
