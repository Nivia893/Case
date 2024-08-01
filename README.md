# Analisador de Tráfego de Rede

## Descrição
Esta aplicação captura pacotes de uma interface de rede especificada e exibe estatísticas básicas sobre o tráfego capturado.

## Requisitos
- Python 3.x
- Biblioteca Scapy

## Instalação
1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>

Instale as dependências:
Basch:
pip install scapy

Uso

Execute o script traffic_analyzer.py especificando a interface de rede:

python traffic_analyzer.py <INTERFACE>

Exemplo:
```bash

python traffic_analyzer.py eth0


## Docker (Opcional)
Para executar a aplicação em um contêiner Docker:
1. Construa a imagem Docker:
   ```bash
   docker build -t traffic_analyzer .

Execute o contêiner:
docker run --rm --net=host traffic_analyzer <INTERFACE>

Autor

Seu Nome


### Passo 4: Dockerfile (Opcional)

Se você deseja utilizar Docker, crie um arquivo `Dockerfile` com o seguinte conteúdo:

```dockerfile
FROM python:3.9-slim

RUN pip install scapy

COPY traffic_analyzer.py /app/traffic_analyzer.py

WORKDIR /app

ENTRYPOINT ["python", "traffic_analyzer.py"]

Passo 5: Teste e Entrega

Teste a aplicação:

Execute o script localmente para garantir que ele funcione conforme esperado:
python traffic_analyzer.py <INTERFACE>


Teste com Docker (opcional):

Construa a imagem Docker:
docker build -t traffic_analyzer .

Execute o contêiner:
docker run --rm --net=host traffic_analyzer <INTERFACE>


Envie o código:

Crie um repositório no GitHub ou outra plataforma de versionamento de código.
Faça o push do código, incluindo traffic_analyzer.py, README.md e Dockerfile (se aplicável).
Conclusão

Seguindo esses passos, você terá uma aplicação funcional de análise de tráfego de rede que captura pacotes e exibe estatísticas básicas. A documentação e o Dockerfile (opcional) facilitarão a configuração e execução da aplicação. Certifique-se de testar a aplicação em diferentes ambientes para garantir que ela funcione conforme esperado.

Se precisar de mais alguma coisa ou tiver alguma dúvida durante o processo, estou à disposição para ajudar!
