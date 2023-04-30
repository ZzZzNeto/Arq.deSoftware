# import filter1 from filter1.py
# import filter2 from filter2.py
# import filter3 from filter3.py
import webbrowser

data = [{
    "nome": "jose",
    "genero": "masculino",
    "idade": "19",
    "turma": "4C"
},
{
    "nome": "maria",
    "genero": "feminino",
    "idade": "12",
    "turma": "1B"
},
{
    "nome": "lucas",
    "genero": "masculino",
    "idade": "49",
    "turma": "4C"
},
{
    "nome": "ricardo",
    "genero": "masculino",
    "idade": "15",
    "turma": "4C"
},
{
    "nome": "pedro",
    "genero": "masculino",
    "idade": "99",
    "turma": "4C"
},
{
    "nome": "ana",
    "genero": "feminino",
    "idade": "19",
    "turma": "4C"
},
{
    "nome": "julia",
    "genero": "feminino",
    "idade": "13",
    "turma": "4C"
},
]

# data = filter1(data, "masculino") #apenas masculinos
# data = filter2(data, "18") #apenas acima de 18 anos
# data = filter3(data, "4C") #apenas da turma 4C

f = open('generated.html','w')

message = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel='stylesheet' type='text/css' media='screen' href='main.css'>
    <script src='main.js'></script>
</head>
<body>

    <h1>Lista de alunos </h1>
    <h3>Turma: 4C</h3>
    <h3>Ano: 2023</h3>
    <h3>Alunos: </h3>
    <ul>
"""
for x in data:
    message += f"""
        <li>{x["nome"]}</li>
    """
message += """
    </ul>
</body>
</html>
"""

f.write(message)
f.close()

webbrowser.open_new_tab('generated.html')

