
document.addEventListener('DOMContentLoaded', function(){
        const search = document.getElementById('plus_box');
        const add = document.getElementById('add_section');
        search.addEventListener('click', function(){
            if (add.style.display === 'none'){
                add.style.display = 'block';
            } else {
                add.style.display = 'none';
        }})

        
        const add_button = document.getElementById('button_add');
      
        add_button.addEventListener('click', function(){

        const main_div = document.getElementById('add_section');
        const newDiv = document.createElement('div');
        newDiv.classList.add('container');
       
        

        const label_c = document.createElement('label');
        label_c.innerText = 'Question Type:';
        newDiv.appendChild(label_c);
        
        const select_c = document.createElement('select');
        

        const option_c = document.createElement('option');
        option_c.value = 'scale';
        option_c.innerText = '1-10 scale';
        select_c.appendChild(option_c)

        const option_c1 = document.createElement('option');
        option_c1.value = 'own';
        option_c1.innerText = 'Own Answer';
        select_c.appendChild(option_c1)

        const option_c2 = document.createElement('option');
        option_c2.value = 'yes_no_mabye';
        option_c2.innerText = 'Yes/No/Mabye';
        select_c.appendChild(option_c2);

        const newDiv2 = document.createElement('div');
        newDiv2.classList.add('container');

        const question_label = document.createElement('label');
        question_label.innerText = 'Question:'
        question_label.classList.add('S_q')
        newDiv2.appendChild(question_label);

        const question_ask = document.createElement('input');
        question_ask.type = 'text';
        question_ask.name = 'S_question';
        question_ask.id = 'S_question';
        newDiv2.appendChild(question_ask);
        
        newDiv.appendChild(select_c);
        main_div.appendChild(newDiv);
        main_div.appendChild(newDiv2);
        console.log("This worked");


        



        


    });
});
