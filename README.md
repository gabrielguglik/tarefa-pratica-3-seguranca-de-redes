# Bem-vindo ao iFood - Autenticação de dois fatores (2FA)!

Aplicação para simular o pedido de um prato de comida para um restaurante, simulando um sistema de iFood:


## Estrutura do projeto

### Auth.py
Contém as funções para gerar o QR Code e para verificar o código TOTP.

### Crypto.py
É onde se concentram as funções de criptografia: 
- derivação da chave de sessão usando PBKDF2; 
- cifragem do comprovante usando AES-GCM e 
- decifração do comprovante.

### Main.py
Código principal, onde é feita a interface com o usuário e a chamada dos métodos principais.

### Utils.py
Lógicas auxiliares de escolha de prato, envio do pedido ao restaurante, cálculo do horário de chegada e solicitação do código TOTP.


## Instalação

Abra o terminal do seu VSCode e instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Após instalar as dependências, execute o main:

```
python main.py
```

Agora, é só seguir os passos abaixo:

1. Escolha seu prato de comida;
2. Informe seu número de telefone;
3. Vá até o arquivo gerado: qrcode.png;
4. Leia o QR Code com seu celular (app recomendado: Google Authenticator) e digite o código obtido na tela para enviar para o sistema;
5. O sistema valida o código obtido como 2º fator de autenticação;
6. O sistema decifra o comprovante e envia o pedido para o restaurante.
7. O sistema envia uma mensagem cifrada, avisando o horário que o pedido
deve chegar.



## Contribuidores

Gabriel Guglielmi Kirtschig - 21200417

Kamilly Victória Ruseler - 21204042

