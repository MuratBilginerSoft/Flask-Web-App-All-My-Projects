# region Import Lib

from controller.settings.projectlib import *

# endregion

# region Dashboard Class Created

class Dashboard():

    # region Variable List

    url = "index.html"
    
    # endregion

    # region Get

    def Get(self):

        return render_template(self.url)

    # endregion

    # region Post

    def Post(self):

        return render_template(self.url)

    # endregion

# endregion