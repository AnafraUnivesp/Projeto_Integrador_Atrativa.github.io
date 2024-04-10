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

document.getElementById('btInserir').addEventListener('click', function() {
  // Área onde os resultados serão exibidos
  const resultados = document.getElementById('resultados');
  resultados.innerHTML = ''; // Limpa resultados anteriores
  
  // Recupera os valores dos inputs
  const inputs = [
    document.getElementById('inputCodigo'),
    document.getElementById('inputLote'),
    document.getElementById('inputDescricao'),
    document.getElementById('inCor'),
    document.getElementById('inTamanho'),
    document.getElementById('inpuQuantidade'), // Corrija o typo para 'inputQuantidade' no seu HTML e aqui
    document.getElementById('inputValor'),
    document.getElementById('inCategoria'),
    document.getElementById('inputDataEnt')
  ];

  // Para cada input, cria uma nova div, define seu conteúdo e anexa ao div de resultados
  inputs.forEach(input => {
    const div = document.createElement('div');
    div.textContent = input.value; // Usa textContent para evitar riscos de XSS
    resultados.appendChild(div);
  });
});
