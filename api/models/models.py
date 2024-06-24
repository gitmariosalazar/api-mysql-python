# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:54:16 2023

@author: Mario
"""

from .entities import entities as entity
from database import connectdb as conn
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class Model:

    @classmethod
    def delete_user(self, id, password):
        try:
            connection = conn.get_connection()
            user = self.get_userbyusername(id)
            if check_password_hash(user.get('user')['password'], password):
                with connection.cursor() as cursor:
                    cursor.execute(
                        "update users set user_delete = 1 where user_name = '{0}'".format(id))
                    row_affects = cursor.rowcount
                    connection.commit()
                    if row_affects > 0:
                        return 1
                    else:
                        return 0
            else:
                return -1
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def setEnable(self,state):
        if(state==1):
            return 0
        else:
            return 1

    @classmethod
    def setenable_user(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                user = self.get_userbyusername(id)
                if user:
                    user_state = user.get('user')['user_state']
                    
                    cursor.execute(
                        "update users set user_state = '{0}' where user_name = '{1}'".format(self.setEnable(user_state), id))
                    row_affects = cursor.rowcount
                    connection.commit()
                    if row_affects > 0:
                        return 1
                    else:
                        return 0
                else:
                    return -1
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_genders(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select * from gender order by id_gender asc;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.genderList(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_rols(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute("select * from rol_user order by id_rol asc;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.rolList(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_knowledgwlevels(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from knowledge_level kl order by kl.id_knowledge_level asc;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.knowledgeLevelList(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_language(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from language_learned where id_langlearn = {0}".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return 1
                else:
                    return 0
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_LanguagesProgramming(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from language_programming lp inner join language_type lt on lp.language_type = lt.id_langtype;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.languageProgrammingList(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_users(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from gender g inner join person p on p.gender = g.id_gender inner join users u on u.person = p.id_person inner join rol_user ru on ru.id_rol = u.rol_user where u.user_delete = 0 order by u.id_user desc;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.ListUsers(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_languages(self):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from language_type lt inner join language_programming lp on lt.id_langtype = lp.language_type inner join language_learned ll on ll.language_programming = lp.id_language inner join knowledge_level kl on kl.id_knowledge_level = ll.knowledge_level;")
            rows = cursor.fetchall()
            if rows:
                return entity.Entity.languageLearnedList(rows)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_languagesbyuser(self, username):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from language_type lt inner join language_programming lp on lt.id_langtype = lp.language_type inner join language_learned ll on ll.language_programming = lp.id_language inner join knowledge_level kl on kl.id_knowledge_level = ll.knowledge_level where ll.user_language = {0} order by lt.id_langtype asc;".format(username))
            row = cursor.fetchall()
            if row:
                return entity.Entity.languageLearnedList(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_educationbyid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select*from education e where e.id_education = {0};".format(id))
            row = cursor.fetchone()
            if row:
                return entity.Entity.educationEntity(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_educationbyuser(self, username):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select*from education e where e.user_education = {0} order by e.id_education asc;".format(username))
            row = cursor.fetchall()
            if row:
                return entity.Entity.educationList(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_education(self, data):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute("insert into education (institution, major, year_start, year_end, description, user_education) values ('{0}', '{1}', {2}, {3}, '{4}', {5});".format(
                    data['institution'], data['major'], data['year_start'], data['year_end'], data['description'], data['user_education']))
                cursor.execute("SELECT LAST_INSERT_ID();")
                id = cursor.fetchone()[0]
                rows_affects = cursor.rowcount
                connection.commit()
                if rows_affects > 0:
                    e = self.get_educationbyid(id)
                    return e
                else:
                    return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_education(self, id, data):
        try:
            connection = conn.get_connection()
            e = self.get_educationbyid(id)
            if e:
                cursor = connection.cursor()
                cursor.execute("update education set institution = '{0}', major = '{1}', year_start = {2}, year_end = {3}, description = '{4}', user_education = {5} where id_education = {6};".format(
                    data['institution'], data['major'], data['year_start'], data['year_end'], data['description'], data['user_education'], id))
                connection.commit()
                rows_affect = cursor.rowcount
                if rows_affect > 0:
                    return self.get_educationbyid(id)
                else:
                    return 0
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_education(self, id):
        try:
            connection = conn.get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from education where id_education = {0}".format(id))
                row_affects = cursor.rowcount
                connection.commit()
                if row_affects > 0:
                    return 1
                else:
                    return 0
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_languagebyid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from language_type lt inner join language_programming lp on lt.id_langtype = lp.language_type inner join language_learned ll on ll.language_programming = lp.id_language inner join knowledge_level kl on kl.id_knowledge_level = ll.knowledge_level where ll.id_langlearn = {0};".format(id))
            row = cursor.fetchone()
            if row:
                return entity.Entity.languageLearnedEntity(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_languagebylu(self, language, user):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from language_type lt inner join language_programming lp on lt.id_langtype = lp.language_type inner join language_learned ll on ll.language_programming = lp.id_language inner join knowledge_level kl on kl.id_knowledge_level = ll.knowledge_level where ll.language_programming = {0} and ll.user_language = {1};".format(language, user))
            row = cursor.fetchone()
            if row:
                return entity.Entity.languageLearnedEntity(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_language(self, data):
        try:
            us = self.get_languagebylu(
                data['language_programming'], data['user_language'])
            if us:
                return -1
            else:
                connection = conn.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute("insert into language_learned (description, knowledge_level, language_programming, user_language) values('{0}', {1}, {2}, {3});".format(
                        data['description'], data['knowledge_level'], data['language_programming'], data['user_language']))
                    cursor.execute("SELECT LAST_INSERT_ID();")
                    id = cursor.fetchone()[0]
                    rows_affects = cursor.rowcount
                    connection.commit()
                    if rows_affects > 0:
                        user = self.get_languagebyid(id)
                        return user
                    else:
                        return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_languagelearn(self, id, data):
        try:
            connection = conn.get_connection()
            language = self.get_languagebyid(id)
            if language:
                cursor = connection.cursor()
                cursor.execute("update language_learned set description = '{0}', knowledge_level = {1} where id_langlearn = {2};".format(
                    data['description'], data['knowledge_level'], id))
                connection.commit()
                rows_affect = cursor.rowcount
                if rows_affect > 0:
                    return self.get_languagebyid(id)
                else:
                    return 0
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_userbyusername(self, username):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from gender g inner join person p on p.gender = g.id_gender inner join users u on u.person = p.id_person inner join rol_user ru on ru.id_rol = u.rol_user where u.user_name = '{0}' and u.user_delete = 0;".format(username))
            row = cursor.fetchone()
            if row:
                return entity.Entity.entityUser(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_userbyemail(self, email):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from gender g inner join person p on p.gender = g.id_gender inner join users u on u.person = p.id_person inner join rol_user ru on ru.id_rol = u.rol_user where u.email = '{0}' and u.user_delete = 0;".format(email))
            row = cursor.fetchone()
            if row:
                return entity.Entity.entityUser(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_userbyid(self, id):
        try:
            connection = conn.get_connection()
            cursor = connection.cursor()
            cursor.execute(
                "select * from gender g inner join person p on p.gender = g.id_gender inner join users u on u.person = p.id_person inner join rol_user ru on ru.id_rol = u.rol_user where u.id_user = '{0}' and u.user_delete = 0;".format(id))
            row = cursor.fetchone()
            if row:
                return entity.Entity.entityUser(row)
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login_user(self, id_user, password):
        try:
            user = self.get_userbyemail(
                id_user) or self.get_userbyusername(id_user)
            if user:
                if check_password_hash(user.get('user')['password'], password) and user.get('user')['user_state'] == 1:
                    return user
                elif check_password_hash(user.get('user')['password'], password) is False:
                    return 2
                elif user.get('user')['user_state'] is False:
                    return 1
            else:
                return -1
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def change_password(self, id, data):
        try:
            connection = conn.get_connection()
            user = self.get_userbyemail(id) or self.get_userbyusername(id)
            rows_affect = -1
            if user:
                if check_password_hash(user.get('user')['password'], data['lastpassword']):
                    hash_pwd = generate_password_hash(data['new_password'])
                    if check_password_hash(hash_pwd, data['rep_password']):
                        if not check_password_hash(user.get('user')['password'], data['new_password']):
                            cursor = connection.cursor()
                            cursor.execute("update users set password = '{0}' where id_user  = {1};".format(
                                hash_pwd, user.get('user')['id_user']))
                            connection.commit()
                            rows_affect = cursor.rowcount
                        else:
                            rows_affect = 4
                    else:
                        rows_affect = 2
                else:
                    rows_affect = 3
            return rows_affect
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_user(self, data):
        try:
            us = self.get_userbyemail(
                data['email']) or self.get_userbyusername('ADM-{0}'.format(data['card_id_person'])) or self.get_userbyusername('PRE-{0}'.format(data['card_id_person'])) or self.get_userbyusername('EMP-{0}'.format(data['card_id_person'])) or self.get_userbyusername('SEC-{0}'.format(data['card_id_person'])) or self.get_userbyusername('CUS-{0}'.format(data['card_id_person']))
            if us:
                return -1
            else:
                connection = conn.get_connection()
                with connection.cursor() as cursor:
                    f = datetime.datetime.now()
                    fecha = "{0}/{1}/{2}".format(f.year, f.month, f.day)
                    cursor.execute("insert into person(card_id_person, first_name, last_name, phone, address, gender, date_born) values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}');".format(
                        data['card_id_person'], data['first_name'], data['last_name'], data['phone'], data['address'], data['gender'], data['date_born']))

                    cursor.execute("SELECT LAST_INSERT_ID();")
                    id_person = cursor.fetchone()[0]
                    print(id_person)
                    iduser = ''
                    if int(data['id_rol']) == 1:
                        iduser = 'PRE-' + data['card_id_person']
                    if int(data['id_rol']) == 2:
                        iduser = 'EMP-' + data['card_id_person']
                    if int(data['id_rol']) == 3:
                        iduser = 'SEC-' + data['card_id_person']
                    if int(data['id_rol']) == 4:
                        iduser = 'CUS-' + data['card_id_person']
                    password = data['password']
                    hashed = generate_password_hash(password)
                    query = "INSERT INTO users(user_name, email, password, login_code, user_state, register_date,person, rol_user, user_delete) values('{0}', '{1}', '{2}','{3}', '{4}', '{5}', '{6}', '{7}', 0)".format(
                        iduser, data['email'], hashed, '0', 0, fecha, id_person, data['id_rol'])
                    cursor.execute(query)
                    rows_affects = cursor.rowcount
                    connection.commit()
                    if rows_affects > 0:
                        user = self.get_userbyusername(iduser)
                        return user
                    else:
                        return {'message': 'Error, Insert user failed!'}
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, data, id_user):
        try:
            us = self.get_userbyid(id_user)
            print(us)
            if us:
                connection = conn.get_connection()
                with connection.cursor() as cursor:
                    cursor.execute(
                        "update person set first_name = '{0}', card_id_person = '{1}', last_name = '{2}', phone = '{3}', address = '{4}', gender = '{5}', date_born = '{6}' where card_id_person = '{7}';".format(data['first_name'], data['card_id_person'], data['last_name'], data['phone'], data['address'], data['gender'], data['date_born'], (us.get('user')['person'])['card_id_person']))
                    username = ''
                    if int(data['id_rol']) == 1:
                        username = 'PRE-' + data['card_id_person']
                    if int(data['id_rol']) == 2:
                        username = 'EMP-' + data['card_id_person']
                    if int(data['id_rol']) == 3:
                        username = 'SEC-' + data['card_id_person']
                    if int(data['id_rol']) == 4:
                        username = 'CUS-' + data['card_id_person']
                    cursor.execute(
                        "update users set email = '{0}', rol_user = '{1}', user_name = '{2}' where id_user = '{3}';".format(data['email'], data['id_rol'], username, id_user))
                    row_affects = cursor.rowcount
                    connection.commit()
                    
                    print("Row afects: ", cursor)
                    if row_affects > 0:
                        us = self.get_userbyid(id_user)
                        return us
                    else:
                        return None
            else:
                return -1
        except Exception as ex:
            raise Exception(ex)