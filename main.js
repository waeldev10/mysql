
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


  document.querySelectorAll('.copy').forEach(function(button) {
    button.addEventListener('click', function(event) {
      let index = Array.from(document.querySelectorAll('.copy')).indexOf(button);
      let text = document.querySelectorAll('.result')[index].innerText;
      let elem = document.createElement('textarea');
      document.body.appendChild(elem);
      elem.value = text;
      elem.select();
      document.execCommand('copy');
      document.body.removeChild(elem);
      alert("تم النسخ بنجاح")
    });
  });

