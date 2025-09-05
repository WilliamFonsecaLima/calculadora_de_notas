import streamlit as st
import math

def aa(nota):
    inteira = math.floor(nota)
    decimal = nota - inteira

    if decimal >= 0.5:
        return inteira + 1
    else:
        return inteira + 0.5 if decimal >= 0.25 else inteira

st.set_page_config(
    page_title="Calculadora de Notas",
    page_icon="🧮",
    layout="wide"
)

# Estilos CSS
st.markdown("""
<style>
    .resultado-aprovado {
        color: #2ecc71;
        font-weight: bold;
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
        background-color: #2ecc7110;
        text-align: center;
    }
    .resultado-exame {
        color: #e74c3c;
        font-weight: bold;
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
        background-color: #e74c3c10;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Título e descrição
st.title("📊 Calculadora de Notas")
st.markdown("""
Calcula sua média final e mostra se você precisa de exame!
* **Peso das notas**: 
  - P1: 30%
  - P2: 30%
  - Prévia: 40%
""")

# Divisão em colunas para organização
col1, col2, col3 = st.columns(3)

with col1:
    p1 = st.number_input("Nota da P1", min_value=0.0, max_value=10.0, step=0.5, format="%.1f")
    
with col2:
    p2 = st.number_input("Nota da P2", min_value=0.0, max_value=10.0, step=0.5, format="%.1f")

with col3:
    previa1 = st.number_input("Nota da Prévia", min_value=0.0, max_value=10.0, step=0.5, format="%.1f")

# Cálculo da média
r = (p1 * 30 + p2 * 30 + previa1 * 40) / 100


# Botão de cálculo
if st.button("Calcular Média", type="primary"):
    # Mostrar resultado
    st.divider()
    
    if r >= 7:
        st.markdown(f'<div class="resultado-aprovado">'
                    f'Sua nota é {r:.1f}. Parabéns você passou! 🎉'
                    f'</div>', unsafe_allow_html=True)
        st.balloons()
    else:
        nm = max(7, 14 - r)  # Garante no mínimo 7
        re = aa(nm)    # arredonda para 0.5
        
        # Cálculo da média final após o exame
        media_final = (r + nm) / 2
        
        # Verifica se o aluno ficará de recuperação
        if nm < 7:
            status = "aprovado após exame"
            classe = "resultado-aprovado"
            emoji = "🎉"
        else:
            status = "de RECUPERAÇÃO"
            classe = "resultado-recuperacao"
            emoji = "⚠️"
        
        st.markdown(f'<div class="resultado-exame">'
                    f'Sua nota é {r:.1f}. Você está de EXAME! ❗<br>'
                    f'Precisa de no minimo {re:.1f} pontos na prova final.<br>'
                    f'</div>', unsafe_allow_html=True)