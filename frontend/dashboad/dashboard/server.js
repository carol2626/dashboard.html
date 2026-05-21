const express = require("express");
const cors = require("cors");
const bcrypt = require("bcrypt");
const { Pool } = require("pg");

const app = express();

// =========================
// ✅ MIDDLEWARE
// =========================
app.use(cors());
app.use(express.json());

// =========================
// ✅ CONEXÃO BANCO
// =========================
const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "postgres",
  password: "nupilta",
  port: 5432,
});

// =========================
// ✅ TESTAR CONEXÃO
// =========================
pool.connect()
  .then(() => {
    console.log("Banco conectado com sucesso ✅");
  })
  .catch((err) => {
    console.log("Erro ao conectar no banco ❌");
    console.log(err);
  });

// =========================
// ✅ CADASTRO
// =========================
app.post("/register", async (req, res) => {

  const {
    nome,
    email,
    senha
  } = req.body;

  if (!nome || !email || !senha) {
    return res.status(400).json({
      mensagem: "Preencha todos os campos ❌"
    });
  }

  try {

    // verifica email
    const usuarioExiste = await pool.query(
      "SELECT * FROM users WHERE email = $1",
      [email]
    );

    if (usuarioExiste.rows.length > 0) {
      return res.status(400).json({
        mensagem: "Email já cadastrado ❌"
      });
    }

    // criptografa senha
    const senhaCriptografada = await bcrypt.hash(senha, 10);

    // salva usuário
    await pool.query(
      "INSERT INTO users (nome, email, senha) VALUES ($1, $2, $3)",
      [nome, email, senhaCriptografada]
    );

    res.status(201).json({
      mensagem: "Cadastro realizado com sucesso ✅"
    });

  } catch (erro) {

    console.log("ERRO REGISTER:");
    console.log(erro);

    res.status(500).json({
      mensagem: "Erro no servidor ❌"
    });
  }

});

// =========================
// ✅ LOGIN
// =========================
app.post("/login", async (req, res) => {

  const { email, senha } = req.body;

  if (!email || !senha) {
    return res.status(400).json({
      mensagem: "Preencha email e senha ❌"
    });
  }

  try {

    const result = await pool.query(
      "SELECT * FROM users WHERE email = $1",
      [email]
    );

    if (result.rows.length === 0) {
      return res.status(400).json({
        mensagem: "Email ou senha inválidos ❌"
      });
    }

    const usuario = result.rows[0];

    const senhaCorreta = await bcrypt.compare(
      senha,
      usuario.senha
    );

    if (!senhaCorreta) {
      return res.status(400).json({
        mensagem: "Senha inválida ❌"
      });
    }

    res.status(200).json({
      mensagem: "Login realizado com sucesso 🚀",
      usuario: usuario.nome
    });

  } catch (erro) {

    console.log("ERRO LOGIN:");
    console.log(erro);

    res.status(500).json({
      mensagem: "Erro no servidor ❌"
    });
  }

});

// =========================
// ✅ CRIAR VAGA
// =========================
app.post("/vaga", async (req, res) => {

  const {
    empresa,
    cargo,
    status,
    data_entrevista,
    usuario_email
  } = req.body;

  try {

    await pool.query(
      `
      INSERT INTO vagas
      (
        empresa,
        cargo,
        status,
        data_entrevista,
        usuario_email
      )
      VALUES ($1, $2, $3, $4, $5)
      `,
      [
        empresa,
        cargo,
        status,
        data_entrevista,
        usuario_email
      ]
    );

    res.status(201).json({
      mensagem: "Vaga cadastrada com sucesso ✅"
    });

  } catch (erro) {

    console.log("ERRO VAGA:");
    console.log(erro);

    res.status(500).json({
      mensagem: "Erro ao cadastrar vaga ❌"
    });
  }

});

// =========================
// ✅ LISTAR VAGAS
// =========================
app.get("/vagas/:email", async (req, res) => {

  const email = req.params.email;

  try {

    const result = await pool.query(
      `
      SELECT * FROM vagas
      WHERE usuario_email = $1
      ORDER BY id DESC
      `,
      [email]
    );

    res.json(result.rows);

  } catch (erro) {

    console.log("ERRO LISTAR VAGAS:");
    console.log(erro);

    res.status(500).json({
      mensagem: "Erro ao buscar vagas ❌"
    });
  }

});

// =========================
// ✅ DELETAR VAGA
// =========================
app.delete("/vaga/:id", async (req, res) => {

  const id = req.params.id;

  try {

    await pool.query(
      "DELETE FROM vagas WHERE id = $1",
      [id]
    );

    res.json({
      mensagem: "Vaga removida com sucesso 🗑️"
    });

  } catch (erro) {

    console.log("ERRO DELETE:");
    console.log(erro);

    res.status(500).json({
      mensagem: "Erro ao deletar vaga ❌"
    });
  }

});

// =========================
// ✅ ATUALIZAR STATUS
// =========================
app.put("/vaga/:id", async (req, res) => {

  const id = req.params.id;

  const { status } = req.body;

  try {

    await pool.query(
      `
      UPDATE vagas
      SET status = $1
      WHERE id = $2
      `,
      [status, id]
    );

    res.json({
      mensagem: "Status atualizado ✅"
    });

  } catch (erro) {

    console.log("ERRO UPDATE:");
    console.log(erro);

    res.status(500).json({
      mensagem: "Erro ao atualizar status ❌"
    });
  }

});

// =========================
// ✅ SERVIDOR
// =========================
app.listen(3000, () => {
  console.log("Servidor rodando na porta 3000 🚀");
});