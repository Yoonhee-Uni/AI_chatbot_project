import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

# MYSQL configuration
db_config = {
    'user': 'user',
    'password': 'password',
    'host': '127.0.0.1',
    'raise_on_warnings': True}
connection = mysql.connector.connect(**db_config)

# Connect to MySQL
mycursor = connection.cursor()

# Create database and tables
script = """ DROP DATABASE IF EXISTS question_bank_chatbot;
CREATE DATABASE question_bank_chatbot;

USE question_bank_chatbot;

DROP TABLE IF EXISTS conversation_history;
DROP TABLE IF EXISTS conversation_ids;
DROP TABLE IF EXISTS junction_keywords_faqs;
DROP TABLE IF EXISTS keywords;
DROP TABLE IF EXISTS junction_faqs_sources;
DROP TABLE IF EXISTS faqs;
DROP TABLE IF EXISTS sources;
DROP TABLE IF EXISTS conversation_history;

CREATE TABLE conversation_ids (
    conversation_id INT, 
    PRIMARY KEY (conversation_id) 
);

CREATE TABLE conversation_history (
conversation_id INT,
input VARCHAR(255),
response LONGTEXT,
created_at DATETIME,
PRIMARY KEY (conversation_id, created_at),
FOREIGN KEY (conversation_id) REFERENCES CONVERSATION_IDS(conversation_id)
);

CREATE TABLE faqs (
	question_id INT NOT NULL primary key,
	question VARCHAR(255) NOT NULL,
	answer LONGTEXT NOT NULL
);

CREATE TABLE sources (
	source_id INT NOT NULL primary key,
	source_title VARCHAR(255) NOT NULL,
	source_link VARCHAR(2048) NOT NULL
);

CREATE TABLE keywords (
	keyword_id INT NOT NULL primary key,
    keyword VARCHAR(150) NOT NULL
    );
    
CREATE TABLE junction_keywords_faqs (
	keyword_id INT NOT NULL,
    question_id INT NOT NULL,
    FOREIGN KEY (keyword_id) REFERENCES KEYWORDS(keyword_id),
    FOREIGN KEY (question_id) REFERENCES FAQS(question_id)
    );

CREATE TABLE junction_faqs_sources;(
	question_id INT NOT NULL,
	source_id INT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES FAQS(question_id),
    FOREIGN KEY (source_id) REFERENCES SOURCES(source_id)
);
""" 
# connect sql
mycursor = connection.cursor()
# execute sql query
mycursor.execute(script)

# put csv file data to sql
engine = create_engine("mysql+mysqlconnector://user:user_password@localhost/question_bank_chatbot")

