
// Seleciona o elemento da div
const divMensagens = document.querySelector('.contMsg');

// Define a função para remover a div após 5 segundos
const removerDiv = () => {
    divMensagens.remove();
}

// Define o atraso de 5 segundos e chama a função de remover a div
setTimeout(removerDiv, 5000);

