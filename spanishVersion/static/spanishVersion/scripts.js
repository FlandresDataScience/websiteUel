$(document).ready(function() { 

    // Quantidade de cursos oferecidos
    let containerA = document.getElementById("circleA");

    let circleA = new ProgressBar.Circle(containerA, {

        color: '#008000',
        strokeWidth: 8,
        duration: 1400,
        from: {color: '#AAA'},
        to: { color: '#008000' },

        step: function(state, circle){

            circle.path.setAttribute('stroke', state.color)

            let value = Math.round(circle.value() * 52);

            circle.setText(value);

        }

    });

    let containerB = document.getElementById("circleB");

    let circleB = new ProgressBar.Circle(containerB, {

        color: '#008000',
        strokeWidth: 8,
        duration: 1600,
        from: {color: '#AAA'},
        to: { color: '#008000' },

        step: function(state, circle){

            circle.path.setAttribute('stroke', state.color)

            let value = Math.round(circle.value() * 75);

            circle.setText(value);

        }

    });

    let containerC = document.getElementById("circleC");

    let circleC = new ProgressBar.Circle(containerC, {

        color: '#008000',
        strokeWidth: 8,
        duration: 1800,
        from: {color: '#AAA'},
        to: { color: '#008000' },

        step: function(state, circle){

            circle.path.setAttribute('stroke', state.color)

            let value = Math.round(circle.value() * 48);

            circle.setText(value);

        }

    });

    let containerD = document.getElementById("circleD");

    let circleD = new ProgressBar.Circle(containerD, {

        color: '#008000',
        strokeWidth: 8,
        duration: 2100,
        from: {color: '#AAA'},
        to: { color: '#008000' },

        step: function(state, circle){

            circle.path.setAttribute('stroke', state.color)

            let value = Math.round(circle.value() * 33);

            circle.setText(value);

        }

    });

    // Iniciando o loader dos cursos quando o usuario chega no elemento da pagina
    let dataAreaOffset = $('#data-area').offset();
    let stop = 0;

    $(window).scroll(function(e) {

        let scroll = $(window).scrollTop();

        if(scroll > (dataAreaOffset.top - 500) && stop == 0) {

            circleA.animate(1.0);
            circleB.animate(1.0);
            circleC.animate(1.0);
            circleD.animate(1.0);

            stop = 1;
             
        }

    });

    //Parallax  (impressão de um ambiente 3D em uma tela 2D)
    setTimeout(function(){

        $('#data-area').parallax({imageSrc: 'img/recepcao.jpg'});
        $('#apply-area').parallax({imageSrc: 'img/Lousa.jpg'});
    }, 100);

    
});