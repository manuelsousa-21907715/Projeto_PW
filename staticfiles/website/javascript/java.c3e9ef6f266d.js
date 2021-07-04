function showPage(page) {
    document.querySelectorAll('div').forEach(div => {
        div.style.display = 'none';
    });
    document.querySelector(`#${page}`).style.display = 'block';
}

var x = 0;
function gray() {
   if (x == 0) {
        var element = document.getElementById("img");
        element.classList.add("gray");
        x = 1;
   } else {
        var element = document.getElementById("img");
        element.classList.remove("gray");
        x = 0;
   }
}

var x2 = 0;
function gray2() {
    if (x2 == 0) {
        var element = document.getElementById("img2");
        element.classList.add("gray");
        x2 = 1;
    } else {
        var element = document.getElementById("img2");
        element.classList.remove("gray");
        x2 = 0;
    }
}

var x3 = 0;
function gray3() {
   if (x3 == 0) {
        var element = document.getElementById("img3");
        element.classList.add("gray");
        x3 = 1;
   } else {
        var element = document.getElementById("img3");
        element.classList.remove("gray");
        x3 = 0;
   }
}


document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.thisButton').onclick = function() {
            showPage(this.dataset.page);
        }
    });

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.thisButton2').onclick = function() {
            showPage(this.dataset.page);
        }
    });

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('.thisButton3').onclick = function() {
            showPage(this.dataset.page);
        }
    });