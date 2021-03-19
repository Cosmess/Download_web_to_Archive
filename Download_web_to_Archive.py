#Essa ferramenta serve para download de paginas em diversos formatos, desde que o arquivo de criado
# seja correspondente a pagina de origem, exemplo: wwww.pagina.com.br/arquivo.pdf ===> arquivo_de_destino_pdf
import urllib.request, urllib.parse, urllib.error
 
url = input("digite ou cole a url que deseja baixar: ")

#arquivo por padrão será criado na pasta C:\\dir (caso necessario crie a pasta DIR) ou o diretorio do seu criterio
local='C:\\dir\\'

nome = input("digite o nome do arquivo: ")
extensão= input("digite a extensão do arquivo (A extensão deve corresponder ao tipo da pagina):  ")
print("baixando o conteudo....")
urllib.request.urlretrieve(url,local + nome + '.' + extensão)