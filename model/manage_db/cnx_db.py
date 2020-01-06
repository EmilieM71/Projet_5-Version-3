import logging
from config import USER, PASSWORD, HOST, DB_NAME
from mysql import connector
from mysql.connector import errorcode


class CnxDatabase:
    """ This class is responsible for connecting to the database """

    def __init__(self):
        self._cnx = None

    def _get_cnx(self):
        """Method for accessing the 'cnx' attribute"""
        if self._cnx is None:
            self._cnx = self.connection()
        return self._cnx

    cnx = property(_get_cnx)

    def connection(self):
        """ this method is responsible for connecting to mysql with the
            demo profile:
            - HOST = 'localhost'
            - USER = 'student_OC'
            - PASSWORD = '123abc'
            - DB_NAME = 'PurBeurre'
                """
        config = {
            'user': USER,
            'password': PASSWORD,
            'host': HOST,
            'database': DB_NAME
        }
        try:
            self._cnx = connector.connect(**config)
        except connector.Error:
            try:
                config["auth_plugin"] = "mysql_native_password"
                self._cnx = connector.connect(**config)
            except connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    logging.ERROR("Something is wrong with your user name or "
                                  "password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    # logging.INFO("Database does not exist")
                    self.connection_mysql()
                else:
                    logging.ERROR(err)
        finally:
            return self._cnx

    def connection_mysql(self):
        """ this method is responsible for connecting to mysql with the
            demo profile:
            - HOST = 'localhost'
            - USER = 'student_OC'
            - PASSWORD = '123abc'
                """
        config = {
            'user': USER,
            'password': PASSWORD,
            'host': HOST
        }
        try:
            self._cnx = connector.connect(**config)
        except connector.Error:
            try:
                config["auth_plugin"] = "mysql_native_password"
                self._cnx = connector.connect(**config)
            except connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    logging.ERROR("Something is wrong with your user name or "
                                  "password")
                else:
                    logging.ERROR(err)
        finally:
            return self._cnx


if __name__ == "__main__":
    pass
