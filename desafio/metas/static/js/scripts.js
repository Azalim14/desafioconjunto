$(document).ready(function() {

    baseUrl = 'http://abrasel.pythonanywhere.com';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');

    $(deleteBtn).on('click', function(e) {
        e.preventDefault();

        var delLink = $(this).attr('href');
        var result = confirm('Quer mesmo deletar esta meta?');

        if(result){
            window.location.href = delLink;
        }

    });

    $(searchBtn).on('click', function(){
        searchForm.submit();
    });

    $(filter).change(function(){
        var filter = $(this).val();
        window.location.href = baseUrl + '?filter=' + filter;
    });

    var formPorcentagem = $('#formulario-porcentagem');

    $(formPorcentagem).submit(function(){
        
        var porcentagem = $('#input-porcentagem');
        var idMeta = $('#id-meta').val();
        $(formPorcentagem).attr('action', baseUrl + '/comentario/' + idMeta + '/' + porcentagem.val());
        
    });

});