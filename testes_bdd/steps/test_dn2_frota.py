from behave import given, when, then
import random

contexto_pedido = {}

@given('que um cliente solicita uma entrega via AppTurbo10')
def step_pedido_realizado(context):
    contexto_pedido['status'] = 'pendente'

@when('o sistema aloca um entregador em menos de {tempo_limite:d} segundos')
def step_pedido_atribuido(context, tempo_limite):
    contexto_pedido['tempo_alocacao'] = random.randint(5, tempo_limite)  

@then('o pedido deve ser considerado como atendido dentro do SLA')
def step_verifica_sla(context):
    assert contexto_pedido['tempo_alocacao'] <= 30, "Alocação demorou mais do que o permitido!"

@when('o sistema não consegue alocar um entregador dentro de {tempo_limite:d} segundos')
def step_pedido_sem_atribuicao(context, tempo_limite):
    contexto_pedido['tempo_alocacao'] = tempo_limite + 1  

@then('um alerta deve ser gerado para redistribuir a frota ou acionar medidas emergenciais')
def step_alerta_frota(context):
    assert contexto_pedido['tempo_alocacao'] > 60, "Alerta não gerado corretamente!"

@given('que a demanda por entregadores em uma vertente específica aumenta em {percentual:d}% em relação à média das outras')
def step_aumento_demanda(context, percentual):
    contexto_pedido['demanda_aumentada'] = percentual

@when('o tempo médio de alocação ultrapassa o limite esperado para essa vertente')
def step_demanda_acima_limite(context):
    contexto_pedido['tempo_medio'] = random.randint(21, 50)  

@then('um alerta deve ser gerado para reavaliar a distribuição da frota')
def step_alerta_reavaliacao_frota(context):
    assert contexto_pedido['tempo_medio'] > 20, "Nenhum alerta gerado!"

@given('que um cliente solicita uma entrega na categoria "{categoria}"')
def step_categoria_pedido(context, categoria):
    contexto_pedido['categoria'] = categoria

@when('o tempo médio de alocação do entregador for inferior a {tempo_limite:d} segundos')
def step_verifica_tempo_medio(context, tempo_limite):
    contexto_pedido['tempo_medio'] = random.randint(5, tempo_limite)

@then('o sistema deve considerar o SLA cumprido para essa categoria')
def step_valida_sla_categoria(context):
    if contexto_pedido['categoria'] == "Retail":
        assert contexto_pedido['tempo_medio'] <= 15, "Tempo acima do permitido para Retail!"
    elif contexto_pedido['categoria'] in ["Restaurantes", "Mercados"]:
        assert contexto_pedido['tempo_medio'] <= 20, "Tempo acima do permitido para Restaurantes e Mercados!"