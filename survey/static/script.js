
document.addEventListener('DOMContentLoaded', function(){
  const search = document.getElementById('addButton');
  const add = document.getElementById('add_section');
  const overlay = document.getElementById('overlay')
  var input = document.querySelector("input[name='search_s']");
      search.addEventListener('click', function(){
        if (add.style.display === 'none'){
  
          overlay.style.display = 'block';
          add.style.display = 'block';
      } else {
          add.style.display = 'none';
          overlay.style.display = 'none';
      }
      });

        
        const add_button = document.getElementById('button_add');
        const questionsSection = document.getElementById('questions_section');
        let questionCounter = 0;
        add_button.addEventListener('click', function(event){
            console.log("Hi this workedc")
            event.preventDefault();
            questionCounter++;
            const newDiv = document.createElement('div');
            newDiv.classList.add('container');
        
            

            const label_c = document.createElement('label');
            label_c.innerText = 'Question Type:';
            label_c.style.fontFamily = "Lucida Sans, Lucida Sans Regular, Lucida Grande, Lucida Sans Unicode"
            label_c.style.fontWeight = "bold";
            newDiv.appendChild(label_c);
            const select_c = document.createElement('select');
            select_c.name = "Q_options" + questionCounter +"_question";
            newDiv.appendChild(select_c)

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
            question_label.innerText = 'Question:';
            question_label.style.fontFamily = "Lucida Sans, Lucida Sans Regular, Lucida Grande, Lucida Sans Unicode";
            question_label.style.fontWeight = "bold";
            newDiv2.appendChild(question_label);

            const question_ask = document.createElement('input');
            question_ask.type = 'text';
            question_ask.name = 'S_question' + questionCounter + "_question";
            newDiv2.appendChild(question_ask);
            
        
            questionsSection.appendChild(newDiv);
            questionsSection.appendChild(newDiv2);
            console.log("This worked");
            
            

            

        

            


        });

        

        
});