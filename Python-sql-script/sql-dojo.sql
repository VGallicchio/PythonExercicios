CREATE DATABASE Movies;
USE Movies;
--Criando Tabelas:
CREATE TABLE Movies
(	
	--ID INT IDENTITY(1,1) PRIMARY KEY,
	DATASET_ID INT NOT NULL PRIMARY KEY,
	TITLE VARCHAR(255) NOT NULL
);

CREATE TABLE Genres
(	
	ID INT IDENTITY(1,1) PRIMARY KEY,
	NAME VARCHAR(255) NOT NULL
);

CREATE TABLE Users
(	
	ID INT IDENTITY(1,1) PRIMARY KEY,
	NAME VARCHAR(255) NOT NULL,
);

CREATE TABLE Copy
(	
	ID INT IDENTITY(1,1) PRIMARY KEY,
	MOVIE_ID INT FOREIGN KEY REFERENCES Movies(DATASET_ID)
);
--Criando banco:
CREATE DATABASE Movies;
USE Movies;

CREATE TABLE Rent
(	
	ID INT IDENTITY(1,1) PRIMARY KEY,
	COPY_ID INT FOREIGN KEY REFERENCES Copy(ID),
	USER_ID INT FOREIGN KEY REFERENCES Users(ID),
	RENT_DATE DATE NOT NULL,
	RETURN_DATE DATE NOT NULL,
	ACTUAL_RETURN_DATE DATE

);

CREATE TABLE Genres_Link
(	
	MOVIE_ID INT FOREIGN KEY REFERENCES Movies(DATASET_ID),
	GENRE_ID INT FOREIGN KEY REFERENCES Genres(ID)
);

CREATE TABLE Ratings
(	
	ID INT IDENTITY(1,1) PRIMARY KEY,
	MOVIE_ID INT FOREIGN KEY REFERENCES Movies(DATASET_ID),
	RATING FLOAT NOT NULL
);

CREATE TABLE raw_genre
(
	NAME VARCHAR(255),
	NAME1 VARCHAR(255),
	NAME2 VARCHAR(255),
	NAME3 VARCHAR(255),
	NAME4 VARCHAR(255),
	NAME5 VARCHAR(255),
	NAME6 VARCHAR(255)
);

--- Inserindo na tabela Copy:
INSERT INTO Copy(MOVIE_ID)
	SELECT MOVIE_ID
    FROM Ratings 
    ORDER BY MOVIE_ID;

-- Inserindo generos distintos na tabela generos:
INSERT INTO raw_genre (NAME5)
	SELECT DISTINCT NAME
	FROM raw_genre;

INSERT INTO raw_genre (NAME5)
	SELECT DISTINCT NAME1
	FROM raw_genre;

INSERT INTO raw_genre (NAME5)
	SELECT DISTINCT NAME2
	FROM raw_genre;

INSERT INTO raw_genre (NAME5)
	SELECT DISTINCT NAME3
	FROM raw_genre;

INSERT INTO raw_genre (NAME5)
	SELECT DISTINCT NAME4
	FROM raw_genre;

INSERT INTO Genres(NAME)
	SELECT DISTINCT NAME5
	FROM raw_genre
	where NAME5 IS NOT null AND NAME5 NOT LIKE '';
	
---Inserts manuais:	
INSERT INTO Users VALUES
('Ricardo'),
('José'),
('Marcos'),
('Guilherme'),
('Ana'),
('Patricia'),
('Roseli'),
('Vitor'),
('Alexandre'),
('Juliano'),
('Amanda');

INSERT INTO Rent VALUES
(5,6,'2021-01-20','2021-01-23','2021-01-26'),
(25,5,'2021-01-21','2021-01-24','2021-01-27');




-- Criando procedure para alugar uma cópia:

CREATE PROCEDURE RENT_COPY @copyid INT, @userid INT, @days INT
AS
BEGIN
	DECLARE @Rented int
	SELECT @Rented = COUNT(1) FROM Rent WHERE COPY_ID = @copyid AND ACTUAL_RETURN_DATE IS NULL
	IF (@Rented = 1)
	BEGIN
		RAISERROR ('Copy is already rented', 16,1)
		RETURN
	END
	INSERT INTO Rent(COPY_ID, USER_ID, RENT_DATE, RETURN_DATE) VALUES(
		@copyid,
		@userid,
		GETDATE(),
		DATEADD(DAY, @days, GETDATE())
		)
END

EXECUTE RENT_COPY 1, 2, 3;

SELECT * 
FROM Rent R
JOIN Users U 
ON U.ID = R.ID

--- Criando procedure para retornar uma cópia:
CREATE PROCEDURE RETURN_COPY @copyid INT
AS
	UPDATE Rent SET ACTUAL_RETURN_DATE = GETDATE() WHERE COPY_ID = @copyid AND ACTUAL_RETURN_DATE IS NULL;

EXECUTE RETURN_COPY 2;

--- Criando procedure para ver as copias que estão disponíveis:
CREATE FUNCTION AVAL_COPY(@movieid INT)
RETURNS TABLE
AS
RETURN(
	SELECT * FROM Copy COPY WHERE COPY.MOVIE_ID = @movieid AND COPY.ID NOT IN(
		SELECT C.ID
		FROM Copy C
		JOIN Rent R
			ON R.COPY_ID = C.ID
			AND C.MOVIE_ID = @movieid
			AND R.ACTUAL_RETURN_DATE IS NULL
		)
)

SELECT * FROM AVAL_COPY(10)

--- Criando view para visualizar as cópias com entrega atrasada:
DROP VIEW RENT_DELAY;
CREATE OR ALTER VIEW RENT_DELAY
AS
	SELECT U.NAME, M.TITLE, R.RETURN_DATE 
		FROM Rent R
		JOIN Copy C
		ON C.ID = R.COPY_ID
		JOIN Movies M
		ON M.DATASET_ID = C.MOVIE_ID 	
		JOIN Users U
		ON U.ID = R.USER_ID
		WHERE R.ACTUAL_RETURN_DATE IS NULL
		AND R.RETURN_DATE < GETDATE()
		
SELECT * FROM RENT_DELAY;

--- Criando view para visualizar usuários que entregaram atrasado:
DROP VIEW RENT_DELAY;
CREATE OR ALTER VIEW USERS_DELAYED_RENTS
AS
	SELECT U.NAME, M.TITLE, R.RETURN_DATE, R.ACTUAL_RETURN_DATE 
		FROM Rent R
		JOIN Copy C
		ON C.ID = R.COPY_ID
		JOIN Movies M
		ON M.DATASET_ID = C.MOVIE_ID 	
		JOIN Users U
		ON U.ID = R.USER_ID
		WHERE R.ACTUAL_RETURN_DATE > R.RETURN_DATE 
		
SELECT * FROM USERS_DELAYED_RENTS;