
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:15:31 2022

@author: Mario
"""
from decouple import config
import mysql.connector as c




def get_points(username, password, hostname, database, port):
    try:
        db = c.connect(user="{0}".format(username), password="{0}".format(password),
                       host="{0}".format(hostname), database="{0}".format(database), port="{0}".format(port))
        return db
    except Exception as ex:
        return "Error to connect to MySQL: {0}".format(ex)


def get_connection():
    try:
        return get_points(
            config('USERNAME_MYSQL_AWS'),
            config('PASSWORD_MYSQL_AWS'),
            config('HOSTNAME_MYSQL_AWSS'),
            config('DATABASE_MYSQL_AWS'),
            config('PORT_MYSQL')
        )
    except Exception as ex:
        raise ex
