# Mapa do Business Drivers

*DN1 - Experiência do Entregador e Feedback Estruturado*
- Requisito: O sistema deve oferecer um mecanismo nativo de feedback dentro do app, garantindo que pelo menos 50% dos entregadores ativos forneçam feedback mensalmente.
- Métrica: Respostas aos formulários devem ser coletadas automaticamente e analisadas com base em tendências de churn e insatisfação.
- Monitoramento: Se a taxa de resposta cair abaixo de 30%, um alerta deve ser gerado para incentivar novas pesquisas.

*DN3 - Eficiência e Distribuição da Frota do Turbo 10*
- Requisito: A distribuição da frota do Turbo 10 deve garantir que 95% dos pedidos sejam atribuídos a um entregador dentro de 30 segundos após a solicitação.
- Métrica: O tempo médio de alocação de entregador deve ser inferior a 15 segundos para pedidos de Retail. Para Restaurantes e Mercados, o tempo médio de alocação não pode ultrapassar 20 segundos. Se mais de 5% dos pedidos permanecerem sem entregador por mais de 60 segundos, um alerta deve ser disparado.
- Monitoramento: O sistema deve rastrear e ajustar automaticamente a frota com base na demanda por vertente (Retail, Restaurante, Mercado). Caso uma vertente específica tenha um tempo de alocação 50% maior que a média das outras, um alerta deve ser gerado para reavaliar a distribuição da frota.
