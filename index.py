import streamlit as st
from PIL import Image
import io
import openai
import pytesseract

openai.api_key = "YOUR_API_KEY"

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image, lang='eng')
    return text

def generate_test_scenarios(extracted_text):
    prompt = f"""
    Baseado no seguinte texto extraído de uma imagem:
    \"{extracted_text}\"
    Crie cenários de teste detalhados, incluindo:
    - Objetivo do teste
    - Passos
    - Resultados esperados
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um especialista em geração de cenários de teste."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

st.title("Cenários de Teste a partir de Imagens")
st.write("Faça upload de uma imagem e receba cenários de teste baseados no texto extraído.")

uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagem Carregada", use_column_width=True)
    
    with st.spinner("Extraindo texto da imagem..."):
        extracted_text = extract_text_from_image(image)
    
    if extracted_text.strip():
        with st.spinner("Gerando cenários de teste..."):
            test_scenarios = generate_test_scenarios(extracted_text)
        
        st.subheader("Cenários de Teste Gerados:")
        st.write(test_scenarios)
    else:
        st.error("Não foi possível extrair texto significativo da imagem.")

automacao = st.selectbox("Gostaria de gerar automação desta tela em:", ["Cypress", "Playwrigth", "Selenium"])

if st.button("Gera automação"):    
    with st.spinner("Gerando automação..."):
        prompt = f"""
            Baseado no seguinte texto extraído de uma imagem:
            \"{extracted_text}\"
            Crie automação de teste na ferramenta {automacao}.
            Com um código de exemplo de erro e sucesso.
            """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em geração de automação de teste."},
                {"role": "user", "content": prompt}
            ],
        )

        recomendacao = response['choices'][0]['message']['content'].strip()
        st.write("### Recomendação de Automação:")
        st.write(recomendacao)

st.write("Feito por JFilhoGN - 2024")