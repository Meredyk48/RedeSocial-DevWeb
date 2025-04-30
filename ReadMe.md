# Como usar o Quasar Framework neste projeto (via CDN)

Este documento explica como o Quasar Framework foi adicionado ao seu arquivo `index.html` e como você pode continuar utilizando seus componentes.

## 1. Configuração via CDN

Para utilizar o Quasar sem um processo de build complexo (como o Quasar CLI), adicionamos as referências necessárias diretamente no arquivo `/rede_social/templates/pages/index.html` através de uma CDN (Content Delivery Network).

- **No `<head>`:**
    - Adicionamos os links para as fontes `Roboto` e `Material Icons`, que são comumente usadas com Quasar.
    - Adicionamos o link para o arquivo CSS principal do Quasar (`quasar.prod.css`).

  ```html
  <head>
      ...
      <!-- Quasar CDN Links -->
      <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900|Material+Icons" rel="stylesheet" type="text/css">
      <link href="https://cdn.jsdelivr.net/npm/quasar@2.18.1/dist/quasar.prod.css" rel="stylesheet" type="text/css">
      ...
  </head>
  ```

- **No final do `<body>`:**
    - Adicionamos o script do `Vue.js` (versão 3), que é a base do Quasar.
    - Adicionamos o script principal do Quasar (`quasar.umd.prod.js`).
    - Incluímos um script para inicializar o Vue.js e registrar o Quasar.

  ```html
  <body>
      <div id="q-app">
          <!-- Todo o conteúdo da sua página que usa Quasar vai aqui dentro -->
          ...
      </div>

      <!-- Vue.js e Quasar JS CDN -->
      <script src="https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.prod.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/quasar@2.18.1/dist/quasar.umd.prod.js"></script>

      <!-- Inicialização do Vue e Quasar -->
      <script>
          const { createApp, ref } = Vue

          const app = createApp({
              setup() {
                  // Variáveis e funções reativas do Vue (ex: controle do drawer)
                  const leftDrawerOpen = ref(false)
                  return {
                      leftDrawerOpen,
                      toggleLeftDrawer() {
                          leftDrawerOpen.value = !leftDrawerOpen.value
                      }
                  }
              }
          })

          app.use(Quasar) // Registra todos os componentes e diretivas Quasar
          app.mount(\'#q-app\') // Monta a aplicação Vue no elemento com id="q-app"
      </script>
  </body>
  ```

## 2. Estrutura HTML com Quasar

O conteúdo principal da sua página foi envolvido por um `div` com `id="q-app"`. Dentro dele, utilizamos componentes Quasar para estruturar a interface:

- **`<q-layout>`:** Componente principal que define a estrutura da página (header, drawer, page container).
- **`<q-header>`, `<q-toolbar>`, `<q-btn>`:** Usados para criar a barra de navegação superior.
- **`<q-drawer>`:** Usado para criar o painel lateral (lista de amigos).
- **`<q-page-container>`, `<q-page>`:** Contêiner para o conteúdo principal da página.
- **`<q-card>`, `<q-item>`, `<q-avatar>`, `<q-input>`, etc.:** Componentes usados para exibir as postagens, a área de adicionar postagem e a lista de amigos.

**Importante:** Ao usar a versão UMD/CDN, **não utilize tags de fechamento automático** (como `<q-btn ... />`). Sempre use a tag de abertura e fechamento completa (ex: `<q-btn ...></q-btn>`).

## 3. Integração com Django Templates

Os componentes Quasar foram integrados com as tags de template do Django que você já utilizava. Por exemplo, o loop para exibir as postagens continua funcionando:

```html
<!-- Lista de Postagens (Renderizada pelo Django dentro de componentes Quasar) -->
{% for post in posts %}
<q-card class="my-card">
    <q-item>
        <q-item-section avatar>
            <q-avatar>
                <img src="https://cdn.quasar.dev/img/boy-avatar.png">
            </q-avatar>
        </q-item-section>
        <q-item-section>
            <q-item-label>{{ post.user }}</q-item-label>
            <q-item-label caption>{{ post.created_at|date:'d/m/Y H:i' }}</q-item-label>
        </q-item-section>
    </q-item>
    <q-card-section>
        <div>{{ post.content }}</div>
    </q-card-section>
    <q-separator />
    <q-card-actions align="around">
        <q-btn flat round color="primary" icon="thumb_up"></q-btn>
        <q-btn flat round color="primary" icon="comment"></q-btn>
        <q-btn flat round color="primary" icon="share"></q-btn>
    </q-card-actions>
</q-card>
{% empty %}
<p>Nenhuma postagem ainda.</p>
{% endfor %}
```

Você pode continuar passando dados do seu backend Django para o template e usando as tags `{{ variable }}` dentro dos componentes Quasar.

## 4. Próximos Passos

- **Consultar a Documentação:** Para adicionar mais componentes ou funcionalidades, consulte a [documentação oficial do Quasar](https://quasar.dev/vue-components).
- **Adicionar Interatividade:** Para funcionalidades mais complexas (como adicionar posts dinamicamente sem recarregar a página, carregar amigos via API, etc.), você precisará escrever mais código JavaScript/Vue dentro do bloco `<script>` de inicialização ou em arquivos JS separados.
- **Estilização:** Você pode adicionar seus próprios estilos CSS no bloco `<style>` dentro do `<head>` ou em arquivos CSS separados.

Esta configuração via CDN é uma forma rápida de começar a usar Quasar, mas para projetos maiores, o uso do Quasar CLI é geralmente recomendado por oferecer mais recursos e otimizações.

