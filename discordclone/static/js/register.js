const form = document.forms['register-form'];
const firstField = document.querySelector('.firstfields');
const secondField = document.querySelector('.secondFields');

const usernameField = document.querySelector('#username');
const passwordField = document.querySelector('#password');
const emailField = document.querySelector('#email');

const usernameErr = document.querySelector('#usernameErr');
const passwordErr = document.querySelector('#passwordErr');
const emailErr = document.querySelector('#emailErr');
const dobErr = document.querySelector('#dobErr');
const submitBtn = document.querySelector('#submitBtn');
const lastErrField = document.querySelector('#lastErrField');

const dobField = document.getElementById('id_dob');
const profilePictureDisplay = document.querySelector('#profilePictureDisplay');
const profilePicture = document.querySelector('#id_profile_picture');
const currentYear = new Date().getFullYear();
const title = document.getElementsByTagName('h1')[0]
let age;

nextBtn = document.querySelector('#nextBtn');
backBtn = document.querySelector('#backBtn');

nextBtn.addEventListener('click', e => {
    e.preventDefault();

    title.innerText = 'Additional Info'
    title.style.fontSize = '1.3rem'
    passwordErr.style.visibility = 'hidden';
    emailErr.style.visibility = 'hidden';
    usernameErr.style.visibility = 'hidden';
    
    if (usernameField.value.length < 4) {
        usernameErr.innerText = 'Username must be at least 4 characters'
        usernameErr.style.visibility = 'visible'
        return
    }

    else if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(emailField.value))) {
        emailErr.innerText = 'Please enter a valid email address.'
        emailErr.style.visibility = 'visible'
        return
    }

    else if (passwordField.value.length < 8) {
        passwordErr.innerText = 'Password must be at least 8 characters'
        passwordErr.style.visibility = 'visible'
        return
    }

    firstField.classList.remove('show');
    secondField.classList.add('show');
    secondField.classList.remove('hide')
})

backBtn.addEventListener('click', e => {
    e.preventDefault();

    title.style.fontSize = '2rem'
    title.innerText = 'Register'
    firstField.classList.add('show');
    secondField.classList.remove('show');
    secondField.classList.add('hide')
})


dobField.addEventListener('change', () => {
    userYear = parseInt(dobField.value.slice(0, 4))
    age = currentYear - userYear 
    console.log(age)
    if (age < 13) {
        dobErr.innerText = 'You must be at least 13 years old to register'
        dobErr.style.visibility = 'visible';
    }
    else {
        dobErr.style.visibility = 'hidden';
    }
})

profilePicture.addEventListener('change', () => {
    picture = profilePicture.files[0];
    url = URL.createObjectURL(picture);
    profilePictureDisplay.src = url;
})

submitBtn.addEventListener('click', e => {
    e.preventDefault();

    lastErrField.style.cssText = 'visibility: hidden; text-align: center;'

    if (usernameField.value.length < 4) {
        lastErrField.innerText = 'Username must be at least 4 characters'
        lastErrField.style.visibility = 'visible'
        return
    }

    else if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(emailField.value))) {
        lastErrField.innerText = 'Please enter a valid email address.'
        lastErrField.style.visibility = 'visible'
        return
    }

    else if (passwordField.value.length < 8) {
        lastErrField.innerText = 'Password must be at least 8 characters'
        lastErrField.style.visibility = 'visible'
        return
    }

    else if (age == undefined) {
        lastErrField.innerText = 'You haven\'t specified an age.'
        lastErrField.style.visibility = 'visible'
    }
    else if (age < 13) {
        lastErrField.style.visibility = 'visible'
        lastErrField.innerText = 'You must be at least 13 years old to register'
        return
    }

    else {
        form.submit()
    }

})