# análise do Dataset Class em Python

## 1-) uma amostra correspondente a 30% da base de dados original.

```python 
    amostra=data_df.sample(np.floor(0.3*data_df.shape[0]))
    print(amostra)
```

### Amostra correspondente a 30% da base de dados original
|     |  ID |      RI |    Na |   Mg |   Ai |    Si |    K |    Ca |   Ba |   Fe | Type|
|-----|-----|---------|-------|------|------|-------|------|-------|------|------|-----|
| 80  |  81 | 1.51592 | 12.86 | 3.52 | 2.12 | 72.66 | 0.69 |  7.97 | 0.00 | 0.00 |    2|
| 15  |  16 | 1.51761 | 12.81 | 3.54 | 1.23 | 73.24 | 0.58 |  8.39 | 0.00 | 0.00 |    1|
| 197 | 198 | 1.51727 | 14.70 | 0.00 | 2.34 | 73.28 | 0.00 |  8.95 | 0.66 | 0.00 |    7|
| 152 | 153 | 1.51779 | 13.64 | 3.65 | 0.65 | 73.00 | 0.06 |  8.93 | 0.00 | 0.00 |    3|
| 22  |  23 | 1.51736 | 12.78 | 3.62 | 1.29 | 72.79 | 0.59 |  8.70 | 0.00 | 0.00 |    1|
| 106 | 107 | 1.53125 | 10.73 | 0.00 | 2.10 | 69.81 | 0.58 | 13.30 | 3.15 | 0.28 |    2|
| 34  |  35 | 1.51783 | 12.69 | 3.54 | 1.34 | 72.95 | 0.57 |  8.75 | 0.00 | 0.00 |    1|
| 101 | 102 | 1.51730 | 12.35 | 2.72 | 1.63 | 72.87 | 0.70 |  9.23 | 0.00 | 0.00 |    2|
| 147 | 148 | 1.51610 | 13.33 | 3.53 | 1.34 | 72.67 | 0.56 |  8.33 | 0.00 | 0.00 |    3|
| 134 | 135 | 1.51811 | 13.33 | 3.85 | 1.25 | 72.78 | 0.52 |  8.12 | 0.00 | 0.00 |    2|
| 203 | 204 | 1.51658 | 14.80 | 0.00 | 1.99 | 73.11 | 0.00 |  8.28 | 1.71 | 0.00 |    7|
| 75  |  76 | 1.51590 | 13.02 | 3.58 | 1.51 | 73.12 | 0.69 |  7.96 | 0.00 | 0.00 |    2|
| 23  |  24 | 1.51751 | 12.81 | 3.57 | 1.35 | 73.02 | 0.62 |  8.59 | 0.00 | 0.00 |    1|
| 108 | 109 | 1.52222 | 14.43 | 0.00 | 1.00 | 72.67 | 0.10 | 11.52 | 0.00 | 0.08 |    2|
| 60  |  61 | 1.51905 | 13.60 | 3.62 | 1.11 | 72.64 | 0.14 |  8.76 | 0.00 | 0.00 |    1|
| 16  |  17 | 1.51784 | 12.68 | 3.67 | 1.16 | 73.11 | 0.61 |  8.70 | 0.00 | 0.00 |    1|
| 46  |  47 | 1.51869 | 13.19 | 3.37 | 1.18 | 72.72 | 0.57 |  8.83 | 0.00 | 0.16 |    1|
| 170 | 171 | 1.52369 | 13.44 | 0.00 | 1.58 | 72.22 | 0.32 | 12.24 | 0.00 | 0.00 |    5|
| 109 | 110 | 1.51818 | 13.72 | 0.00 | 0.56 | 74.45 | 0.00 | 10.99 | 0.00 | 0.00 |    2|
| 21  |  22 | 1.51966 | 14.77 | 3.75 | 0.29 | 72.02 | 0.03 |  9.00 | 0.00 | 0.00 |    1|
| 84  |  85 | 1.51409 | 14.25 | 3.09 | 2.08 | 72.28 | 1.10 |  7.08 | 0.00 | 0.00 |    2|
| 126 | 127 | 1.51667 | 12.94 | 3.61 | 1.26 | 72.75 | 0.56 |  8.60 | 0.00 | 0.00 |    2|
| 6   |   7 | 1.51743 | 13.30 | 3.60 | 1.14 | 73.09 | 0.58 |  8.17 | 0.00 | 0.00 |    1|
| 161 | 162 | 1.51934 | 13.64 | 3.54 | 0.75 | 72.65 | 0.16 |  8.89 | 0.15 | 0.24 |    3|
| 192 | 193 | 1.51623 | 14.20 | 0.00 | 2.79 | 73.46 | 0.04 |  9.04 | 0.40 | 0.09 |    7|
| 94  |  95 | 1.51629 | 12.71 | 3.33 | 1.49 | 73.28 | 0.67 |  8.24 | 0.00 | 0.00 |    2|
| 169 | 170 | 1.51994 | 13.27 | 0.00 | 1.76 | 73.03 | 0.47 | 11.32 | 0.00 | 0.00 |    5|
| 33  |  34 | 1.51753 | 12.57 | 3.47 | 1.38 | 73.39 | 0.60 |  8.55 | 0.00 | 0.06 |    1|
| 137 | 138 | 1.51711 | 12.89 | 3.62 | 1.57 | 72.96 | 0.61 |  8.11 | 0.00 | 0.00 |    2|
| 19  |  20 | 1.51735 | 13.02 | 3.54 | 1.69 | 72.73 | 0.54 |  8.44 | 0.00 | 0.07 |    1|
| ..  | ... |    ...  |  ...  | ...  | ...  |  ...  | ...  |  ...  | ...  | ...  | ... |
| 144 | 145 | 1.51660 | 12.99 | 3.18 | 1.23 | 72.97 | 0.58 |  8.81 | 0.00 | 0.24 |    2|
| 102 | 103 | 1.51820 | 12.62 | 2.76 | 0.83 | 73.81 | 0.35 |  9.42 | 0.00 | 0.20 |    2|
| 69  |  70 | 1.52300 | 13.31 | 3.58 | 0.82 | 71.99 | 0.12 | 10.17 | 0.00 | 0.03 |    1|
| 178 | 179 | 1.51829 | 14.46 | 2.24 | 1.62 | 72.38 | 0.00 |  9.26 | 0.00 | 0.00 |    6|
| 1   |   2 | 1.51761 | 13.89 | 3.60 | 1.36 | 72.73 | 0.48 |  7.83 | 0.00 | 0.00 |    1|
| 164 | 165 | 1.51915 | 12.73 | 1.85 | 1.86 | 72.69 | 0.60 | 10.09 | 0.00 | 0.00 |    5|
| 205 | 206 | 1.51732 | 14.95 | 0.00 | 1.80 | 72.99 | 0.00 |  8.61 | 1.55 | 0.00 |    7|
| 95  |  96 | 1.51860 | 13.36 | 3.43 | 1.43 | 72.26 | 0.51 |  8.60 | 0.00 | 0.00 |    2|
| 111 | 112 | 1.52739 | 11.02 | 0.00 | 0.75 | 73.08 | 0.00 | 14.96 | 0.00 | 0.00 |    2|
| 189 | 190 | 1.52365 | 15.79 | 1.83 | 1.31 | 70.43 | 0.31 |  8.61 | 1.68 | 0.00 |    7|
| 212 | 213 | 1.51651 | 14.38 | 0.00 | 1.94 | 73.61 | 0.00 |  8.48 | 1.57 | 0.00 |    7|
| 14  |  15 | 1.51763 | 12.61 | 3.59 | 1.31 | 73.29 | 0.58 |  8.50 | 0.00 | 0.00 |    1|
| 35  |  36 | 1.51567 | 13.29 | 3.45 | 1.21 | 72.74 | 0.56 |  8.57 | 0.00 | 0.00 |    1|
| 194 | 195 | 1.51683 | 14.56 | 0.00 | 1.98 | 73.29 | 0.00 |  8.52 | 1.57 | 0.07 |    7|
| 110 | 111 | 1.52664 | 11.23 | 0.00 | 0.77 | 73.21 | 0.00 | 14.68 | 0.00 | 0.00 |    2|
| 66  |  67 | 1.52152 | 13.05 | 3.65 | 0.87 | 72.22 | 0.19 |  9.85 | 0.00 | 0.17 |    1|
| 181 | 182 | 1.51888 | 14.99 | 0.78 | 1.74 | 72.50 | 0.00 |  9.95 | 0.00 | 0.00 |    6|
| 199 | 200 | 1.51609 | 15.01 | 0.00 | 2.51 | 73.05 | 0.05 |  8.83 | 0.53 | 0.00 |    7|
| 160 | 161 | 1.51832 | 13.33 | 3.34 | 1.54 | 72.14 | 0.56 |  8.99 | 0.00 | 0.00 |    3|
| 113 | 114 | 1.51892 | 13.46 | 3.83 | 1.26 | 72.55 | 0.57 |  8.21 | 0.00 | 0.14 |    2|
| 204 | 205 | 1.51617 | 14.95 | 0.00 | 2.27 | 73.30 | 0.00 |  8.71 | 0.67 | 0.00 |    7|
| 162 | 163 | 1.52211 | 14.19 | 3.78 | 0.91 | 71.36 | 0.23 |  9.14 | 0.00 | 0.37 |    3|
| 27  |  28 | 1.51721 | 12.87 | 3.48 | 1.33 | 73.04 | 0.56 |  8.43 | 0.00 | 0.00 |    1|
| 136 | 137 | 1.51806 | 13.00 | 3.80 | 1.08 | 73.07 | 0.56 |  8.38 | 0.00 | 0.12 |    2|
| 141 | 142 | 1.51851 | 13.20 | 3.63 | 1.07 | 72.83 | 0.57 |  8.41 | 0.09 | 0.17 |    2|
| 142 | 143 | 1.51662 | 12.85 | 3.51 | 1.44 | 73.01 | 0.68 |  8.23 | 0.06 | 0.25 |    2|
| 65  |  66 | 1.52099 | 13.69 | 3.59 | 1.12 | 71.96 | 0.09 |  9.40 | 0.00 | 0.00 |    1|
| 77  |  78 | 1.51627 | 13.00 | 3.58 | 1.54 | 72.83 | 0.61 |  8.04 | 0.00 | 0.00 |    2|
| 127 | 128 | 1.52081 | 13.78 | 2.28 | 1.43 | 71.99 | 0.49 |  9.85 | 0.00 | 0.17 |    2|
| 156 | 157 | 1.51655 | 13.41 | 3.39 | 1.28 | 72.64 | 0.52 |  8.65 | 0.00 | 0.00 |    3|
[64 rows x 11 columns]

## 2-) faça um comparativo entre a mostra gerada e a base de dados original (em relação a valores médios de seus atributos.

```python
    print('media da base')
    print(data_df.mean())
    print('media da amostra')
    print(amostra.mean())
```

|media da base     |media da amostra  |
|------------------|------------------|
|ID      107.500000|ID      112.625000|
|RI        1.518365|RI        1.518588|
|Na       13.407850|Na       13.413281|
|Mg        2.684533|Mg        2.447500|
|Ai        1.444907|Ai        1.406719|
|Si       72.650935|Si       72.766875|
|K         0.497056|K         0.394375|
|Ca        8.956963|Ca        9.185312|
|Ba        0.175047|Ba        0.215469|
|Fe        0.057009|Fe        0.045469|
|Type      2.780374|Type      2.875000|

## 3-) imprima a média, o desvio padrão, o menor e maior valor encontrado no atributo Potassium

> media da base para o atributo potassium = 0.49705607476635494

```python
    print(data_df['K'].mean())
```
> desvio padrão da base para o atributo potassium = 0.6521918455589802

```python
    print(data_df['K'].std())
```
> maior da base para o atributo potassium = 6.21

```python
    print(data_df['K'].max())
```
> menor da base para o atributo potassium = 0.0

```python
    print(data_df['K'].min())
```
## 4-) a quantidade de instâncias por tipo diferente de vidro (atributo Type of glass) quantidade de instâncias por tipo diferente de vidro

```python
    print(data_df['Type'].value_counts())
```

| I | QT |
|---|----|
| 2 | 76 |
| 1 | 70 |
| 7 | 29 |
| 3 | 17 |
| 5 | 13 |
| 6 |  9 |

## 5-) procure identificar correlações positivas, negativas e neutras entre alguns atributos que constituem a base de dados.

```python
    plt.matshow(data_df.corr())
```

### Matriz de correlação
![alt text](https://github.com/mateusvilione/Analise-do-Dataset-Class/blob/master/img/1.png "Matriz de correlação")

|     correlações     |                                                       atributos                                                                |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|
|correlações positivas|![alt text][cel1] Os atributos com essa tonalidade tendem a ser fortemente positivos Exs: ele com ele mesmo ou (0,10 - 1,7 ...) |
|correlações negativas|![alt text][cel2] Os atributos com essa tonalidade tendem a ser fortemente negativos Exs: (0,3 - 2,5 - 3,8 - 3,10 ...)          |
|correlações neutras  |![alt text][cel3] Os atributos com essa tonalidade tendem a ser fortemente neutra Exs: (1,3 - 1,8 - 4,9 ...)                    |

[cel1]: https://github.com/mateusvilione/Analise-do-Dataset-Class/blob/master/img/celula%201.png "correlação positivas"
[cel2]: https://github.com/mateusvilione/Analise-do-Dataset-Class/blob/master/img/celula%202.png "correlação negativas"
[cel3]: https://github.com/mateusvilione/Analise-do-Dataset-Class/blob/master/img/celula%203.png "correlação neutras"



---

### Converta o arquivo original disponibilizado no formato glass.data para o formato glass.arff (formato utilizado pelo software WEKA).

## 1-) Com base neste arquivo execute o programa WEKA e utilize a técnica classificação com o programa MultiplayerPerceptron, calcule e imprima os percentuais de classificação (correta e incorreta) para as seguintes configurações:
 
## 1.1) utilizando TODO o conjunto de dados (Test options -> Using training set)

### Todo o Conjunto
|              Summary             |          |     |   |
|----------------------------------|----------|-----|---|
| Correctly Classified Instances   |    214   | 100 | % |
| Incorrectly Classified Instances |     0    |  0  | % |
| Kappa statistic                  |     1    |     |   |
| Mean absolute error              | 0.0076   |     |   |
| Root mean squared error          | 0.0191   |     |   |
| Relative absolute error          | 3.0968 % |     |   |
| Root relative squared error      | 5.4519 % |     |   |
| Total Number of Instances        | 214      |     |   |


#### Detailed Accuracy By Class
|                 | TP Rate | FP Rate | Precision | Recall | F-Measure | MCC   | ROC Area | PRC Area | Class |
|-----------------|---------|---------|-----------|--------|-----------|-------|----------|----------|-------|
|                 | 1,000   | 0,000   | 1,000     | 1,000  | 1,000     | 1,000 | 1,000    | 1,000    | 1     |
|                 | 1,000   | 0,000   | 1,000     | 1,000  | 1,000     | 1,000 | 1,000    | 1,000    | 2     |
|                 | 1,000   | 0,000   | 1,000     | 1,000  | 1,000     | 1,000 | 1,000    | 1,000    | 3     |
|                 | 1,000   | 0,000   | 1,000     | 1,000  | 1,000     | 1,000 | 1,000    | 1,000    | 5     |
|                 | 1,000   | 0,000   | 1,000     | 1,000  | 1,000     | 1,000 | 1,000    | 1,000    | 6     |
|                 | 1,000   | 0,000   | 1,000     | 1,000  | 1,000     | 1,000 | 1,000    | 1,000    | 7     |
| Weighted Avg.   | 1,000   | 0,000   | 1,000     | 1,000  | 1,000     | 1,000 | 1,000    | 1,000    |       |


#### Confusion Matrix
|  a |  b |  c |  d | e |  f | <-- classified as|
|----|----|----|----|---|----|--------|
| 70 |  0 |  0 |  0 | 0 |  0 |  a = 1 |
|  0 | 76 |  0 |  0 | 0 |  0 |  b = 2 |
|  0 |  0 | 17 |  0 | 0 |  0 |  c = 3 |
|  0 |  0 |  0 | 13 | 0 |  0 |  d = 5 |
|  0 |  0 |  0 |  0 | 9 |  0 |  e = 6 |
|  0 |  0 |  0 |  0 | 0 | 29 |  f = 7 |


## 1.2) utilizando validação cruzada com 10 pastas (Test options -> Cross-validation)

### Validação cruzada com 10 pastas

#### Stratified cross-validation

|              Summary             |           |         |   |
|----------------------------------|-----------|---------|---|
| Correctly Classified Instances   |    206    | 96.2617 | % |
| Incorrectly Classified Instances |     8     |  3.7383 | % |
| Kappa statistic                  | 0.9492    |         |   |
| Mean absolute error              | 0.0213    |         |   |
| Root mean squared error          | 0.0997    |         |   |
| Relative absolute error          | 8.6435 %  |         |   |
| Root relative squared error      | 28.429  % |         |   |
| Total Number of Instances        | 214       |         |   |
  
  
#### Detailed Accuracy By Class
|                 | TP Rate | FP Rate | Precision | Recall | F-Measure | MCC   | ROC Area | PRC Area | Class |
|-----------------|---------|---------|-----------|--------|-----------|-------|----------|----------|-------|
|                 | 1,000   | 0,007   | 0,986     | 1,000  | 0,993     | 0,989 | 1,000    | 1,000    | 1     |
|                 | 0,974   | 0,014   | 0,974     | 0,974  | 0,974     | 0,959 | 0,989    | 0,991    | 2     |
|                 | 0,882   | 0,000   | 1,000     | 0,882  | 0,938     | 0,935 | 0,999    | 0,988    | 3     |
|                 | 0,923   | 0,015   | 0,800     | 0,923  | 0,857     | 0,850 | 0,970    | 0,923    | 5     |
|                 | 0,889   | 0,005   | 0,889     | 0,889  | 0,889     | 0,884 | 0,995    | 0,942    | 6     |
|                 | 0,931   | 0,005   | 0,964     | 0,931  | 0,947     | 0,939 | 0,997    | 0,971    | 7     |
| Weighted Avg.   | 0,963   | 0,009   | 0,964     | 0,963  | 0,963     | 0,955 | 0,994    | 0,985    |       |


#### Confusion Matrix
|  a |  b |  c |  d | e |  f | <-- classified as|
|----|----|----|----|---|----|--------|
| 70 |  0 |  0 |  0 | 0 |  0 |  a = 1 |
|  1 | 74 |  0 |  1 | 0 |  0 |  b = 2 |
|  0 |  2 | 15 |  0 | 0 |  0 |  c = 3 |
|  0 |  0 |  0 | 12 | 0 |  1 |  d = 5 |
|  0 |  0 |  0 |  1 | 8 |  0 |  e = 6 |
|  0 |  0 |  0 |  1 | 1 | 27 |  f = 7 |

> Procure explicar a razão da variação do percentual de classificação obtido.
> Treinando com a base toda o percentual da correlação de acertos sempre será de 100%(acurácia), pois nessa fase ele não tem relações dividas em bases de treinamento e testes como no cross-validation.
> O cross-validation faz o seguinte processo ex: leva 214 dados rotulados Ele produz 10 conjuntos de tamanhos iguais. Cada conjunto é dividido em dois grupos: 90% dos dados rotulados são usados para treinamento e 10% dados rotulados são usados para testes. Ele produz um classificador com um algoritmo a partir de 90% de dados rotulados e aplica-se que nos 10% de dados de teste para o conjunto 1. Ele faz a mesma coisa para o conjunto 2 a 10 e produz mais 9 classificadores Ele calcula a média do desempenho dos 10 classificadores produzidos a partir de 10 conjuntos de tamanhos iguais (90 de treinamento e 10 de teste).
