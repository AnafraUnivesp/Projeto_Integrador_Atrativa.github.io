# Anotações

Passo 01

Instalar o Python na máquina

* http://127.0.0.1:5000 : Ip local de desesenvolvimento + porta 
* Será mudada para http://localhost.5000
* Realizamos uma requisição através do localhost, porém não informamos a rota para retorno nas informações
* Ao verificar o log nos deparamos com 3 etapas de retorno do servidor we:
    * Método: GET (pesquisar metodos)
    * Rota: /
    * Código de Status de retorno: 404 ( pesquisar status codeweb) <!-- 202: requisão bem sucedida e o servidor retorno o que foi solicitado | 404: A rota solicitada não foi encontrada no servidor | 405: A rota existe, porém o método de requisão usado não é suportado por essa rota( GET,PUT e etc) | 500: Erro no servidor que impediu a requisição e gerou algum erro no backend -->


    * O cliente fez a requição da rota principal ( rota /), o backend encontrou essa rota e executou a função atrelada à rota e a função retornou uma resposta exibida no site. O site retornou o status 200

