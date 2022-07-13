Faça o download do arquivo. Ele também está disponível em Recorded Crime Data at the Police Force Area Level | Kaggle onde você pode ver um pouco mais sobre os dados.

Crie um programa que faça a leitura desse arquivo. 

 Você deverá agrupar os crimes por região, porém só deverá manter as regiões com mais de 2 tipos de infração. Você tambem deverá manter o número de cada crime. Apenas contabilizar crimes com mais de 10 ocorrências na região.

Em cada região, colocar o horário em que você fez o processamento. O horário deverá estar no formato dd/MM/yyyy HH:mm

Como saída você deverá gravar cada regiao ( e seus respectivos dados ) em uma linha em formato JSON.

Ex:

Imagine que o arquivo contenha apenas as seguintes linhas
![image](https://user-images.githubusercontent.com/81394440/178748775-83a67cd5-8574-4ab2-8782-ed965febfaf5.png)

Seu arquivo de saída deverá ser:

{"process_time": "01/09/2021 16:01", "region": "South West", "crimes": [{"crime": "All other theft offences", "count": 25959}, {"crime": "Bicycle theft", "count": 3090}]}

{"process_time": "01/09/2021 16:02", "region": "East", "crimes": [{"crime": "All other theft offences", "count": 8797}, {"crime": "Bicycle theft", "count": 719}]}


Note que a região "British Transport Police" não aparece, pois após o agrupamento teria apenas 1 tipo de crime.
