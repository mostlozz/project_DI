import sqlite3
from datetime import datetime
import pandas as pd

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Закрузка из файла скл (создание базы данных)
def load_sql ():
	with open ('ddl_dml.sql', 'r', encoding='utf-8') as f:
		sql_script = f.read()
	# Разделение скрипта на отдельные запросы по точке с запятой
	sql_commands = sql_script.split(';')

	# Выполнение каждого запроса по очереди
	for command in sql_commands:
	    try:
	        if command.strip():  # Пропуск пустых строк
	            cursor.execute(command)
	            conn.commit()
	    except sqlite3.OperationalError as e:
	        print(f"Ошибка при выполнении запроса: {command}")
	        print(f"Сообщение об ошибке: {e}")


# принт таблицы из БД скл
def showTable (name):
	cursor.execute(f'''
		SELECT * from {name} limit 10
		''')
	print('-_'*50)
	print(f'{name}')
	print('-_'*50)
	for i in cursor.fetchall():
		print(i)

load_sql ()
showTable('cards')
showTable('accounts')
showTable('clients')

