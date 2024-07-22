let spnext = document.querySelector('.spnext')
let spprev = document.querySelector('.spprev')

spnext.addEventListener('click', function(){
    let items = document.querySelectorAll('.spitem')
    document.querySelector('.spslide').appendChild(items[0])
})

spprev.addEventListener('click', function(){
    let items = document.querySelectorAll('.spitem')
    document.querySelector('.spslide').prepend(items[items.length - 1]) // here the length of items = 6
})