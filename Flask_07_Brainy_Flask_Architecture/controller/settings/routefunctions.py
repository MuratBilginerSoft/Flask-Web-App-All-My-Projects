#region Kütüphaneler

from controller.settings.projectlib import *

#endregion

# region Route Function Class Created

class RouteFunction():

    # region RouteClass

    indexObj = Index()
    logInObj = Login()
    signInObj = SignIn()
    dashboardObj = Dashboard()

    errorObj = Error()
    fourZeroFourObj = FourZeroFour()
    
    # endregion

    # region Index

    def Index(self):

        # region GET

        if request.method == "GET":
            
            return self.indexObj.Get()

        # endregion

        #region Error

        else:
            return redirect(url_for("Index"))

    #endregion

    # endregion

    # region SignIn

    def SignIn(self):

        #region GET

        if request.method == "GET":

            return self.signInObj.Get()
        
        #endregion

        #region POST

        elif request.method == "POST":

            return self.signInObj.Post()

        #endregion

        #region Error

        else:
            return redirect(url_for("Error"))

        #endregion

    # endregion

    # region Login

    def Login(self):

        #region GET

        if request.method == "GET":

            return self.logInObj.Get()
        
        #endregion

        #region POST

        elif request.method == "POST":

            return self.logInObj.Post()

        #endregion

        #region Error

        else:
            return redirect(url_for("Error"))

        #endregion

    #endregion

    # region Dashboard
    
    def Dashboard(self):

        #region GET

        if request.method == "GET" and session["Status"]:

            return self.dashboardObj.Get()
        
        #endregion

        #region POST

        elif request.method == "POST" and session["Status"]:

            pass

        #endregion

        #region Error

        else:
            return redirect(url_for("Error"))
        
        #endregion

    #endregion

    # region Error

    def Error(self):

        # region Get

        return self.errorObj.Get()

        # endregion

    #endregion

    # region Logout

    def Logout(self):

        session["Status"] = False

        return redirect(url_for("Index"))

    #endregion

# endregion