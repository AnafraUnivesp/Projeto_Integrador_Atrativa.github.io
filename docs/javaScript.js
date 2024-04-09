document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.tabsMain .tab'); // Corrigindo a seleção dos elementos .tab

  tabs.forEach(tab => { // Corrigindo para 'tabs.forEach'
    tab.addEventListener('click', function(event) {
      event.preventDefault(); // Impede a ação padrão

      // Oculta todos os conteúdos das abas
      document.querySelectorAll('.tab-content').forEach(tabContent => {
        tabContent.classList.remove('active');
      });

      // Exibe o conteúdo da aba selecionada
      const tabName = this.getAttribute('data-tab');
      document.getElementById(tabName).classList.add('active');
    });
  });
});