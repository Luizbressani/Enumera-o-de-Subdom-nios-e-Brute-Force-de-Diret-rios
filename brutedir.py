import requests 
import sys
import dns.resolver

resolver = dns.resolver.Resolver()
def brutedir(URL, lista):
	for list in lista:
		try:
			URL_Final = "http://{}/{}".format(URL, list.strip( ))
			response = requests.get(URL_Final)
			code =response.status_code	
			if code != 404:
				print("{} --> {}".format(URL_Final, code))
		except KeyboardInterrupt:
			sys.exit(0)
		except Exception as erro:
			print(erro)
			
def brutesub(url, lista):
	for list in lista:
		try:
			sub = list.strip() 
			URL_Final = "{}.{}".format(sub, URL)
			response = resolver.resolve(URL_Final, "A")
			for resposta in response:
				print("{} --> {}".format(URL_Final, resposta))	
			
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			pass
			
				
if __name__ == "__main__":
    import sys
    URL = sys.argv[1]
    lista = sys.argv[2]
    with open(lista, "r") as file:
        lista = file.readlines()
        escolha = input("Gostaria de realizar uma Enumerção de Subdominios[1] ou um BruteForce de Diretorios[2]? ")
        escolha = int(escolha)  
        if escolha == 1:
            brutesub(URL, lista)
        elif escolha == 2:
            brutedir(URL, lista)
        else:
            print("Escolha inválida")

