## Cenários de Teste a partir de Imagens

Repositório com objetivo de estudar o funcionamento do streamlit com geração de cenários de teste integrando com o chatgpt. Para a próxima fase é integra com o ollama

## Comandos docker

- docker build -t streamlit-app .
- docker run -p 8501:8501 streamlit-qa
- nohub docker run -p 8501:8501 streamlit-qa &