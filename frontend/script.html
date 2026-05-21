document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("registerForm");
  const mensagem = document.getElementById("mensagem");

  // --- ELEMENTOS PARA MÁSCARAS ---
  const inputDataNascimento = document.getElementById("dataNascimento");
  const inputFormatura = document.getElementById("formatura");
  const inputCPF = document.getElementById("cpf");
  const inputCEP = document.getElementById("cep");

  // --- FUNÇÕES DE MÁSCARA (Aplica enquanto o usuário digita) ---
  const aplicarMascara = (input, funcaoMascara) => {
    input.addEventListener("input", (e) => {
      e.target.value = funcaoMascara(e.target.value);
    });
  };

  const mascaraData = (valor) => {
    return valor
      .replace(/\D/g, "") // Remove tudo que não é dígito
      .replace(/(\d{2})(\d)/, "$1/$2") // Adiciona a primeira barra
      .replace(/(\d{2})(\d)/, "$1/$2") // Adiciona a segunda barra
      .replace(/(\d{4})\d+?$/, "$1"); // Limita em 8 dígitos (dd/mm/aaaa)
  };

  const mascaraCPF = (valor) => {
    return valor
      .replace(/\D/g, "")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d)/, "$1.$2")
      .replace(/(\d{3})(\d{1,2})$/, "$1-$2")
      .replace(/(-\d{2})\d+?$/, "$1"); // Limita os dígitos do CPF
  };

  const mascaraCEP = (valor) => {
    return valor
      .replace(/\D/g, "")
      .replace(/(\d{5})(\d)/, "$1-$2")
      .replace(/(-\d{3})\d+?$/, "$1"); // Limita os dígitos do CEP
  };

  // Aplicando as máscaras nos campos corretos
  aplicarMascara(inputDataNascimento, mascaraData);
  aplicarMascara(inputFormatura, mascaraData);
  aplicarMascara(inputCPF, mascaraCPF);
  aplicarMascara(inputCEP, mascaraCEP);

  // --- EVENTO DE SUBMIT DO FORMULÁRIO ---
  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Impede a página de recarregar

    // Captura dos valores dos campos
    const nome = document.getElementById("nome").value.trim();
    const dataNascimento = inputDataNascimento.value;
    const cpf = inputCPF.value;
    const genero = document.getElementById("genero").value;
    const cor = document.getElementById("cor").value;
    const pais = document.getElementById("pais").value.trim();
    const estado = document.getElementById("estado").value.trim();
    const cidade = document.getElementById("cidade").value.trim();
    const cep = inputCEP.value;
    const endereco = document.getElementById("endereco").value.trim();
    const instituicao = document.getElementById("instituicao").value.trim();
    const curso = document.getElementById("curso").value.trim();
    const periodo = document.getElementById("periodo").value.trim();
    const formatura = inputFormatura.value;
    const vaga = document.getElementById("vaga").value.trim();
    const email = document.getElementById("emailCadastro").value.trim();
    const senha = document.getElementById("senhaCadastro").value;
    const confirmarSenha = document.getElementById("confirmarSenha").value;

    // --- VALIDAÇÕES ---

    // 1. Validar se as senhas coincidem
    if (senha !== confirmarSenha) {
      exibirMensagem("As senhas não coincidem. Por favor, verifique.", "error");
      return;
    }

    // 2. Validação simples de tamanho de senha (ex: mínimo 6 caracteres)
    if (senha.length < 6) {
      exibirMensagem("A senha deve ter no mínimo 6 caracteres.", "error");
      return;
    }

    // 3. Validação básica de formato de data (dd/mm/aaaa)
    const regexData = /^\d{2}\/\d{2}\/\d{4}$/;
    if (!regexData.test(dataNascimento)) {
      exibirMensagem("Formato de data de nascimento inválido (dd/mm/aaaa).", "error");
      return;
    }

    // Se houver previsão de formatura preenchida, valida também
    if (formatura && !regexData.test(formatura)) {
      exibirMensagem("Formato da previsão de formatura inválido (dd/mm/aaaa).", "error");
      return;
    }

    // --- CRIAÇÃO DO OBJETO DE DADOS ---
    // Se tudo estiver correto, junta os dados em um objeto pronto para enviar para uma API/Banco de dados
    const dadosCadastro = {
      nome,
      dataNascimento,
      cpf,
      genero,
      cor,
      endereco: { pais, estado, cidade, cep, logradouro: endereco },
      academico: { instituicao, curso, periodo, formatura },
      vaga,
      acesso: { email, senha }
    };

    // Exibe no console do navegador para testes
    console.log("Dados prontos para envio:", dadosCadastro);

    // Sucesso!
    exibirMensagem("Cadastro realizado com sucesso!", "success");

    // Limpa o formulário após o sucesso
    form.reset();
  });

  // --- FUNÇÃO AUXILIAR PARA EXIBIR MENSAGENS ---
  function exibirMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = ""; // Limpa classes anteriores

    if (tipo === "success") {
      mensagem.style.color = "green";
      mensagem.style.fontWeight = "bold";
    } else if (tipo === "error") {
      mensagem.style.color = "red";
      mensagem.style.fontWeight = "bold";
    }
  }
});