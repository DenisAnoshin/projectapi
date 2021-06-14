
import pymysql
db = pymysql.connect(
	host='localhost', 
	port=3306, 
	user='user', 
	password='1234', 
	database='project808', 
	cursorclass=pymysql.cursors.DictCursor
)