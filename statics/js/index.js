document.getElementById("women-banner").style.backgroundColor = "#f8d7da";
document.getElementById("women-banner").style.marginTop = "10px";
document.getElementById("heading").style.textTransform = 'uppercase';
document.getElementById("women-card").style.backgroundColor = '#cff4fc';
document.getElementById("women-card2").style.backgroundColor = 'goldenrod';

document.getElementById("women-banner").id = "kids-banner";
document.getElementById("kids-card").style.background = "lightskyblue";
document.getElementById("text-bodies").style.textDecoration = "none";
document.getElementById('nav-items').style.marginLeft = "10px";

document.querySelectorAll('.custom-button').forEach(button => {
    button.addEventListener('mouseover', () => {
      button.style.transition = '0.3s';
      button.style.transform = 'translateY(-3px)';
    });
  
    button.addEventListener('mouseout', () => {
      button.style.transform = 'translateY(0)';
    });
  
    button.addEventListener('click', () => {
      button.classList.add('clicked');
      setTimeout(() => button.classList.remove('clicked'), 300);
    });
  });
  