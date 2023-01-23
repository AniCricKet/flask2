import sqlite3
class FastFoodRankingSystem:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    def init_fast_food_ranking_system_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS FastFoodRankingSystem (
            UserID INTEGER PRIMARY KEY,
            RestaurantName TEXT,
            Ranking INTEGER,
            AverageRanking INTEGER
        )""")
        self.conn.commit()
    def insert_ranking(self, user_id, restaurant_name, ranking):
        self.cursor.execute("""INSERT INTO FastFoodRankingSystem (UserID, RestaurantName, Ranking)
            VALUES (?,?,?)""", (user_id, restaurant_name, ranking))
        self.conn.commit()
    def update_ranking(self, user_id, restaurant_name, ranking):
        self.cursor.execute("""UPDATE FastFoodRankingSystem
            SET Ranking = ?
            WHERE UserID = ? AND RestaurantName = ?""", (ranking, user_id, restaurant_name))
        self.conn.commit()
    def delete_ranking(self, user_id, restaurant_name):
        self.cursor.execute("""DELETE FROM FastFoodRankingSystem
            WHERE UserID = ? AND RestaurantName = ?""", (user_id, restaurant_name))
        self.conn.commit()
    def get_average_ranking(self, restaurant_name):
        self.cursor.execute("""SELECT AVG(Ranking) FROM FastFoodRankingSystem
            WHERE RestaurantName = ?""", (restaurant_name,))
        rows = self.cursor.fetchall()
        return rows[0][0]
    def get_user_ranking(self, user_id):
        self.cursor.execute("""SELECT RestaurantName, Ranking FROM FastFoodRankingSystem
            WHERE UserID = ?""", (user_id,))
        rows = self.cursor.fetchall()
        return rows
    def get_all_rankings(self):
        self.cursor.execute("""SELECT * FROM FastFoodRankingSystem""")
        rows = self.cursor.fetchall()
        return rows
    def close(self):
        self.conn.close()
#Init Method:
def init_fast_food_ranking_system():
    db_name = 'fast_food_ranking_system.db'
    db = FastFoodRankingSystem(db_name)
    db.init_fast_food_ranking_system_table()
    # Add preliminary/test data
    db.insert_ranking(1, 'Restaurant 1', 9)
    db.insert_ranking(2, 'Restaurant 2', 8)
    db.insert_ranking(3, 'Restaurant 3', 7)
    db.insert_ranking(4, 'Restaurant 4', 6)
    db.close()
init_fast_food_ranking_system()