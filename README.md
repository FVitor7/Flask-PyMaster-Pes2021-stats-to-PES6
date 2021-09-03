# PyMaster (Pes2021 stats to PES6)
<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/fvitor7/pesmaster?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/FVitor7/PesMaster?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/FVitor7/PesMaster?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/FVitor7/PesMaster?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/FVitor7/PesMaster?style=for-the-badge)

<img src="pymaster.jpg" alt="PyMaster">

> Preview do projeto online.

---

## Clone
```bash
git clone https://github.com/FVitor7/PyMaster-Pes2021-stats-to-PES6.git
```

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Extração dos jogadores do Site pesmaster;
- [x] inserir os dados dos jogadores em um banco SQLite;
- [x] Criação da API Rest com o micro-framework Flask;
- [x] Consumir API Rest com Javascript;
- [x] Criação do Frontend com auxilio do bootstrap;
- [ ] Criação de um aplicativo mobile com React Native.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Você instalou a versão mais recente do `<Python3">`
* Você tem uma máquina `<Windows / Linux / Mac>`.
* Você instalou todas as dependências do `"requirements.txt"`.

```
pip install -r requirements.txt
```

## 🚀 Executando o PyMaster (Pes2021 stats to PES6)

Para executar, siga estas etapas:

Linux, macOS & Windows:

Vá até a pasta do projeto e execute o seguinte comando
```
flask add-user -u admin -p 1234  # adiciona usuario admin (executar apenas uma vez)
flask run
```
URL para acessar o projeto no navegador:

```
http://localhost:5000
````

Painel ADMIN: (é possível cadastrar novos usuários e jogadores).

```
http://localhost:5000/admin
````

API:

```
http://localhost:5000/api/v1/
```
Buscando jogadores pelo nome:
```
http://localhost:5000/api/v1/?name=vitor
```
É possível buscar por time e nacionalidade passando os parametros (team e nation).

Obtendo stats dos jogadores através do ID:

```
http://localhost:5000/api/v1/stats/?id=10
```


## ☕ Usando o PyMaster (Pes2021 stats to PES6)

Para usar, siga estas etapas:

```
Você pode pesquisar pelo nome dos jogadores, times e nacionalidade. 
Ao clicar no jogador é exibido as suas habilidades para PES6 e um botão para copiar.

```

## Structure

```bash
.
├── Makefile
├── pymaster  (MAIN PACKAGE)
│   ├── app.py  (APP FACTORIES)
│   ├── blueprints  (BLUEPRINT FACTORIES)
│   │   ├── __init__.py
│   │   ├── restapi  (REST API)
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   └── webui  (FRONT END)
│   │       ├── __init__.py
│   │       ├── templates
│   │       │   ├── index.html
│   │       │   ├── player.html
│   │       │   └── api.html
│   │       └── views.py
│   ├── ext (EXTENSION FACTORIES)
│   │   ├── admin.py
│   │   ├── appearance.py
│   │   ├── auth.py
│   │   ├── commands.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models.py  (DATABASE MODELS)
│   ├── templates  (Login page and ADMIN html)
│   ├── static  (Login page and ADMIN js)
├── README.md
├── requirements.txt
└── settings.toml  (SETTINGS)

```


## 📫 Contribuindo para PyMaster (Pes2021 stats to PES6)
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com PyMaster (Pes2021 stats to PES6), siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/FVitor7">
        <img src="https://avatars2.githubusercontent.com/u/48036134?s=460&u=83e0e7eb1fe80c60164e6c9561a6174874c3b3da&v=4" width="100px;" alt="Foto do Fábio Vitor no GitHub"/><br>
        <sub>
          <b>Fábio Vitor</b>
        </sub>
      </a>
    </td>
    
  </tr>
</table>


## 😄 Seja um dos contribuidores<br>

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#pymaster-pes2021-stats-to-pes6)<br>
