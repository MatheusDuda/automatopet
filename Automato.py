# Mapeamento de letras para eventos do processo
mapa_eventos = {
    'a': "Início",
    'b': "Receber Pré-forma",
    'c': "Repetir aquecimento",
    'd': "Aquecimento",
    'e': "Sopro e Moldagem",
    'f': "Resfriamento",
    'g': "Repetir resfriamento",
    'h': "Inspeção de Qualidade",
    'i': "Reprovação",
    'j': "Envase",
    'k': "Falha no Envase",
    'l': "Fechamento",
    'm': "Falha no Fechamento",
    'n': "Retirar Tampa",
    'o': "Rotulagem",
    'p': "Erro no Rótulo",
    'q': "Retirar Rótulo",
    'r': "Embalagem Final"
}

# Transições do autômato
transicoes = {
    ("q0", "Início"): "q1",
    ("q1", "Receber Pré-forma"): "q2",
    ("q2", "Repetir aquecimento"): "q2",
    ("q2", "Aquecimento"): "q3",
    ("q3", "Sopro e Moldagem"): "q4",
    ("q4", "Resfriamento"): "q5",
    ("q4", "Repetir resfriamento"): "q4",
    ("q5", "Inspeção de Qualidade"): "q6",
    ("q5", "Reprovação"): "q2",
    ("q6", "Envase"): "q7",
    ("q6", "Falha no Envase"): "q2",
    ("q7", "Fechamento"): "q8",
    ("q7", "Falha no Fechamento"): "qr1",
    ("qr1", "Retirar Tampa"): "q7",
    ("q8", "Rotulagem"): "q9",
    ("q8", "Erro no Rótulo"): "qr2",
    ("qr2", "Retirar Rótulo"): "q8",
    ("q9", "Embalagem Final"): "qf"
}

# Função principal
def simular_customizado(codigo):
    estado_atual = "q0"
    print("🧪 Simulador com Entrada Personalizada")
    print(f"🔤 Código digitado: {codigo}")
    print("-" * 40)

    for letra in codigo:
        evento = mapa_eventos.get(letra)
        if not evento:
            print(f"❌ Letra inválida: '{letra}'")
            return

        input(f"\nPressione ENTER para executar: '{evento}'")
        chave = (estado_atual, evento)
        if chave in transicoes:
            proximo_estado = transicoes[chave]
            print(f"✅ {estado_atual} --[{evento}]--> {proximo_estado}")
            estado_atual = proximo_estado
        else:
            print(f"❌ ERRO: Transição inválida de {estado_atual} com '{evento}'")
            return

    print(f"\n🏁 Processo finalizado no estado: {estado_atual}")

# Exemplo de uso
codigo_usuario = input("Digite a sequência de letras do processo (ex: abcddef...): ").lower()
simular_customizado(codigo_usuario)