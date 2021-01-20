from core.database.db_connect import Connection
from pypika import Query, Table

users = Table("users")

class UserRepository(Connection):
    def getById(self, args=None):
        query = Query.from_(users).select("*").where(users.tg_id == "%s")
        q = query.get_sql(quote_char=None)

        return self._select(q, args)

    def getByUsername(self, args=None):
        q = "SELECT * FROM users WHERE tg_username = %s"

        return self._select(q, args)

    def getUserByGroup(self, args=None):
        q = "SELECT u.tg_id,u.tg_username,gr.id_group,gu.warn_count, gr.max_warn FROM users u INNER JOIN group_users gu ON gu.tg_id = u.tg_id INNER JOIN groups gr ON gu.tg_group_id = gr.id_group WHERE u.tg_id = %s AND gr.id_group = %s"
        return self._select(q, args)

    def getAll(self, args=None):
        query = Query.from_(users).select("*").where(users.tg_id == "%s")
        q = query.get_sql(quote_char=None)

        return self._selectAll(q, args)

    def add(self, args=None):
        q = "INSERT INTO users (tg_id, tg_username, warn_count) VALUES (%s,%s,%s)"
        return self._insert(q, args)

    def add_into_mtm(self, args=None):
        q = "INSERT IGNORE INTO group_users (tg_id, tg_group_id, warn_count) VALUES (%s,%s,%s)"
        return self._insert(q, args)

    def update(self, args=None):
        q = "UPDATE users SET tg_username = %s WHERE tg_id = %s"
        return self._update(q, args)

    def updateWarn(self, args=None):
        q = "UPDATE group_users SET warn_count = warn_count + 1 WHERE tg_id = %s AND tg_group_id = %s"
        return self._update(q, args)