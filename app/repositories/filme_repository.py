import csv
import sqlite3

db_file = 'dados.db'
csv_file = 'data/movielist.csv'

def criar_tabela():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filmes (
            year INTEGER,
            title TEXT,
            studios TEXT,
            producers TEXT,
            winner TEXT
        )
    ''')

    conn.commit()
    conn.close()

def importar_dados():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(csv_file, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')

        for linha in leitor_csv:
            year = int(linha['year'])
            title = linha['title']
            studios = linha['studios']
            producers = linha['producers']
            winner = linha['winner']

            cursor.execute("INSERT INTO filmes (year, title, studios, producers, winner) VALUES (?, ?, ?, ?, ?)",
                           (year, title, studios, producers, winner))

        conn.commit()
        conn.close()

def mostrar_dados():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM filmes")
    registros = cursor.fetchall()
    
    result = []
    for registro in registros:
        year, title, studios, producers, winner = registro
        result.append({
            "Year": year,
            "Title": title,
            "Studios": studios,
            "Producers": producers,
            "Winner": winner
        })
    
    conn.close()
    return result

def obter_maior_intervalo_e_premio_mais_rapido():
    # Conecte-se ao banco de dados SQLite
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()

    # Execute uma consulta SQL para selecionar todos os registros da tabela "filmes"
    cursor.execute("SELECT * FROM filmes ORDER BY year")
    registros = cursor.fetchall()

    # Crie um dicionário para rastrear os prêmios por produtor
    premios_por_produtores = {}

    # Dicionários para rastrear o maior e o menor intervalo
    maior_intervalo = {"producer": None, "interval": -1, "previousWin": None, "followingWin": None}
    menor_intervalo = {"producer": None, "interval": float('inf'), "previousWin": None, "followingWin": None}

    for registro in registros:
        year, producers = registro[0], registro[3]

        if producers:
            produtores = producers.split(', ')
            for produtor in produtores:
                if produtor not in premios_por_produtores:
                    premios_por_produtores[produtor] = []

                premios_por_produtores[produtor].append(year)

                # Verifique o intervalo entre os prêmios consecutivos para este produtor
                premios = premios_por_produtores[produtor]
                if len(premios) > 1:
                    intervalo = premios[-1] - premios[-2]

                    if intervalo > maior_intervalo["interval"]:
                        maior_intervalo["producer"] = produtor
                        maior_intervalo["interval"] = intervalo
                        maior_intervalo["previousWin"] = premios[-2]
                        maior_intervalo["followingWin"] = premios[-1]

                    if intervalo < menor_intervalo["interval"]:
                        menor_intervalo["producer"] = produtor
                        menor_intervalo["interval"] = intervalo
                        menor_intervalo["previousWin"] = premios[-2]
                        menor_intervalo["followingWin"] = premios[-1]

    conn.close()

    return {"min": [menor_intervalo], "max": [maior_intervalo]}