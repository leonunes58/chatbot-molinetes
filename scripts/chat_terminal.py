"""Converse com o bot no terminal, sem WhatsApp.

Uso:  python -m scripts.chat_terminal
Mostra a intenção e a confiança de cada mensagem (útil para achar frases que o modelo erra).
"""
from app.bot import responder
from app.nlp.classificador import prever


def main() -> None:
    print("Chat de teste (digite 'sair' para encerrar)\n")
    while True:
        texto = input("Você: ").strip()
        if texto.lower() == "sair":
            break
        p = prever(texto)
        print(f"   [intenção: {p.intencao} | confiança: {p.confianca:.0%}]")
        resposta = responder("terminal", texto)
        print(f"Bot: {resposta if resposta else '(silêncio: conversa com humano)'}\n")


if __name__ == "__main__":
    main()
