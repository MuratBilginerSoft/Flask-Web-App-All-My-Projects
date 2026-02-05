# region Import Lib

from controller.settings.projectlib import *

# endregion

# region IndexRoute Oluşturuldu

class Index():

    # region Variables

    url = "index.html"

    # endregion
    
    # region Get

    def Get(self):

        session["status"] = False
        
        try:
            return render_template(self.url)
        except:
            return redirect(url_for("Index"))
    
    # endregion

# endregion