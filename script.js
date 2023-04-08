// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});


/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

  // const aboutSection = document.querySelector("#about");
  // const aboutObserver = new IntersectionObserver(entries => {
  //   entries.forEach(entry => {
  //     if (entry.isIntersecting) {
  //       aboutSection.classList.add("visible");
  //     } else {
  //       aboutSection.classList.remove("visible");
  //     }
  //   });
  // });
  // aboutObserver.observe(aboutSection);

  var navLinks = document.querySelectorAll(".nav-link");
  var sections = document.querySelectorAll("section");

  function highlightNavLink() {
    var index = sections.length;

    while (--index && window.scrollY + 50 < sections[index].offsetTop) {}

    navLinks.forEach((link) => link.classList.remove("active"));
    navLinks[index].classList.add("active");
  }

  highlightNavLink();

  window.addEventListener("scroll", highlightNavLink);

// Get all the faq-question elements
const questions = document.querySelectorAll(".faq-question");

// Add a click event listener to each question
questions.forEach(function(question) {
  question.addEventListener("click", function() {
    // Get the corresponding faq-answer element
    const answer = question.nextElementSibling;

    // Check if the answer is currently visible
    if (answer.style.display === "block") {
      // If it is, hide the answer and change the icon to plus
      answer.style.display = "none";
      question.classList.remove("active");
      question.querySelector(".faq-icon").textContent = "+";
    } else {
      // If it isn't, hide any other visible answers and change their icons to plus
      const visibleAnswer = document.querySelector(".faq-answer[style='display: block;']");
      if (visibleAnswer) {
        visibleAnswer.style.display = "none";
        visibleAnswer.previousElementSibling.classList.remove("active");
        visibleAnswer.previousElementSibling.querySelector(".faq-icon").textContent = "+";
      }
      // And show the answer for the clicked question and change the icon to minus
      answer.style.display = "block";
      question.classList.add("active");
      question.querySelector(".faq-icon").textContent = "-";
    }
  });
});


  
  
  
