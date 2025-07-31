# 🕵️‍♂️ OSINT Target Recon

**Ferramenta de Reconhecimento OSINT** para identificar possíveis perfis públicos associados a um domínio, organização ou nome de usuário.

## 📌 Sobre a Ferramenta

Esta ferramenta foi feita para auxiliar em investigações de **Open Source Intelligence (OSINT)**. A ideia principal é automatizar a busca por **perfis públicos** ligados a um determinado alvo, seja ele um domínio ou username.

Atualmente ela faz verificações simples em redes como:

- GitHub
- Twitter

## ⚙️ Como usar

1. Instale as dependências:
```bash
pip install requests
```

2. Execute o script:
```bash
python osint_target_recon.py
```

3. Digite o nome de domínio ou username (ex: `openai`, `hackernews`, `empresa123`)

4. A ferramenta retorna os perfis ativos encontrados.

---

## 🧠 Conceito OSINT

**OSINT (Open Source Intelligence)** é a coleta de informações a partir de fontes públicas como:
- Redes Sociais
- Repositórios Públicos
- Sites de Empresas
- Fóruns
- Bancos de dados de vazamentos

Essa técnica é muito usada por:
- Profissionais de Segurança
- Hackers Éticos
- Investigadores Privados
- Jornalistas

> Essa ferramenta serve como um ponto inicial. Nenhuma invasão é feita — apenas consulta de dados abertos.

---

**Feito por Bellani - 2025**
