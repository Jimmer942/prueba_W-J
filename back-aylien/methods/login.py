#!/usr/bin/env python3

import MySQLdb

def login(data):
    user_name = data['user_name']
    try:
        db = MySQLdb.connect(host="localhost", user="whalejaguar", passwd="whalejaguar", db="whalejaguar")
        cursor = db.cursor()
        query = "SELECT * FROM users WHERE user_name = '" + str(user_name) + "'"
        table = cursor.execute(query)
        aux = cursor.fetchone()
        response = dict()
        response['user_name'] = aux[0]
        response['user_password'] = aux[2]
        return response
    except:
            return {'error': 'Can not show the user {} on the table users because it does not exist'.format(user_name)}