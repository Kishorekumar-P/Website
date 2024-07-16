{%load static%}
document.addEventListener('DOMContentLoaded', function() {
    const images = [
      '{%static 'assets/sliding_image1.png'%}', 
      '{%static 'assets/sliding_image1.png'%}', 
      '{%static 'assets/sliding_image1.png'%}', 
      '{%static 'assets/sliding_image1.png'%}', 
      '{%static 'assets/sliding_image1.png'%}', 
    ];
  
    const gallery = document.getElementById('gallery');
  
    images.forEach(src => {
      const img = document.createElement('img');
      img.src = src;
      img.alt = 'Gallery Image';
      gallery.appendChild(img);
    });
  });
  