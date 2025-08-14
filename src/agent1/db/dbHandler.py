import sqlite3
import sqlite_vec
import os
from agent1.tools.embed import embed
class DBHandler:
    def __init__(self, db_path = './src/agent1/db/semantic_index.db', table_name= "embeddings_vec", embedding_dim=1536):
        self.db_path = db_path
        self.table_name = table_name
        self.embedding_dim = embedding_dim
        self.conn = sqlite3.connect(db_path)
        self.conn.enable_load_extension(True)
        sqlite_vec.init(self.conn)
        self.cursor = self.conn.cursor()
        self.conn.execute(f"""
        CREATE VIRTUAL TABLE IF NOT EXISTS {self.table_name} USING vec0(
            embedding FLOAT[{self.embedding_dim}],  -- Define the vector column with its dimensions
            url TEXT,
            verse TEXT,
        );
        """)


    def _execute_query(self, query, params=()):
        try:
            cursur = self.conn.cursor()
            cursur.execute(query, params)
            self.conn.commit()
            return cursur
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            self.conn.close()

    def insert(self, title, embedding):
        '''
        Insert a new document into the database.
        DB is ready. If you want to add more, you can complete this function
        '''
        pass


    def similarity_search(self, text, k=3):
        embedding = embed(text)
        query = f"""
        SELECT 
            id, 
            file_path, 
            embedding, 
            vec_cosine_distance(embedding, vec{self.embedding_dim}(?)) AS similarity
        FROM {self.table_name} 
        ORDER BY similarity ASC
        LIMIT ?;"""

        params = (embedding, k)
        return self._execute_query(query, params)
    
    