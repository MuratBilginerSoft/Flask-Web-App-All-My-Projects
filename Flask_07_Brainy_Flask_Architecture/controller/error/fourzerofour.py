# region Import Lib

from controller.settings.projectlib import *

# endregion

# region 404 Class Created

class FourZeroFour():

    # region Variable List

    url = "main/error/404.html"
    
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