
document.addEventListener('DOMContentLoaded', function(){
  const search = document.getElementById('plus_box');
  const add = document.getElementById('add_section');
  var input = document.querySelector("input[name='search_s']");
      search.addEventListener('click', function(){
        if (add.style.display === 'none'){
          const inputRect = input.getBoundingClientRect();
          const offset = 557; // Adjust this offset value as needed
          const top = inputRect.top + input.offsetHeight + window.scrollY + 66;
          const left = inputRect.left - add.offsetWidth - offset;

          add.style.top = top + "px";
          add.style.left = left + "px";
          add.style.display = 'block';
      } else {
          add.style.display = 'none';
      }
      });

        
        const add_button = document.getElementById('button_add');
        const questionsSection = document.getElementById('questions_section');
        let questionCounter = 0;
        add_button.addEventListener('click', function(event){
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

      function search() {
          // Clear previous results
          document.getElementById("results").innerHTML = "";
        
          // Get the keyword entered by the user
          var keyword = document.getElementById("searchInput").value;
        
          // Create a new XMLHttpRequest object
          var xhr = new XMLHttpRequest();
        
          // Define the request URL
          var url = "/survey?keyword=" + encodeURIComponent(keyword);
        
          // Open a GET request to the server
          xhr.open("GET", url, true);
        
          // Define the callback function when the request completes
          xhr.onreadystatechange = function() {
            console.log(xhr.responseText);
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
              // Parse the response as JSON
              var results = JSON.parse(xhr.responseText);
              
              // Display the results
              displayResults(results);
            }
          };
        
          // Send the request
          xhr.send();
        }
        
        function displayResults(results) {
          var container = document.getElementById("results");
        
          // Iterate over the results and create HTML elements to display them
          for (var i = 0; i < results.length; i++) {
            var item = results[i];
        
            var resultElement = document.createElement("div");
            resultElement.textContent = item.title;
        
            container.appendChild(resultElement);
          }
        }
