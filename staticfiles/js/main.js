// On scroll Add Class
$(window).scroll(function(){
    if ($(this).scrollTop() > 300) {
       $('.headerss').addClass('sticky');
    } else {
       $('.headerss').removeClass('sticky');
    }
   });
  
  
  document.addEventListener("DOMContentLoaded", function(){
      document.querySelectorAll('.sidenav .nav-link').forEach(function(element){
        
        element.addEventListener('click', function (e) {
    
          let nextEl = element.nextElementSibling;
          let parentEl  = element.parentElement;	
    
            if(nextEl) {
                e.preventDefault();	
                let mycollapse = new bootstrap.Collapse(nextEl);
                
                if(nextEl.classList.contains('show')){
                  mycollapse.hide();
                } else {
                    mycollapse.show();
                    // find other submenus with class=show
                    var opened_submenu = parentEl.parentElement.querySelector('.sub-menu.show');
                    // if it exists, then close all of them
                    if(opened_submenu){
                      new bootstrap.Collapse(opened_submenu);
                    }
                }
            }
        }); // addEventListener
      }) // forEach
    });
    
  
  
    document.addEventListener("DOMContentLoaded", function (event) {
      const showNavbar = (toggleId, navId, bodyId, headerId) => {
        const toggle = document.getElementById(toggleId),
          nav = document.getElementById(navId),
          bodypd = document.getElementById(bodyId),
          headerpd = document.getElementById(headerId);
  
        // Validate that all variables exist
        if (toggle && nav && bodypd && headerpd) {
          toggle.addEventListener("click", () => {
            // show navbar
            nav.classList.toggle("show");
            // change icon
            toggle.classList.toggle("bx-x");
            // add padding to body
            bodypd.classList.toggle("body-pd");
            // add padding to header
            headerpd.classList.toggle("body-pd");
          });
        }
      };
  
      showNavbar("header-toggle", "nav-bar", "body-pd", "header");
  
      /*===== LINK ACTIVE =====*/
      const linkColor = document.querySelectorAll(".nav_link");
  
      function colorLink() {
        if (linkColor) {
          linkColor.forEach((l) => l.classList.remove("active"));
          this.classList.add("active");
        }
      }
      linkColor.forEach((l) => l.addEventListener("click", colorLink));
  
      // Your code to run since DOM is loaded and ready
    });
  
  // date pickar js
  
    $(function() {
      $( ".calendar" ).datepicker({
        dateFormat: 'dd/mm/yy',
        firstDay: 1
      });
      
      $(".calendar").on("change",function(){
        var $me = $(this),
            $selected = $me.val(),
            $parent = $me.parents('.date-picker');
        $parent.find('.result').children('span').html($selected);
      });
    });
  
    