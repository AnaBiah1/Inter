    const images = ['imagem1.jpg', 'imagem2.jpg', 'imagem3.jpg'];
    let currentImageIndex = 0;

    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        document.getElementById('carousselImagem').src = images[currentImageIndex];
    }

    const menuIcon = document.getElementById("menu-icon");
const sideMenu = document.getElementById("side-menu");

menuIcon.addEventListener("click", () => {
  if (sideMenu.style.width === "250px") {
    sideMenu.style.width = "0";
  } else {
    sideMenu.style.width = "250px";
  }
});

document.querySelectorAll(".side-menu a").forEach(link => {
  link.addEventListener("click", () => {
    sideMenu.style.width = "0";
  });
});