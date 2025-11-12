import joblib
import pandas as pd
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dicionário de nomes legíveis das variáveis (para exibição no site)
NOMES_LEGIVEIS = {
    "person_age": "Idade",
    "person_income": "Renda",
    "loan_amnt": "Valor do Empréstimo",
    "loan_int_rate": "Taxa de Juros",
    "loan_to_income_ratio": "Proporção Empréstimo/Renda",
    "person_home_ownership_MORTGAGE": "Casa Financiada",
    "person_home_ownership_OWN": "Casa Própria",
    "person_home_ownership_RENT": "Casa Alugada",
    "loan_intent_EDUCATION": "Motivo do Empréstimo: Educação",
    "loan_intent_HOMEIMPROVEMENT": "Motivo do Empréstimo: Reforma Residencial",
    "loan_intent_PERSONAL": "Motivo do Empréstimo: Uso Pessoal",
    "loan_intent_VENTURE": "Motivo do Empréstimo: Empreendimento",
    "loan_intent_DEBTCONSOLIDATION": "Motivo do Empréstimo: Consolidação de Dívidas",
    "loan_intent_MEDICAL": "Motivo do Empréstimo: Saúde",
    "loan_grade_A": "Score de Crédito - 900+",
    "loan_grade_B": "Score de Crédito - 800-900",
    "loan_grade_C": "Score de Crédito - 700-800",
    "loan_grade_D": "Score de Crédito - 600-700",
    "loan_grade_E": "Score de Crédito - 600-500",
    "loan_grade_F": "Score de Crédito - 500-400",
    "loan_grade_G": "Score de Crédito - > 400",
    "cb_person_default_on_file_Y": "Histórico de Inadimplência: Sim",
    "cb_person_default_on_file_N": "Histórico de Inadimplência: Não"
}


def carregar_modelo(caminho_modelo="ml_models/XGBClassifier_simulador.pkl",
                    caminho_colunas="ml_models/feature_columns_simulador.pkl",
                    caminho_preproc="ml_models/preprocessor_simulador.pkl",
                    caminho_taxas="ml_models/taxas_por_grade.pkl",):
    """
    Carrega o modelo, o pré-processador e as colunas salvas durante o treino.
    """

    if not os.path.exists(caminho_modelo):
        raise FileNotFoundError(f"Modelo não encontrado em: {caminho_modelo}")
    modelo = joblib.load(caminho_modelo)
    print(f"Modelo carregado: {modelo.__class__.__name__}")

    if not os.path.exists(caminho_preproc):
        raise FileNotFoundError(f"Pré-processador não encontrado em: {caminho_preproc}")
    preprocessor = joblib.load(caminho_preproc)
    print(f"Pré-processador carregado com sucesso!")

    if not os.path.exists(caminho_colunas):
        raise FileNotFoundError(f"Arquivo de colunas não encontrado em: {caminho_colunas}")
    feature_cols = joblib.load(caminho_colunas)
    print(f"Colunas carregadas ({len(feature_cols)} features).")

    return modelo, preprocessor, feature_cols

def preprocessar_dados(dados_cliente, preprocessor, feature_cols):
    """
    Recebe os dados de um cliente fictício, aplica o pré-processamento e retorna o DataFrame pronto para o modelo.
    """
    #Convertendo o dicionário em DataFrame
    df_input = pd.DataFrame([dados_cliente])

    print("\nDados brutos recebidos:")
    print(df_input)

    #Aplicando o pré-processador
    X_ready = preprocessor.transform(df_input)

    #Criando o DataFrame com os nomes das colunas originais usadas no treino
    X_ready_df = pd.DataFrame(X_ready, columns=feature_cols)

    print("\nAmostra dos dados processados:")
    print(X_ready_df.head(1))

    return X_ready_df

def prever_risco_credito(modelo, X_ready, threshold=0.3):
    """
    Gera a previsão de inadimplência com base nos dados processados.
    Retorna dicionário com o risco e decisão de crédito.
    """

    # Garante que o modelo suporte predict_proba
    if not hasattr(modelo, "predict_proba"):
        raise ValueError("O modelo não suporta previsão de probabilidade.")

    # Probabilidade de inadimplência (classe 1)
    prob_default = modelo.predict_proba(X_ready)[:, 1][0]

    # Aplica a regra de decisão
    aprova = prob_default < threshold

    # Mensagem humanizada
    resultado = "✅ Crédito Aprovado" if aprova else "❌ Crédito Negado"

    print(f"\nResultado: {resultado} | Risco de inadimplência: {prob_default*100:.2f}%")

    return {
        "resultado": resultado,
        "risco_inadimplencia": round(prob_default, 4),
        "aprova": aprova
    }

def carregar_importancias():
    """Carrega o arquivo de importâncias salvo após o treino e converte para tipos nativos do Python."""
    caminhos = [
        os.path.join(BASE_DIR, "feature_importance.pkl"),
        os.path.join(BASE_DIR, "models", "feature_importance.pkl"),
        os.path.join("ml_models", "feature_importance.pkl"),
    ]

    for path in caminhos:
        if os.path.exists(path):
            print(f"📊 Importâncias carregadas de: {path}")
            importancias = joblib.load(path)

            # Converte para float nativo
            importancias = {k: float(v) for k, v in importancias.items() if v is not None}
            print(f"Total de variáveis carregadas: {len(importancias)}")
            return importancias

    print("⚠️ Nenhum arquivo de importâncias encontrado.")
    return {}

def calcular_importancias(modelo, feature_cols):
    """Calcula a importância das variáveis do modelo."""
    importancias = modelo.feature_importances_
    return dict(zip(feature_cols, importancias))

def explicar_previsao(X_ready, importancias):
    """
    Estima os fatores mais influentes na previsão atual.
    Multiplica os valores absolutos do input pelas importâncias do modelo,
    normalizando o resultado para exibição proporcional.
    """

    # 🔧 Corrige nomes de colunas (remove prefixos)
    importancias = {
        k.replace("num__", "")
         .replace("cat__", "")
         .replace("onehotencoder__", "")
         .replace("x0__", "")
         .replace("preprocessor__", "")
         .replace("remainder__", ""): v
        for k, v in importancias.items()
    }

    # Garante que todas as colunas do input existam nas importâncias
    feature_weights = {
        k: importancias.get(k, 0.0) for k in X_ready.columns
    }

    # Usa valores absolutos e normaliza por max (mantém proporções)
    valores = np.abs(X_ready.iloc[0].to_numpy())
    pesos = np.array(list(feature_weights.values()))
    influencias = valores * pesos

    # Normaliza para escala 0–1
    if influencias.sum() > 0:
        influencias = influencias / influencias.sum()

    # Cria dicionário nome → influência
    score_influence = dict(zip(X_ready.columns, influencias))

    # Cria dicionário nome → influência (com tradução legível)
    score_influence = {
        NOMES_LEGIVEIS.get(k, k): float(v)
        for k, v in zip(X_ready.columns, influencias)
    }

    # Retorna as 5 features mais influentes
    explicacao = sorted(score_influence.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\n📊 Fatores mais influentes nesta previsão:")
    for nome, val in explicacao:
        print(f"  {nome}: {val:.4f}")
    return explicacao

if __name__ == '__main__':
    modelo, preproc, cols = carregar_modelo()

    dados_teste = {
        "person_age": 30,
        "person_income": 50000,
        "person_home_ownership": "RENT",
        "loan_intent": "PERSONAL",
        "loan_grade": "C",
        "loan_amnt": 8000,
        "loan_int_rate": 12.5,
        "loan_to_income_ratio": 0.16,
        "cb_person_default_on_file": "N",
        "cb_person_cred_hist_length": 3
    }

    X_ready = preprocessar_dados(dados_teste, preproc, cols)
    resultado = prever_risco_credito(modelo, X_ready, threshold=0.3)

    print(resultado)