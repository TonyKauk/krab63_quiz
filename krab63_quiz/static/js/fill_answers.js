// При запросе ответы на вопросы теста убирает имеющиеся отметки и отмечает
// все правльные ответы


$(document).ready( function () {
    $( ':checkbox' ).prop('checked', false);
    $( 'input[value="' + answers[0] + '"]' ).prop('checked', true);

    for ( var i = 0, l = answers.length; i <= l-1; i++ ) {
        let correctAnswer = answers[i];
        $( 'input[value="' + correctAnswer + '"]' ).prop('checked', true);
    };
});