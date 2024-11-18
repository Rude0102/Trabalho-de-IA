import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from fpdf import FPDF

# Carregar os dados históricos de uma ação, por exemplo, da Yahoo Finance.
data = pd.read_csv("historico_acoes.csv")
data.head()


# Criação de novas features e variáveis alvo
data['Target'] = np.where(data['Close'].shift(-1) > data['Close'], 1, 0)
features = ['Open', 'High', 'Low', 'Close', 'Volume']
X = data[features]
y = data['Target']

# Divisão em dados de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Inicializar e treinar o modelo
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Avaliação preliminar do modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Acurácia do Modelo:", accuracy)
print(classification_report(y_test, y_pred))


# Extração da importância das features
importances = model.feature_importances_
feature_importance = pd.DataFrame({'feature': features, 'importance': importances})
feature_importance = feature_importance.sort_values(by='importance', ascending=False)

# Visualização da importância das features
sns.barplot(x='importance', y='feature', data=feature_importance)
plt.title("Importância das Variáveis")
plt.show()

# Resultados de desempenho
print(f"Acurácia: {accuracy_score(y_test, y_pred)}")
print("Relatório de Classificação:\n", classification_report(y_test, y_pred))



# Classe para o relatório em PDF
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Relatório de Mineração de Dados em Ações", 0, 1, "C")

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, content)
        self.ln()

# Criação do PDF com os dados
pdf = PDFReport()
pdf.add_page()

# Adicionar introdução
pdf.add_section("Introdução", "Este projeto realiza uma análise preditiva com o objetivo de identificar padrões em séries temporais de ações...")

# Adicionar metodologia
pdf.add_section("Metodologia", "Utilizamos RandomForest para detecção de padrões...")

# Adicionar resultados
result_content = f"Acurácia do modelo: {accuracy:.2f}\n\nRelatório de Classificação:\n{classification_report(y_test, y_pred)}"
pdf.add_section("Resultados", result_content)

# Salvar o PDF
pdf.output("relatorio_analise_acoes.pdf")
