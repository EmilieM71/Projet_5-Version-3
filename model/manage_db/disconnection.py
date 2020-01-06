import logging


class Disconnection:
    """ This class is responsible for disconnection """

    def __init__(self, cnx):
        """ Connection with the MySQL server
        :param cnx: CMySQL.connection (Connection with the MySQL server can be
        made using the mysql.connector.connect() method or the
        mysql.connector.MySQLConnection() class.)
        """
        self.cnx = cnx

    def __exit__(self):
        """ This method close the connection """
        self.cnx.close()
        logging.INFO("closed connection")
