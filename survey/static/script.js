
document.addEventListener('DOMContentLoaded', function(){
        const search = document.getElementById('plus_box');
        const add = document.getElementById('add_section')
        search.addEventListener('click', function(){
            if (add.style.display === 'none'){
                add.style.display = 'block';
            } else {;
                add.style.display = 'none';
            }

        });
});