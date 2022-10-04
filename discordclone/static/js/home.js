const buttons = document.querySelectorAll('.btn--nav')
const errDisplay = document.querySelector('.err--nav')
const friendsDisplay = document.querySelector('#friends--display')
const search = document.querySelector('#search')

const updateErr = (mode, errMessage) => {
    if (mode === 'show') {
        errDisplay.style.display = 'block'
        errDisplay.textContent = errMessage

    }
    else if (mode === 'hide') {
        errDisplay.style.display = 'none'
    }
}

search.addEventListener('keypress', async e => {
    friendsDisplay.innerHTML = ''
    q = e.currentTarget.value
    let loading = true
    try {
        response = await fetch(`${searchUrl}?q=${q}`)

        if (!response.ok ) {
            throw new Error('Error trying to fetch data...')
        }
        updateErr('hide') // Hides the error message incase there is any.
        data = await response.json()

        if (data.length == 0) { // If there is no data.
            let itemContainer = document.createElement('p')
            itemContainer.classList.add('friends--empty')
            itemContainer.textContent = 'This tab is currently empty!'
            friendsDisplay.appendChild(itemContainer)
        }
        else {
            data.forEach(item => { 
                let itemContainer = document.createElement('p')
                itemContainer.classList.add('friends--item')
                itemContainer.textContent = `${item.username}#${item.tag}`
                friendsDisplay.appendChild(itemContainer)
            })
        }
    }
    catch (err) {
        friendsDisplay.innerHTML = '' // Clears the display content to avoid confusion.
        updateErr('show', err.message)
        console.error(err)
    }
    console.log(q)
})

document.addEventListener('DOMContentLoaded', () => {
    updateErr('hide');
    fetchData('friends'); // To show the friends tab upon page load.
    updateBtn('friends');
})

buttons.forEach(btn => {
    btn.addEventListener('click', async () => {
        mode = event.currentTarget.dataset.id
        fetchData(mode)
        updateBtn(mode)
    });
})

// Updates the active btn by adding a background to it and removing it from the rest of the buttons.
const updateBtn = (mode) => {
    buttons.forEach(btn => {
        if (btn.dataset.id === mode) {
            if (mode == 'add-friends') {
                btn.classList.remove('bg-teal-800');
                btn.classList.add('text-teal-500');
            }
            else {
                btn.classList.add('bg-neutral-900');
            }
        }
        else {
            if (btn.dataset.id == 'add-friends') {
                btn.classList.add('bg-teal-800', 'text-white');
                btn.classList.remove('text-teal-500');
            }
            else {
                btn.classList.remove('bg-neutral-900');
            }
            
        }
    })
}

const fetchData = async (mode) => {
        try {
            response = await fetch(`${fetchUrl}?mode=${mode}`)

            if (!response.ok ) {
                throw new Error('Error trying to fetch data...')
            }
            updateErr('hide') // Hides the error message incase there is any.
            data = await response.json()
            friendsDisplay.innerHTML = '' // Clears the display content incase there is anything there.
            if (data.length == 0) { // If there is no data.
                let itemContainer = document.createElement('p')
                itemContainer.classList.add('friends--empty')
                itemContainer.textContent = 'This tab is currently empty!'
                friendsDisplay.appendChild(itemContainer)
            }
            else {
                data.forEach(item => { 
                    let itemContainer = document.createElement('p')
                    itemContainer.classList.add('friends--item')
                    itemContainer.textContent = `${item.username}#${item.tag}`
                    friendsDisplay.appendChild(itemContainer)
                })
            }
        }
        catch (err) {
            friendsDisplay.innerHTML = '' // Clears the display content to avoid confusion.
            updateErr('show', err.message)
            console.error(err)
        }
}