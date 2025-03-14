## Cenários de Teste a partir de Imagens

Este projeto permite extrair texto de imagens e gerar cenários de teste automaticamente, utilizando a API da OpenAI e o Tesseract OCR. Além disso, também é possível gerar sugestões de automação de testes em diferentes ferramentas como Cypress, Playwright e Selenium.

## Funcionalidades

- Upload de imagens para extração de texto
- Geração automática de cenários de teste baseados no texto extraído
- Sugestão de código de automação de testes
- Interface interativa utilizando Streamlit

## Tecnologias Utilizadas

- Python
- Streamlit
- OpenAI API
- Tesseract OCR (pytesseract)
- Pillow (PIL)

## Comandos docker

- docker build -t streamlit-app .
- docker run -p 8501:8501 streamlit-qa
- nohub docker run -p 8501:8501 streamlit-qa &