async function carregarDesenvolvedoras() {
    const resposta = await fetch("/desenvolvedoras");
    const lista = await resposta.json();

    const tabela = document.getElementById("tabela-desenvolvedoras");
    tabela.innerHTML = "";

    if (lista.length === 0) {
        tabela.innerHTML = "<tr><td colspan='5' class='vazio'>Nenhuma desenvolvedora cadastrada.</td></tr>";
    }

    for (const dev of lista) {
        const linha = document.createElement("tr");
        linha.innerHTML = `
            <td>${dev.id}</td>
            <td>${dev.nome}</td>
            <td>${dev.pais}</td>
            <td>${dev.ano_fundacao}</td>
            <td>
                <button onclick="editarDesenvolvedora(${dev.id})">Editar</button>
                <button class="excluir" onclick="excluirDesenvolvedora(${dev.id})">Excluir</button>
            </td>
        `;
        tabela.appendChild(linha);
    }

    const select = document.getElementById("jogo-desenvolvedora");
    const selecionadoAntes = select.value;
    select.innerHTML = "";

    for (const dev of lista) {
        const opcao = document.createElement("option");
        opcao.value = dev.id;
        opcao.textContent = dev.nome;
        select.appendChild(opcao);
    }
    select.value = selecionadoAntes;
}

document.getElementById("form-desenvolvedora").addEventListener("submit", async function (evento) {
    evento.preventDefault();

    const id = document.getElementById("desenvolvedora-id").value;
    const dados = {
        nome: document.getElementById("desenvolvedora-nome").value,
        pais: document.getElementById("desenvolvedora-pais").value,
        ano_fundacao: Number(document.getElementById("desenvolvedora-ano").value)
    };

    let resposta;
    if (id === "") {
        resposta = await fetch("/desenvolvedoras", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });
    } else {
        resposta = await fetch("/desenvolvedoras/" + id, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });
    }

    if (!resposta.ok) {
        const erro = await resposta.json();
        alert(erro.detail);
        return;
    }

    limparFormularioDesenvolvedora();
    await carregarDesenvolvedoras();
    await carregarJogos();
});

async function editarDesenvolvedora(id) {
    const resposta = await fetch("/desenvolvedoras/" + id);
    const dev = await resposta.json();

    document.getElementById("desenvolvedora-id").value = dev.id;
    document.getElementById("desenvolvedora-nome").value = dev.nome;
    document.getElementById("desenvolvedora-pais").value = dev.pais;
    document.getElementById("desenvolvedora-ano").value = dev.ano_fundacao;
    document.getElementById("botao-salvar-desenvolvedora").textContent = "Salvar alteracoes";
}

async function excluirDesenvolvedora(id) {
    if (!confirm("Excluir esta desenvolvedora?")) {
        return;
    }

    const resposta = await fetch("/desenvolvedoras/" + id, { method: "DELETE" });

    if (!resposta.ok) {
        const erro = await resposta.json();
        alert(erro.detail);
        return;
    }

    await carregarDesenvolvedoras();
}

function limparFormularioDesenvolvedora() {
    document.getElementById("form-desenvolvedora").reset();
    document.getElementById("desenvolvedora-id").value = "";
    document.getElementById("botao-salvar-desenvolvedora").textContent = "Cadastrar desenvolvedora";
}

async function carregarJogos() {
    const resposta = await fetch("/jogos");
    const lista = await resposta.json();

    const tabela = document.getElementById("tabela-jogos");
    tabela.innerHTML = "";

    if (lista.length === 0) {
        tabela.innerHTML = "<tr><td colspan='6' class='vazio'>Nenhum jogo cadastrado.</td></tr>";
    }

    for (const jogo of lista) {
        const linha = document.createElement("tr");
        linha.innerHTML = `
            <td>${jogo.id}</td>
            <td>${jogo.titulo}</td>
            <td>${jogo.console}</td>
            <td>${jogo.ano}</td>
            <td>${jogo.desenvolvedora_nome}</td>
            <td>
                <button onclick="editarJogo(${jogo.id})">Editar</button>
                <button class="excluir" onclick="excluirJogo(${jogo.id})">Excluir</button>
            </td>
        `;
        tabela.appendChild(linha);
    }
}

document.getElementById("form-jogo").addEventListener("submit", async function (evento) {
    evento.preventDefault();

    const id = document.getElementById("jogo-id").value;
    const dados = {
        titulo: document.getElementById("jogo-titulo").value,
        console: document.getElementById("jogo-console").value,
        ano: Number(document.getElementById("jogo-ano").value),
        desenvolvedora_id: Number(document.getElementById("jogo-desenvolvedora").value)
    };

    if (!dados.desenvolvedora_id) {
        alert("Cadastre uma desenvolvedora antes de cadastrar um jogo.");
        return;
    }

    let resposta;
    if (id === "") {
        resposta = await fetch("/jogos", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });
    } else {
        resposta = await fetch("/jogos/" + id, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(dados)
        });
    }

    if (!resposta.ok) {
        const erro = await resposta.json();
        alert(erro.detail);
        return;
    }

    limparFormularioJogo();
    await carregarJogos();
});

async function editarJogo(id) {
    const resposta = await fetch("/jogos/" + id);
    const jogo = await resposta.json();

    document.getElementById("jogo-id").value = jogo.id;
    document.getElementById("jogo-titulo").value = jogo.titulo;
    document.getElementById("jogo-console").value = jogo.console;
    document.getElementById("jogo-ano").value = jogo.ano;
    document.getElementById("jogo-desenvolvedora").value = jogo.desenvolvedora_id;
    document.getElementById("botao-salvar-jogo").textContent = "Salvar alteracoes";
}

async function excluirJogo(id) {
    if (!confirm("Excluir este jogo?")) {
        return;
    }

    const resposta = await fetch("/jogos/" + id, { method: "DELETE" });

    if (!resposta.ok) {
        const erro = await resposta.json();
        alert(erro.detail);
        return;
    }

    await carregarJogos();
}

function limparFormularioJogo() {
    document.getElementById("form-jogo").reset();
    document.getElementById("jogo-id").value = "";
    document.getElementById("botao-salvar-jogo").textContent = "Cadastrar jogo";
}

async function iniciar() {
    await carregarDesenvolvedoras();
    await carregarJogos();
}

iniciar();
