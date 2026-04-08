# projeto-automacao-industrial-python
Protótipo de automação industrial desenvolvido em Python para controle de produção, triagem de qualidade e gestão logística de armazenamento. Projeto acadêmico para a disciplina de Algoritmos e Lógica de Programação - UniFECAF/ Rocketseat.


🏭 Sistema de Automação Industrial - Python
Este projeto consiste em um protótipo de software para controle de qualidade e gestão logística em uma linha de produção industrial.

🚀 Como Executar o Projeto
Certifique-se de ter o Python instalado.

No terminal do VS Code / Codespaces, digite o comando abaixo e pressione Enter:

Bash
python automacao.py


🛠️ Funcionalidades
Controle de Qualidade: Validação automática de peso (95g-105g), cor (azul/verde) e comprimento (10cm-20cm).

Gestão de Estoque: Contagem automática de peças aprovadas e fechamento de caixas a cada 10 unidades.

Monitoramento: Visualização em tempo real do status das caixas e peças na esteira.

Relatórios: Consolidação de dados de produtividade e motivos de reprovação.


📋 Regras de Negócio (Critérios de Aceite)
Para que uma peça seja considerada APROVADA, ela deve cumprir:

Peso: Entre 95g e 105g.

Cor: Exclusivamente "azul" ou "verde".

Comprimento: Entre 10cm e 20cm.