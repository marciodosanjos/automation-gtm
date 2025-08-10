from typing import Any

class Variable:
    name: str
    type: str
    params: dict

    def __init__(self, name: str, type: str, params:dict):
        self.name = name
        self.type = type
        self.params = params



#c = constant
#jsm = custom js
#dlv = data layer


""""
Tipos de Variáveis Comuns
c - Constant: Uma variável que retorna sempre um valor constante. É um dos tipos mais simples.

jsm - Custom JavaScript: Permite que você escreva seu próprio código JavaScript para retornar um valor.

dlv - Data Layer Variable: Retorna valores do objeto dataLayer.

gtm - Google Tag Manager Container ID: Retorna o ID do contêiner do GTM atual.

e - Event Name: Retorna o nome do evento atual.

j - JavaScript Variable: Retorna o valor de uma variável JavaScript global, como document.title.

r - Random Number: Gera e retorna um número aleatório.

u - URL: Permite extrair partes da URL, como o hostname, o path, ou parâmetros de query.

f - First-Party Cookie: Retorna o valor de um cookie de primeira parte.

ref - HTTP Referrer: Retorna a URL da página de referência.

ct - Container Version: Retorna a versão do contêiner atual.

dom - DOM Element: Retorna um valor de um elemento HTML da página.

cid - Click ID: Retorna o ID do elemento clicado.

uv - User-Defined Variable: Este tipo é usado para variáveis que você cria na interface e não são de um dos tipos acima.

ut - UTM Campaign Parameter: Retorna o valor de um parâmetro UTM da URL.

gaa - Google Analytics Setting: Representa as configurações de uma tag do Google Analytics.

gaz - Google Analytics Measurement ID: Representa o ID de medição do Google Analytics 4 (GA4).

gv - Built-In Variable: É o tipo para variáveis integradas do GTM (como Click Text, Page Path, etc.).

Exemplo de Código para uma Variável dlv
O type da variável determina a estrutura do objeto params (ou parameter, na API). Por exemplo, para criar uma variável do tipo Data Layer (dlv), você precisaria de uma estrutura como esta, onde o key é "na
"""

