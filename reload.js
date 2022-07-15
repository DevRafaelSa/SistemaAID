URLback = "http://localhost:8000/" // URL Principal do Backend
api_page = "api/v1/" // Path principal da API
URLfront = "http://localhost:5500/" // URL Frontend

// Função de retorno para index.html caso token esteja expirado. Faz uma requsição GET numa rota qualquer apenas para verificar se o token está válido.
async function tokenExpirado() {

        const method = 'GET';
        const headers = {
            'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
            'Content-Type': 'application/json'
        }
        const response = await fetch(URLback + api_page + "equipe",
            {
                method: method,
                headers: headers,
            });
        const data = await response.json();
        // Se o token for válido, não faz nada, mantém tudo como está.
        if (response.ok || response.status == 200) {
            
            // Se o token de sessão expirou, então redireciona para a página de login
        } else if (data.code == 'token_not_valid') {
            alert('Sessão expirada!');
            window.location.href = URLfront + 'index.html';
        }
        // Se o token de sessão for inválido, então redireciona para a página de login
        else if (data.code == 'token_not_provided') {
            alert('Sessão expirada!');
            window.location.href = URLfront + 'index.html';
        } 
}
tokenExpirado();