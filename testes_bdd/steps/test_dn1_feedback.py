from behave import given, when, then
import random

entregadores_ativos = 1000
feedbacks = []

@given('que há {total_entregadores:d} entregadores ativos na plataforma')
def step_define_entregadores(context, total_entregadores):
    context.total_entregadores = total_entregadores

@when('pelo menos {meta_feedback:d} entregadores enviam feedback dentro do mês')
def step_recebe_feedback_sucesso(context, meta_feedback):
    context.feedbacks_recebidos = meta_feedback

@then('o sistema deve registrar que a meta mensal de feedback foi atingida')
def step_valida_meta_feedback(context):
    assert context.feedbacks_recebidos >= context.total_entregadores * 0.5, "Meta não atingida!"


@when('menos de {limite_feedback:d} entregadores enviam feedback dentro do mês')
def step_recebe_feedback_alerta(context, limite_feedback):
    context.feedbacks_recebidos = limite_feedback

@then('o sistema deve alertar para incentivar novas pesquisas')
def step_verifica_alerta_feedback(context):
    if context.feedbacks_recebidos < context.total_entregadores * 0.3:
        context.alerta_gerado = True
    else:
        context.alerta_gerado = False
    assert context.alerta_gerado, f"Alerta não foi gerado corretamente! ({context.feedbacks_recebidos}/{context.total_entregadores})"

@given('que os feedbacks recebidos apresentam notas abaixo de {limite_nota:f} em uma escala de 5')
def step_feedback_negativo(context, limite_nota):
    context.media_feedbacks = limite_nota - 0.5  

@when('a média da nota dos feedbacks estiver abaixo do valor mínimo aceitável')
def step_verifica_media_feedback(context):
    context.feedback_negativo = context.media_feedbacks < 3.0

@then('o sistema deve gerar um relatório de tendências e sugerir ações corretivas')
def step_gera_relatorio_feedback(context):
    assert context.feedback_negativo, "Nenhum relatório gerado, pois a média não está abaixo do limite!"
