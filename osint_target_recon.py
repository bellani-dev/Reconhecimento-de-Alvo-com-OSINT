import requests

def get_social_links(domain):
    print(f"[*] Buscando perfis sociais ligados ao domínio: {domain}")
    # Exemplo simples com GitHub e Twitter
    possible_links = [f"https://github.com/{domain}", f"https://twitter.com/{domain}"]
    for link in possible_links:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                print(f"[+] Possível perfil encontrado: {link}")
            else:
                print(f"[-] Nenhum perfil ativo em: {link}")
        except Exception as e:
            print(f"[!] Erro ao verificar {link}: {e}")

def main():
    print("### OSINT Target Recon Tool ###")
    domain = input("Insira um domínio, nome de usuário ou organização: ").strip()
    get_social_links(domain)

if __name__ == "__main__":
    main()
