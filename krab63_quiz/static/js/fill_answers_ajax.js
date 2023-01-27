// При запросе ответы на вопросы теста убирает имеющиеся отметки и отмечает
// все правльные ответы


$( "#get_answers" ).click(function(event) {
    event.preventDefault();
    $( ':checkbox' ).prop('checked', false);

    var correctAnswers = $.ajax({
        url: url,
        method: 'get',
        dataType: 'json'
    });
    correctAnswers.done( function (data) {
        for ( var i = 0, l = data.length; i <= l-1; i++ ) {
            let correctAnswer = data[i].text;
            $( 'input[value="' + correctAnswer + '"]' ).prop('checked', true);
        };
    });
});