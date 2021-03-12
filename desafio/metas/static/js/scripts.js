$(document).ready(function() {

    baseUrl = 'http://127.0.0.1:8000';
    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var filter = $('#filter');
    var filterS = $('#filterS');
    var urlSetor = $('#url-setor').val();
    var urlCor = $('#url-cor').val();

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

    $(filterS).change(function(){
        var filter = $(this).val();
        window.location.href = baseUrl + urlSetor + '?filter=' + filter;
    });

    var formPorcentagem = $('#formulario-porcentagem');

    $(formPorcentagem).submit(function(){
        
        var porcentagem = $('#input-porcentagem');
        var idMeta = $('#id-meta').val();
        $(formPorcentagem).attr('action', baseUrl + '/comentario/' + idMeta + '/' + porcentagem.val());
        
    });

    $(".back-to-top").click(function() {
        $("html, body").animate({scrollTop: 0}, 800);
    });

});