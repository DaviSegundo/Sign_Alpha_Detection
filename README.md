# Projeto de reconhecimento do alfabeto de libras em tempo real

Projeto de detecção das letras do alfabeto de libras usando o **TensorFlow** para a estruturação da parte de aprendizado e **OpenCV** para a captura em tempo real das imagens.


## Exemplo das letras do alfabeto:

<p align='center'>
    <img src='./docs/american_sign_language.PNG' height=400>
</p>

Para esse projeto não iremos trabalhar com algumas letras em específico, como o "J" e o "Z", que na linguagem de sinais são representados por um movimento e não por uma posição estática.

<p align='center'>
    <img src='./docs/amer_sign2.png' height=450>
</p>

## Rede Neural Convolucional (CNN)

A arquitetura da rede que vai ser utilizada nesse projeto consiste de uma serie de camadas covolucionais para a detecção de features importantes de cada imagem.


### Dados do treinamento

É possível perceber que a rede conseguiu identificar rapidamente as features mais importantes e foi melhorando a função custo e a acurácia constantemente.

<p align='center'>
    <img src='./models/training_data.png' height=650>
</p>

Vale destacar que o callback de redução do learning rate foi ativado uma vez perto final do treinamento, o que contribuiu consideralvemnte para a melhora da acurácia do modelo, fazendo ele conseguir atingir os 99% e assim, parando o treinamento previamente.

Ao final do treinamento os seguintes gráficos foram obtidos.

<p align='center'>
    <img src='./models/train_per_epochs.png'>
</p>

Além disso, vale destacar algumas métricas importantes para a validação do modelo.

#### Confusion Matrix

<p align='center'>
    <img src='./docs/confusion_matrix.png' height=650>
</p>

As taxas de acerto das predições corretas estão bem altas e os casos em que foi observados mais erros são de letras que realmente tem muita semelhança.

#### Classification Report

<p align='center'>
    <img src='./docs/class_report.png' >
</p>

#### Análise de Casos Corretos e Incorretos

##### Casos Corretos

<p align='center'>
    <img src='./docs/correct.png' height=300>
</p>

##### Casos Incorretos

<p align='center'>
    <img src='./docs/wrong.png' height=300>
</p>

É possível perceber que o modelo ficou bem construido e que está errando muito pouco.

## Predição em Tempo Real

Para isso vamos construir um programa para capturar a imagem e realizar o tratamento, utilizando **OpenCV**.

### Exemplos de predições feitas em tempo real.
<div class="row">
  <div class="column" align='center'>
    <img src="./docs/real_time_pred.png" height=300>
    <img src="./docs/real_time_pred2.png" height=300>
    <img src="./docs/real_time_pred3.png" height=300>
    <img src="./docs/real_time_pred4.png" height=300>
  </div>
</div>


