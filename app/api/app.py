import time
import boto3

# Importações originais do seu projeto, com o caminho corrigido
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from app.api.routers.auth import auth
from app.api.routers.users import users
from app.api.routers.predict import predict

# Cria a instância principal da aplicação
app = FastAPI(title="Previsão de Ações SAPR4")

# --- INÍCIO DO CÓDIGO DO MIDDLEWARE DE MONITORAMENTO ---

# Cria o "cliente" que se comunica com o CloudWatch.
cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-2')

# Este decorador diz ao FastAPI para executar esta função em toda requisição.
@app.middleware("http")
async def log_latency_metric(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    if request.url.path.startswith(predict.prefix):
        try:
            cloudwatch_client.put_metric_data(
                Namespace='API/Performance',
                MetricData=[
                    {
                        'MetricName': 'Latency',
                        'Dimensions': [
                            {
                                'Name': 'APIName',
                                'Value': 'PrevisaoAcoesSAPR4'
                            },
                        ],
                        'Unit': 'Seconds',
                        'Value': process_time
                    },
                ]
            )
        except Exception as e:
            print(f"Erro ao enviar métrica para o CloudWatch: {e}")

    return response

# --- FIM DO CÓDIGO DO MIDDLEWARE ---

# Inclui as rotas na aplicação (código original)
app.include_router(predict)
app.include_router(users)
app.include_router(auth)

# Rota de redirecionamento para a documentação (código original)
@app.get('/')
async def redirect_to_docs():
    return RedirectResponse(url="/docs", status_code=302)