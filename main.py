import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor() #objeto mensageiro

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancarias(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo FLOAT NOT NULL,
    cpf TEXT NOT NULL UNIQUE)""")

# cursor.execute("""INSERT INTO contas_bancarias
#                (titular, saldo, cpf) VALUES
#                ("antony", 500, '16164657514')""")

cursor.execute("""SELECT titular, saldo FROM contas_bancarias""")
conta = cursor.fetchall()
cursor.execute("""UPDATE contas_bancarias SET saldo = 13000 WHERE id = 1""")
# cursor.execute('DELETE FROM contas_bancarias WHERE id = 2')
print(conta)

for conta in conta:
    titular, saldo = conta
    print(f"""
titular{titular}
saldo{saldo}
""")


conexao.commit()