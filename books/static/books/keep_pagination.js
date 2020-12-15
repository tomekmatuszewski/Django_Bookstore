$(function() {
    if (localStorage.getItem('pagination')) {
        $("#pagination option").eq(localStorage.getItem('pagination')).prop('selected', true);
    }
    if (localStorage.getItem('author')) {
        $("#author option").eq(localStorage.getItem('author')).prop('selected', true);
    }

    if (localStorage.getItem('genre')) {
        $("#genre option").eq(localStorage.getItem('genre')).prop('selected', true);
    }

    $("#pagination").on('change', function() {
        localStorage.setItem('pagination', $('option:selected', this).index());
    });

    $("#author").on('change', function() {
        localStorage.setItem('author', $('option:selected', this).index());
    });

    $("#genre").on('change', function() {
        localStorage.setItem('genre', $('option:selected', this).index());
    });
});


