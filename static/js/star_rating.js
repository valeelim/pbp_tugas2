document.querySelectorAll('.rating').forEach(rating => {
    let howmany = rating.innerHTML
    rating.innerHTML = ''
    for (let i = 0; i < 5; i++) {
        const star = document.createElement('span')
        star.classList.add('fa', 'fa-star')
        if (i < howmany) star.classList.add('checked')
        rating.appendChild(star)
    }
})

document.querySelectorAll('.watched').forEach(watched => {
    let watch = watched.innerHTML
    watched.innerHTML = ''
    watched.classList.add('fa', watch === 'True' ? 'fa-check' : 'fa-close')
})