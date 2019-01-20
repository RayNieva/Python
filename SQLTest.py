# Also Pyodbc
import pyodbc
cnxn = pyodbc.connect(r'Driver={SQL Server};Server=RAYNIEVA2;Database=BudgetBillsBanking;Trusted_Connection=yes;')
cursor = cnxn.cursor()
# cursor.execute("SELECT  * FROM Table_Bofa_Credit")
cursor.execute("SELECT payee, Amount  FROM Table_Bofa_Credit")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row)
# cnxn.close()

# About Pandas
# import pandas
import pandas as pd
# stmt = "SELECT payee, Amount  FROM Table_Bofa_Credit"
stmt = "SELECT *  FROM Table_Bofa_Credit"
df = pd.read_sql(stmt,cnxn)
df.head(5)


