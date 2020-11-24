#!/usr/bin/env python3

import MySQLdb


def create_user(data):
    db = MySQLdb.connect(host="localhost", user="whalejaguar", passwd="whalejaguar", db="whalejaguar")
    cursor = db.cursor()
    try:
        query = "INSERT INTO users("
        values = "VALUES ("
        sep = ""
        for key, value in data.items():
            query = query + sep + key
            values = values + sep + "'" + value + "'"
            sep = ", "
        query = query + ") " + values + ") "
        cursor.execute(query)
        db.commit()
        db.close()
        return {'message': "success creating {} on users".format(data)}
    except:
        db.close()
        return {'error': 'Missing foreign key'}