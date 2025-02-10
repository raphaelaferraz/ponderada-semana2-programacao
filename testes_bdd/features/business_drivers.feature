Feature: Validação dos Business Drivers do AppTurbo10

  # DN1 - Experiência do Entregador e Feedback Estruturado
  Scenario: Coleta de feedback dos entregadores atinge a meta mensal
    Given que há 1000 entregadores ativos na plataforma
    When pelo menos 500 entregadores enviam feedback dentro do mês
    Then o sistema deve considerar a meta mensal como atingida

  Scenario: Taxa de resposta dos feedbacks cai abaixo do limite de alerta
    Given que há 1000 entregadores ativos na plataforma
    When menos de 300 entregadores enviam feedback dentro do mês
    Then o sistema deve gerar um alerta para incentivar novas pesquisas

  Scenario: Análise de feedback detecta aumento na insatisfação dos entregadores
    Given que os feedbacks recebidos apresentam notas abaixo de 3.0 em uma escala de 5
    When a média da nota dos feedbacks estiver abaixo do valor mínimo aceitável
    Then o sistema deve gerar um relatório de tendências e sugerir ações corretivas

  # DN2 - Eficiência e Distribuição da Frota do Turbo 10
  Scenario: Atribuição de entregador ocorre dentro do tempo esperado
    Given que um cliente solicita uma entrega via AppTurbo10
    When o sistema aloca um entregador em menos de 30 segundos
    Then o pedido deve ser considerado como atendido dentro do SLA

  Scenario: Alerta gerado para pedidos sem alocação de entregador
    Given que um cliente solicita uma entrega via AppTurbo10
    When o sistema não consegue alocar um entregador dentro de 60 segundos
    Then um alerta deve ser gerado para redistribuir a frota ou acionar medidas emergenciais

  Scenario: Ajuste dinâmico da frota baseado na demanda
    Given que a demanda por entregadores em uma vertente específica aumenta em 50% em relação à média das outras
    When o tempo médio de alocação ultrapassa o limite esperado para essa vertente
    Then um alerta deve ser gerado para reavaliar a distribuição da frota

  Scenario: Tempo médio de alocação respeita limites por categoria
    Given que um cliente solicita uma entrega na categoria "Retail"
    When o tempo médio de alocação do entregador for inferior a 15 segundos
    Then o sistema deve considerar o SLA cumprido para essa categoria

    Given que um cliente solicita uma entrega na categoria "Restaurantes e Mercados"
    When o tempo médio de alocação do entregador for inferior a 20 segundos
    Then o sistema deve considerar o SLA cumprido para essa categoria