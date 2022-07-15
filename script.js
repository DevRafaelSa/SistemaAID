// Rotas da aplicação e outras variaveis globais
URLfront = "http://localhost:5500/" // URL Frontend
homepage = "home.html" // Página inicial
storageToken = window.sessionStorage.accessToken // Storage do token de acesso

// Rotas da API
URLback = "http://localhost:8000/" // URL Principal do Backend
auth_page = "auth/" // Página de autenticação
api_page = "api/v1/" // Path principal da API


// Fazendo requisição POST na rota de autenticação e validando os dados informados pelo usuário para realizar o login e obter o token de acesso
function loginRequest() {
    let username = document.getElementById("username").value
    let password = document.getElementById("password").value

    fetch(URLback + auth_page, {

        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'username': username,
            'password': password
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.access) {
                window.sessionStorage.accessToken = data.access
                window.location.href = URLfront + homepage
            }
            else {
                let msgErro = document.querySelector("#msgErro")
                let boxTitle = document.querySelector(".boxTitle")
                let boxuser = document.querySelector("#username")
                let boxpass = document.querySelector("#password")
                msgErro.setAttribute("style", "display: block")
                boxTitle.setAttribute("style", "padding-bottom: 30px")
                boxuser.setAttribute("style", "color: red")
                boxpass.setAttribute("style", "color: red")
                msgErro.innerHTML = "Usuário ou senha incorretos"
            }
        })
        .catch(error => {
            console.log(error)
        })
}

// Função para realizar o logout do usuário
function logout() {
    window.sessionStorage.removeItem("accessToken")
    window.location.href = URLfront + 'index.html'
}


// Função para cadastro de Componentes
async function cadComponente() {
    const method = 'POST';
    const body = JSON.stringify({
        'nome': document.getElementById("nome").value,
        'modelo': document.getElementById("modelo").value,
        'descricao': document.getElementById("descricao").value,
    });
    const headers = {
        'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
        'Content-Type': 'application/json'
    }
    const response = await fetch(URLback + api_page + "componente",
        {
            method: method,
            headers: headers,
            body: body
        });
    const data = await response.json();
    if (response.ok || response.status == 200 || response.status == 201) {
        alert('Cadastrado com sucesso!');
    } else if (data.code == 'token_not_valid') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else if (data.code == 'token_not_provided') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else {
        alert('Erro ao cadastrar!');
    }
}


// Função para cadastro de Equipamentos
async function cadEquipamento() {
    const method = 'POST';
    const body = JSON.stringify({
        'nome': document.getElementById("nome").value,
        'modelo': document.getElementById("modelo").value,
        'descricao': document.getElementById("descricao").value,
    });
    const headers = {
        'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
        'Content-Type': 'application/json'
    }
    const response = await fetch(URLback + api_page + "equipamento",
        {
            method: method,
            headers: headers,
            body: body
        });
    const data = await response.json();
    if (response.ok || response.status == 200 || response.status == 201) {
        alert('Cadastrado com sucesso!');
    } else if (data.code == 'token_not_valid') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else if (data.code == 'token_not_provided') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else {
        alert('Erro ao cadastrar!');
    }
}

// Função para cadastro de Ferramentas
async function cadFerramenta() {
    const method = 'POST';
    const body = JSON.stringify({
        'nome': document.getElementById("nome").value,
        'modelo': document.getElementById("modelo").value,
        'descricao': document.getElementById("descricao").value,
    });
    const headers = {
        'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
        'Content-Type': 'application/json'
    }
    const response = await fetch(URLback + api_page + "ferramenta",
        {
            method: method,
            headers: headers,
            body: body
        });
    const data = await response.json();
    if (response.ok || response.status == 200 || response.status == 201) {
        alert('Cadastrado com sucesso!');
    } else if (data.code == 'token_not_valid') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else if (data.code == 'token_not_provided') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else {
        alert('Erro ao cadastrar!');
    }
}


// Função para cadastro de Mobiliarios
async function cadMobiliario() {
    const method = 'POST';
    const body = JSON.stringify({
        'nome': document.getElementById("nome").value,
        'modelo': document.getElementById("modelo").value,
        'descricao': document.getElementById("descricao").value,
    });
    const headers = {
        'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
        'Content-Type': 'application/json'
    }
    const response = await fetch(URLback + api_page + "mobiliario",
        {
            method: method,
            headers: headers,
            body: body
        });
    const data = await response.json();
    if (response.ok || response.status == 200 || response.status == 201) {
        alert('Cadastrado com sucesso!');
    } else if (data.code == 'token_not_valid') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else if (data.code == 'token_not_provided') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else {
        alert('Erro ao cadastrar!');
    }
}


// Função para cadastro de Equipes
async function cadEquipes() {
    const method = 'POST';
    const body = JSON.stringify({
        'nome': document.getElementById("nome").value,
    });
    const headers = {
        'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
        'Content-Type': 'application/json'
    }
    const response = await fetch(URLback + api_page + "equipe",
        {
            method: method,
            headers: headers,
            body: body
        });
    const data = await response.json();
    if (response.ok || response.status == 200 || response.status == 201) {
        alert('Cadastrado com sucesso!');
    } else if (data.code == 'token_not_valid') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else if (data.code == 'token_not_provided') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else {
        alert('Erro ao cadastrar!');
        console.log(data);
    }
}


// Recebendo os registro existentes no Cadastro de Equipes para preencher o campo select de Equipes do formulário de cadastro de Pessoas
async function buscaCadEquipes() {
    // Se a página acessada for a de cadastro de pessoas, então busca os registros existentes no cadastro de equipes
    if (window.location.href.includes("pessoas/cadastrar")) {
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
        // Se a resposta for ok, então preenche as Options do select de Equipes
        if (response.ok || response.status == 200) {
            for (let i = 0; i < data.count; i++) {
                const select = document.querySelector('#EquipeSelect');
                select.options[select.options.length] = new Option(data.results[i].nome, data.results[i].id);
            }
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
        // Caso retorne qualquer erro, então mostra um alerta
        else {
            alert('Não foi possível carregar as Equipes existentes!');
        }
    }
}
buscaCadEquipes();

// Recebendo os registro existentes no Cadastro de Equipes para preencher o campo select de Equipes do formulário de cadastro de Pessoas
async function buscaCadDonatarios() {
    // Se a página acessada for a de cadastro de pessoas, então busca os registros existentes no cadastro de equipes
    if (window.location.href.includes("doacao/donatario/cadastrar")) {
        const method = 'GET';
        const headers = {
            'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
            'Content-Type': 'application/json'
        }
        const response = await fetch(URLback + api_page + "remover-donatario-fila",
            {
                method: method,
                headers: headers,
            });
        const data = await response.json();
        // Se a resposta for ok, então preenche as Options do select de Equipes
        if (response.ok || response.status == 200) {
            for (let i = 0; i < data.count; i++) {
                const select = document.querySelector('#DonatarioSelect');
                select.options[select.options.length] = new Option(data.results[i].nome, data.results[i].id);
            }
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
        // Caso retorne qualquer erro, então mostra um alerta
        else {
            alert('Não foi possível carregar as Equipes existentes!');
            console.log(data);
        }
    }
}
buscaCadDonatarios();

async function cadDoacaoDonatario() {
    let donatario = document.getElementById("DonatarioSelect").value;
    let descricao = document.getElementById("descricao").value;
    
    const method = 'POST';
    const body = JSON.stringify({
        'donatario': donatario,
        'descricao': descricao
    });
    const headers = {
        'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
        'Content-Type': 'application/json'
    }
    const response = await fetch(URLback + api_page + "doacao-donatario",
        {
            method: method,
            headers: headers,
            body: body
        });
    const data = await response.json();
    if (response.ok || response.status == 200 || response.status == 201) {
        alert('Cadastrado com sucesso!');
    } else if (data.code == 'token_not_valid') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else if (data.code == 'token_not_provided') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else {
        alert('Erro ao cadastrar!');
        console.log(data);
    }
}


async function buscaCadParceiros() {
    // Se a página acessada for a de cadastro de pessoas, então busca os registros existentes no cadastro de equipes
    if (window.location.href.includes("doacao/parceiro/cadastrar")) {
        const method = 'GET';
        const headers = {
            'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
            'Content-Type': 'application/json'
        }
        const response = await fetch(URLback + api_page + "parceiro",
            {
                method: method,
                headers: headers,
            });
        const data = await response.json();
        // Se a resposta for ok, então preenche as Options do select de Equipes
        if (response.ok || response.status == 200) {
            for (let i = 0; i < data.count; i++) {
                const select = document.querySelector('#ParceiroSelect');
                if (data.results[i].pjuridica == true) {
                    select.options[select.options.length] = new Option(data.results[i].nome +" ("+ data.results[i].cnpj +")", data.results[i].id);
                } else {
                    select.options[select.options.length] = new Option(data.results[i].nome +" ("+ data.results[i].cpf +")", data.results[i].id);
                }
            }
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
        // Caso retorne qualquer erro, então mostra um alerta
        else {
            alert('Não foi possível carregar as Equipes existentes!');
            console.log(data);
        }
    }
}
buscaCadParceiros();


async function cadDoacaoParceiro() {
    let parceiro = document.getElementById("ParceiroSelect").value;
    let descricao = document.getElementById("descricao").value;
    
    const method = 'POST';
    const body = JSON.stringify({
        'parceiro': parceiro,
        'descricao': descricao
    });
    const headers = {
        'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
        'Content-Type': 'application/json'
    }
    const response = await fetch(URLback + api_page + "doacao-parceiro",
        {
            method: method,
            headers: headers,
            body: body
        });
    const data = await response.json();
    if (response.ok || response.status == 200 || response.status == 201) {
        alert('Cadastrado com sucesso!');
    } else if (data.code == 'token_not_valid') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else if (data.code == 'token_not_provided') {
        alert('Sessão expirada!');
        window.location.href = URLfront + 'index.html';
    } else {
        alert('Erro ao cadastrar!');
        console.log(data);
    }
}



// Função para cadastro de Pessoas
async function cadPessoa() {

    let nome =  document.getElementById("nome").value;
    let email =  document.getElementById("email").value;
    let cpf =  document.getElementById("CPF").value;
    let rgm =  document.getElementById("RGM").value;
    let equipe =  document.getElementById("equipe").value;
    let nivelexp =  document.getElementById("nivelexp").value;
    let txtexp =  document.getElementById("txtexp").value;

    if (nome == "" || email == "" || cpf == "" || rgm == "" || equipe == "" || nivelexp == "" || txtexp == "") {
        alert('Preencha todos os campos!');
    }
    else {

        if (document.getElementById("estagiario").checked) {
            estagiario = true;
        } else {
            estagiario = false;
        }

        if (document.getElementById("monitor").checked) {
            monitor = true;
        } else {
            monitor = false;
        }

        if (document.getElementById("seg").checked) {
            seg = true;
        } else {
            seg = false;
        }

        if (document.getElementById("ter").checked) {
            ter = true;
        } else {
            ter = false;
        }

        if (document.getElementById("qua").checked) {
            qua = true;
        } else {
            qua = false;
        }

        if (document.getElementById("qui").checked) {
            qui = true;
        } else {
            qui = false;
        }

        if (document.getElementById("sex").checked) {
            sex = true;
        } else {
            sex = false;
        }

        if (document.getElementById("sab").checked) {
            sab = true;
        } else {
            sab = false;
        }

        const method = 'POST';
        const body = JSON.stringify({
            'nome': nome,
            'email': email,
            'cpf': cpf,
            'rgm': rgm,
            'equipe': equipe,
            'nivelexp': nivelexp,
            'txtexp': txtexp,
            'estagiario': estagiario,
            'monitor': monitor,
            'seg': seg,
            'ter': ter,
            'qua': qua,
            'qui': qui,
            'sex': sex,
            'sab': sab
        });
        const headers = {
            'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
            'Content-Type': 'application/json'
        }
        const response = await fetch(URLback + api_page + "pessoa",
            {
                method: method,
                headers: headers,
                body: body
            });
        const data = await response.json();
        if (response.ok || response.status == 200 || response.status == 201) {
            alert('Cadastrado com sucesso!');
        } else if (data.code == 'token_not_valid') {
            alert('Sessão expirada!');
            window.location.href = URLfront + 'index.html';
        } else if (data.code == 'token_not_provided') {
            alert('Sessão expirada!');
            window.location.href = URLfront + 'index.html';
        } else if (Object.keys(data).length > 0) {
            console.log(data);
            for (let i = 0; i < Object.keys(data).length; i++) {
                alert(data[Object.keys(data)[i]]);
            }
        } else {
            alert('Erro ao cadastrar:\nConfira o log no console do navegador!');
            console.log(data);
        }
    }
    
}


async function cadParceiro() {

    var pjuridica = document.getElementById("pjuridica");
    var nome = document.getElementById("nome").value;
    var cpf = document.getElementById("cpf").value;
    var cnpj = document.getElementById("cnpj").value;
    var resp = document.getElementById("resp").value;
    var cep = document.getElementById("cep").value;
    var end = document.getElementById("end").value;
    var num = document.getElementById("num").value;
    var comp = document.getElementById("comp").value;
    var bairro = document.getElementById("bairro").value;
    var cidade = document.getElementById("cidade").value;
    var uf = document.getElementById("uf").value
    var tel = document.getElementById("tel").value;

    if (pjuridica.checked) {
        pjuridica = true;
        if (cnpj == "") {
            alert('Para cadastrar uma Pessoa Jurídica é necessário informar o CNPJ!');

        } else if (resp == "") {
            alert('Para cadastrar uma Pessoa Jurídica é necessário informar o Responsável!');

        } else {
                const method = 'POST';
                const body = JSON.stringify({
                    'pjuridica': pjuridica,
                    'nome': nome,
                    'cpf': "",
                    'cnpj': cnpj,
                    'resp': resp,
                    'cep': cep,
                    'end': end,
                    'num': num,
                    'comp': comp,
                    'bairro': bairro,
                    'cidade': cidade,
                    'uf': uf,
                    'tel': tel
                });
                const headers = {
                    'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
                    'Content-Type': 'application/json'
                }
                const response = await fetch(URLback + api_page + "parceiro",
                    {
                        method: method,
                        headers: headers,
                        body: body
                    });
                const data = await response.json();
                if (response.ok || response.status == 200 || response.status == 201) {
                    alert('Cadastrado com sucesso!');
                    console.log(data);
                } else if (data.code == 'token_not_valid') {
                    alert('Sessão expirada!');
                    window.location.href = URLfront + 'index.html';
                } else if (data.code == 'token_not_provided') {
                    alert('Sessão expirada!');
                    window.location.href = URLfront + 'index.html';
                } else if (Object.keys(data).length > 0) {
                    console.log(data);
                    alert('Erro ao cadastrar:\nPreencha todos os campos!');
                } else {
                    alert('Erro ao cadastrar:\nConfira o log do console!');
                    console.log(data);
                }
                console.log(body);

        }
    } else if (! pjuridica.checked) { 
        pjuridica = false; 
        if (cpf == "") {
            alert('Para cadastrar uma Pessoa Física é necessário informar o CPF!');
        } else {

            const method = 'POST';
            const body = JSON.stringify({
                'pjuridica': pjuridica,
                'nome': nome,
                'cpf': cpf,
                'cnpj': "",
                'resp': "",
                'cep': cep,
                'end': end,
                'num': num,
                'comp': comp,
                'bairro': bairro,
                'cidade': cidade,
                'uf': uf,
                'tel': tel
            });
            const headers = {
                'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
                'Content-Type': 'application/json'
            }
            const response = await fetch(URLback + api_page + "parceiro",
                {
                    method: method,
                    headers: headers,
                    body: body
                });
            const data = await response.json();
            if (response.ok || response.status == 200 || response.status == 201) {
                alert('Cadastrado com sucesso!');
                console.log(data);
            } else if (data.code == 'token_not_valid') {
                alert('Sessão expirada!');
                window.location.href = URLfront + 'index.html';
            } else if (data.code == 'token_not_provided') {
                alert('Sessão expirada!');
                window.location.href = URLfront + 'index.html';
            } else if (Object.keys(data).length > 0) {
                console.log(data);
                alert('Erro ao cadastrar:\nPreencha todos os campos!');
            } else {
                alert('Erro ao cadastrar:\nConfira o log no console do navegador!');
                console.log(data);
            }
            console.log(body);
        }
    } 
}

async function cadDonatario() {

    let nome = document.getElementById("nome").value;
    let data_nasc = document.getElementById("data_nasc").value;
    let email = document.getElementById("email").value;
    let cpf = document.getElementById("cpf").value;
    let rg = document.getElementById("rg").value;
    let emissor = document.getElementById("emissor").value;
    let uf = document.getElementById("uf").value;
    let nacion = document.getElementById("nacion").value;
    let sexo = document.getElementById("sexo").value;
    let estado_civil = document.getElementById("estado_civil").value;
    let end = document.getElementById("end").value;
    let numero = document.getElementById("numero").value;
    let complemento = document.getElementById("complemento").value;
    let cidade = document.getElementById("cidade").value;
    let bairro = document.getElementById("bairro").value;
    let cep = document.getElementById("cep").value;
    let tel = document.getElementById("tel").value;
    let estudante = document.getElementById("estudante").value;
    let estuda_unipe = document.getElementById("estuda_unipe");
    let curso_unipe = document.getElementById("curso_unipe").value;
    let trabalhador = document.getElementById("trabalhador");
    let local_trabalho = document.getElementById("local_trabalho").value;
    let is_funcionario_unipe = document.getElementById("is_funcionario_unipe");
    let qtd_pessoas_familia = document.getElementById("qtd_pessoas_familia").value;
    let renda = document.getElementById("renda").value;
    let indica_unipe = document.getElementById("indica_unipe").value;

    data_nasc = data_nasc.split('/');
    data_nasc = data_nasc[0]

    if (nome == "" || data_nasc == "" || email == "" || cpf == "" || rg == "" || emissor == "" || uf == "" || nacion == "" || sexo == "" || estado_civil == "" || end == "" || numero == "" || complemento == "" || cidade == "" || bairro == "" || cep == "" || tel == "" || estudante == "" || curso_unipe == "" || local_trabalho == "" || qtd_pessoas_familia == "" || renda == "" || indica_unipe == "") 
    {
        alert('Preencha todos os campos!')

    } else {
        if (estuda_unipe.checked) {
            estuda_unipe = true;
        } else {
            estuda_unipe = false;
        }

        if (trabalhador.checked) {
            trabalhador = true;
        } else {
            trabalhador = false;
        }

        if (is_funcionario_unipe.checked) {
            is_funcionario_unipe = true;
        } else {
            is_funcionario_unipe = false;
        }

        const method = 'POST';
        const body = JSON.stringify({
            'nome': nome,
            'data_nasc': data_nasc,
            'email': email,
            'cpf': cpf,
            'rg': rg,
            'emissor': emissor,
            'uf': uf,
            'nacion': nacion,
            'sexo': sexo,
            'estado_civil': estado_civil,
            'end': end,
            'numero': numero,
            'complemento': complemento,
            'cidade': cidade,
            'bairro': bairro,
            'cep': cep,
            'tel': tel,
            'estudante': estudante,
            'estuda_unipe': estuda_unipe,
            'curso_unipe': curso_unipe,
            'trabalhador': trabalhador,
            'local_trabalho': local_trabalho,
            'is_funcionario_unipe': is_funcionario_unipe,
            'qtd_pessoas_familia': qtd_pessoas_familia,
            'renda': renda,
            'indica_unipe': indica_unipe
        });
        const headers = {
            'Authorization': 'Bearer ' + window.sessionStorage.accessToken,
            'Content-Type': 'application/json'
        }
        const response = await fetch(URLback + api_page + "donatario",
            {
                method: method,
                headers: headers,
                body: body
            });
        const data = await response.json();
        if (response.ok || response.status == 200 || response.status == 201) {
            alert('Cadastrado com sucesso!');
        } else if (data.code == 'token_not_valid') {
            alert('Sessão expirada!');
            window.location.href = URLfront + 'index.html';
        } else if (data.code == 'token_not_provided') {
            alert('Sessão expirada!');
            window.location.href = URLfront + 'index.html';
        } else if (Object.keys(data).length > 0) {
            console.log(data);
            for (let i = 0; i < Object.keys(data).length; i++) {
                alert(data[Object.keys(data)[i]]);
            }
        } else {
            alert('Erro ao cadastrar:\nConfira o log no console do navegador!');
            console.log(data);
        }
        console.log(body)
    }
}