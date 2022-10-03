const buttons = document.querySelectorAll('.btn--nav')
const errDisplay = document.querySelector('.err--nav')
const friendsDisplay = document.querySelector('#friends--display')
const activeTab = document.querySelector('#activeTab');

const updateErr = (mode, errMessage) => {
    if (mode === 'show') {
        errDisplay.style.visibility = 'visible'
        errDisplay.textContent = errMessage 
    }
    else if (mode === 'hide') {
        errDisplay.style.visibility = 'hidden'
    }
}

document.addEventListener('DOMContentLoaded', () => {
    updateErr('hide');
    fetchData('friends'); // To show the friends tab upon page load.
})

buttons.forEach(btn => {
    btn.addEventListener('click', async () => {
        mode = event.currentTarget.dataset.id
        fetchData(mode)
    });
})

const fetchData = async (mode) => {
        try {
            response = await fetch(`${fetchUrl}?mode=${mode}`)

            if (!response.ok ) {
                throw new Error('Could not reach the server...')
            }
            updateErr('hide') // Hides the error message incase there is any.
            data = await response.json()
            friendsDisplay.innerHTML = '' // Clears the display content incase there is anything there.
            activeTab.textContent = `Currently viewing ${mode}` // Setting the clicked tab.
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