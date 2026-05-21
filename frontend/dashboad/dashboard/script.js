// Aguarda o DOM carregar completamente
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("recuperarForm");
  const mensagem = document.getElementById("mensagem");

  if (form) {
    form.addEventListener("submit", function (event) {
      // Evita o recarregamento padrão da página
      event.preventDefault();

      const emailInput = document.getElementById("email");
      const email = emailInput.value.trim();

      // Configuração visual de feedback (opcional)
      mensagem.style.color = "#555";
      mensagem.textContent = "Processando...";

      // Simulando uma requisição de envio (substitua pelo seu fetch/axios real depois)
      setTimeout(() => {
        if (email) {
          // Feedback de sucesso
          mensagem.style.color = "green";
          mensagem.textContent = `As instruções foram enviadas para: ${email}`;
          
          // Limpa o campo de input
          form.reset();
        } else {
          // Feedback de erro caso algo falhe
          mensagem.style.color = "red";
          mensagem.textContent = "Por favor, insira um e-mail válido.";
        }
      }, 1500); // Simula 1.5 segundos de espera do servidor
    });
  }
});