document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('.tabs .tab');
  
    tabs.forEach(tab => {
      tab.addEventListener('click', function(event) {
        event.preventDefault(); // Impede a ação padrão do link
  
        // Oculta todos os conteúdos das abas e remove a classe 'active' das abas
        document.querySelectorAll('.tab-content').forEach(tabContent => {
          tabContent.classList.remove('active');
        });
        document.querySelectorAll('.tab').forEach(tab => {
          tab.classList.remove('active');
        });
  
        // Exibe o conteúdo da aba selecionada e adiciona a classe 'active' à aba
        const tabName = this.getAttribute('data-tab');
        document.getElementById(tabName).classList.add('active');
        this.classList.add('active');
      });
    });
  });