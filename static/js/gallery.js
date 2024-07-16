document.addEventListener('DOMContentLoaded', function() {
    const images = [
      '{%%}', // Replace with the actual image paths
      'image2.jpg',
      'image3.jpg',
      'image4.jpg',
      'image5.jpg'
    ];
  
    const gallery = document.getElementById('gallery');
  
    images.forEach(src => {
      const img = document.createElement('img');
      img.src = src;
      img.alt = 'Gallery Image';
      gallery.appendChild(img);
    });
  });
  