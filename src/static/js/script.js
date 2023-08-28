$(document).ready(function() {
    $('.tecla').click(function() {
        var tecla = $(this).text(); // Obtém o texto da tecla clicada
        var clickedTecla = $(this); // Armazena a tecla clicada para uso posterior

        $.get('/escolher', { tecla: tecla }, function(data) {
            $('#message').text(data.message[0]); // Exibe somente o valor da tecla

            if (data.message[1] === "acertou") {
                clickedTecla.toggleClass('acertou'); // Alterna a classe na tecla clicada
                clickedTecla.prop('disabled', true); // Desabilita o botão clicado

            } else if (data.message[1] === "errou") {
                clickedTecla.toggleClass('errou'); // Alterna a classe na tecla clicada
                clickedTecla.prop('disabled', true); // Desabilita o botão clicado
            }

            if (data.message[2] === "ganhou") {
                Swal.fire({
                    title: 'Parabéns!',
                    html: '<h3 style="color:green;">Você ganhou!</h3>A palavra era: <h4>' + data.message[4] + '</h4>',
                    icon: 'success',
                    confirmButtonText: 'Jogar Novamente',
                    allowOutsideClick: false,
                    
                }).then((result) => {
                    if (result.isConfirmed) {
                        location.reload(); // Recarrega a página
                    }
                });
            }

            if (data.message[2] === "perdeu") {
                Swal.fire({
                    title: 'Ops!',
                    html: '<h3 style="color:red;">Você perdeu!</h3>A palavra era: <h4>' + data.message[4] + '</h4>',
                    icon: 'error',
                    confirmButtonText: 'Tentar Novamente',
                    allowOutsideClick: false
                    
                }).then((result) => {
                    if (result.isConfirmed) {
                        location.reload(); // Recarrega a página
                    }
                });
            }

        });
    });
});
