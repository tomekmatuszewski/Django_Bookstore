function grabSelect() {
    const pagination = document.getElementById('pagination').value;
    const authorVal = document.getElementById('author').value;
    const genreVal = document.getElementById('genre').value;

    const buttonsPagination = document.querySelectorAll('.buttons-paginate a');

    for (let i=0; i < buttonsPagination.length; i++) {

        buttonsPagination[i].href += `&paginate_by=${pagination}&author=${authorVal}&genre=${genreVal}`

    }

}

const buttonsPagination = document.querySelectorAll('.buttons-paginate a');

for (let i=0; i < buttonsPagination.length; i++) {

        buttonsPagination[i].addEventListener('click', grabSelect)

    }

