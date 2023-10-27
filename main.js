let btn = document.getElementsByClassName("btn");

function copyText() {

    let pElements = document.querySelectorAll(".result");

    // كرر كل عنصر p
    for (let i = 0; i < pElements.length; i++) {
      // احصل على النص الموجود داخل العنصر p
      let text = pElements[i].textContent;
  
      // انسخ النص إلى الحافظة
      navigator.clipboard.writeText(text);
    }

    
  }

  window.onscroll = function() {
    scrollFunction();
  };

  function scrollFunction() {
    let toTopBtn = document.getElementById("toTopBtn");
    toTopBtn.style.display = (document.documentElement.scrollTop > 20) ? "block" : "none";
  }

  function scrollToTop() {
    document.documentElement.scrollTop = 0;
  }