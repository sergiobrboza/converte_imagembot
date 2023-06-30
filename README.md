[convert_imagembot](https://web.telegram.org/k/#@Image_convertBot)

[![GitHub Follow](https://img.shields.io/github/followers/sergiobrboza)](https://github.com/sergiobrboza)





# Bot do Telegram para Conversão de Imagens

Este é um bot do Telegram desenvolvido em Python que permite aos usuários converter imagens para diferentes formatos.

E esses formatos são:
- PNG, ICO, PDF, JPEG, TIFF, BMP, DIB, EPS, IM, PCX, PPM, SGI, TGA e WEBP.

## Funcionalidades

- Recebe uma foto enviada pelo usuário.
- Suporta diferentes formatos de imagem.
- Converte a imagem para o formato selecionado pelo usuário.
- Envia o arquivo convertido de volta para o usuário.

## Configuração

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias executando o seguinte comando no terminal:

pip install pyTelegramBotAPI pillow

3. Copie a chave de API do seu bot do [Telegram](https://web.telegram.org/k/), que foi fornecida pelo BotFather.
4. No código-fonte, substitua `'SEU_TOKEN'` pela sua chave de API no trecho:

```
chave_api = 'SEU_TOKEN'
Executando o Bot
Para executar o bot, execute o seguinte comando no terminal:

Copy code
python converte_imagembot.py
Certifique-se de estar no diretório correto onde o arquivo do bot está localizado.
```
## Utilização
1. Inicie o bot enviando o comando /start.
2. Envie uma foto para o bot.
3. Selecione o formato de conversão entre as opções apresentadas.
4. O bot irá converter a imagem para o formato selecionado e enviar de volta para você.
## Contribuição
Contribuições são bem-vindas! Se você tiver alguma melhoria ou correção para sugerir, fique à vontade para abrir uma solicitação pull.
