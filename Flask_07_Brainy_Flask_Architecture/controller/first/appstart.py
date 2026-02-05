#region Proje Kütüphaneleri

from controller.settings.projectlib import *

#endregion

#region FlaskStart Classı

class FlaskStart():

    app = None # Flask Sınıfınran Türeyen Bir Nesne Olarak Devam Edecek.

    __name__ = None
    
    def __init__(self,app,__name__):
        self.app = app
        self.__name__ = __name__

    def Start(self):
        if self.__name__ == "__main__":
            self.app.run(host='0.0.0.0', port=8080, use_reloader=True)
        
#endregion