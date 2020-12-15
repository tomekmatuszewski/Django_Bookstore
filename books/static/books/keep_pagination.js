$(function() {
    if (localStorage.getItem('pagination')) {
        $("#pagination option").eq(localStorage.getItem('pagination')).prop('selected', true);
    }

    $("#pagination").on('change', function() {
        localStorage.setItem('pagination', $('option:selected', this).index());
    });
});


