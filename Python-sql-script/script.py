import pyodbc as db

#recebe as configurações para conectar ao banco.        
class Connection():
    def __init__(self):
        self.conx_string = "driver={SQL SERVER}; server=localhost; database=Movies; UID=sa; PWD=yourStrong(!)Password;"
        try:
            self.conn = db.connect(self.conx_string)
            self.cur = self.conn.cursor()
            print('Conexão aceita')
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)

#Métodos para instruções SQL:
    #Retorna o proprio objeto da classe, para conexão.
    def __enter__(self):
        return self
    
    #Para sair e fechar conexão, utilizando exc (com commit).
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()
    

    @property
    def connection(self):
        return self.conn
    
    
    @property
    def cursor(self):
        return self.cur
        
    
    def commit(self):
        self.connection.commit()
        
        
    #Para dar return em determinado registro, para as instruções SQL.
    def fetchall(self):
        return self.cursor.fetchall()
        
    
    #Para receber a instrução SQL.
    def execute(self, sql, params=None):
        #Se a instrução tiver parametros ele passa se não passa uma tupla vazia.
        self.cursor.execute(sql, params or ())
    
    
    #Para receber a query SQL.
    def query(self, sql, params=None):
        #Se a instrução tiver parametros ele passa se não passa uma tupla vazia.
        self.cursor.execute(sql, params or ())
        #Para retornar a instrução SQL.
        return self.fetchall()

#Classe para CRUDE
class MoviesSQL(Connection):
    def __init__(self):
        Connection.__init__(self)

    #Método de insert.    
    def insert(self, *args):
        try:
            #sql = "INSERT INTO Movies (DATASET_ID, TITLE) VALUES (?,?)"
            sql1 = "INSERT INTO Ratings (MOVIE_ID, RATING) VALUES (?,?)"
            #sql2 = "INSERT INTO raw_genre (NAME,NAME1,NAME2,NAME3) VALUES (?,?,?,?)"
            #self.execute(sql, args)
            self.execute(sql1, args)
            #self.execute(sql2, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir na tabela", e)
            
    
    #Insert atraves do CSV.
    def insert_movie(self, filename):
        try:
            filename = (row for row in open(filename))
            linhas_arquivo = (s.rstrip().split(',') for s in filename)
            cols = next(linhas_arquivo)
            dicionario = (dict(zip(cols, data)) for data in linhas_arquivo)
            for row in dicionario:
                self.insert(row["movieId"],row["title"])

        except Exception as e:
            print("Erro ao inserir", e)
            
     
    def insert_rating(self, filename):
        try:
            filename = (row for row in open(filename))
            linhas_arquivo = (s.rstrip().split(',') for s in filename)
            cols = next(linhas_arquivo)
            dicionario = (dict(zip(cols, data)) for data in linhas_arquivo)
            for row in dicionario:
                self.insert(row["movieId"],row["rating"])

        except Exception as e:
            print("Erro ao inserir", e)

                 
    def insert_genres(self, filename):
        try:
            filename = (row for row in open(filename))
            linhas_arquivo = (s.rstrip().split(',') for s in filename)
            cols = next(linhas_arquivo)
            dicionario = (dict(zip(cols, data)) for data in linhas_arquivo)
            for row in dicionario:
                self.insert(row["genres"],row["sep1"],row["sep2"],row["sep3"])

        except Exception as e:
            print("Erro ao inserir", e)

            
if __name__ == "__main__":
    movies = MoviesSQL()
    #print(movies.query("SELECT * FROM Movies"))
    #movies.insert_movie("PythonDOJO-SQL/clean_file.csv")
    movies.insert_rating("PythonDOJO-SQL/ratings.csv")
    #movies.insert_genres("PythonDOJO-SQL/genres.csv")
