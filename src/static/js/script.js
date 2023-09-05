$(document).ready(function () {
    // Quando o valor do select mudar, submeta automaticamente o formulário
    $("#opcao").change(function () {
        $("#meuFormulario").submit();
    });

    // Obtém o valor da opção selecionada do Flask (substitua 'opcaoSelecionada' pelo valor real)
    var opcaoSelecionada = $("#opcao").data("opcao");
    console.log(opcaoSelecionada);

    // Define a opção selecionada com base no valor recebido do Flask
    $("#opcao").val(opcaoSelecionada);

    // Se a opção selecionada for 'Aleatorio', exiba o elemento com a classe 'elemento'
    if (opcaoSelecionada === 'Aleatorio') {
        $("#dica").css("display", "block");
    }

    // Função para lidar com o clique nas teclas
    $('.tecla').click(function () {
        var tecla = $(this).text();
        var clickedTecla = $(this);

        $.get('/escolher', { tecla: tecla }, function (data) {
            $('#message').text(data.message[0]);

            if (data.message[1] === "acertou" || data.message[1] === "errou") {
                clickedTecla.toggleClass('acertou', data.message[1] === "acertou")
                    .toggleClass('errou', data.message[1] === "errou");
                clickedTecla.prop('disabled', true);
            }

            if (data.message[2] === "ganhou" || data.message[2] === "perdeu") {
                var title = data.message[2] === "ganhou" ? 'Parabéns!' : 'Ops!';
                var color = data.message[2] === "ganhou" ? 'green' : 'red';

                Swal.fire({
                    title: title,
                    html: `<h3 style="color:${color};">${title}</h3>A palavra era: <h4>${data.message[3]}</h4>`,
                    icon: data.message[2] === "ganhou" ? 'success' : 'error',
                    confirmButtonText: data.message[2] === "ganhou" ? 'Jogar Novamente' : 'Tentar Novamente',
                    allowOutsideClick: false,
                }).then((result) => {
                    if (result.isConfirmed) {
                        location.reload();
                    }
                });
            }

            // Quando você obtém o valor de 'erros' do servidor Flask, armazene-o em uma variável JavaScript
            var erros = data.message[4]
            console.log(erros)
            // Certifique-se de que 'erros' seja um número válido
            if (isNaN(erros)) {
                erros = '0'; // Ou defina o valor padrão desejado
            }
            console.log(erros)
            // Construa a URL da imagem com base no valor de 'erros' e atualize o atributo 'src' da imagem
            var nomeImagem = erros + ".png";
            var urlImagem = "/static/image/" + nomeImagem;
            console.log(urlImagem)
            $("#imagemErro").attr("src", urlImagem);
        });
    });
});
