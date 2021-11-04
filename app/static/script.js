document.addEventListener('DOMContentLoaded', () => {
  /*
  ** Delete Notification message
  */

  (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
      const $notification = $delete.parentNode
      $delete.addEventListener('click', () => {
        $notification.parentNode.removeChild($notification)
      })
  })

  /* 
  ** Form - dynamic validation
  */

  // Username
  const username = document.getElementById('username')
  if(username) {
    username.addEventListener('keyup', () => {
      const span = username.nextElementSibling
      if(username.value.length < 3 || username.value.length > 20) {
        username.classList.add('is-danger')
        span.firstElementChild.classList.add('fa-exclamation-triangle')
      }
      else {
        username.classList.remove('is-danger')
        username.classList.add('is-success')
        span.firstElementChild.classList.remove('fa-exclamation-triangle')
        span.firstElementChild.classList.add('fa-check')
      }
    })
  }

  // Password
  const password = document.getElementById('password')
  if(password) {
    password.addEventListener('keyup', () => {
      const span = password.nextElementSibling
      if(password.value.length < 4) {
        password.classList.add('is-danger')
        span.firstElementChild.classList.add('fa-exclamation-triangle')
      }
      else {
        password.classList.remove('is-danger')
        password.classList.add('is-success')
        span.firstElementChild.classList.remove('fa-exclamation-triangle')
        span.firstElementChild.classList.add('fa-check')
      }
    })
  }

  // Email 
  // https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript
  function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
    return re.test(String(email).toLowerCase())
  }
  const email = document.getElementById('email')
  if(email) {
    email.addEventListener('keyup', () => {
      const span = email.nextElementSibling
      if(!validateEmail(email.value)) {
        email.classList.add('is-danger')
        span.firstElementChild.classList.add('fa-exclamation-triangle')
      }
      else {
        email.classList.remove('is-danger')
        email.classList.add('is-success')
        span.firstElementChild.classList.remove('fa-exclamation-triangle')
        span.firstElementChild.classList.add('fa-check')
      }
    })
  }

  // Confirm password
  const confirm = document.getElementById('confirm')
  if(password && confirm) {
    confirm.addEventListener('keyup', () => {
      const span = confirm.nextElementSibling
      if(confirm.value !== password.value) {
        confirm.classList.add('is-danger')
        span.firstElementChild.classList.add('fa-exclamation-triangle')
      }
      else {
        confirm.classList.remove('is-danger')
        confirm.classList.add('is-success')
        span.firstElementChild.classList.remove('fa-exclamation-triangle')
        span.firstElementChild.classList.add('fa-check')
      }
    })
  }

  // Picture
  const picture = document.getElementById('picture')
  const picErr = document.getElementById('pic-err')
  if(picture) {
    picture.addEventListener('change', () => {
      const span = picture.nextElementSibling
      if(!picture.files[0].name.match(/.(jpg|jpeg|png|gif)$/i)) {
        picture.classList.add('is-danger')
        span.firstElementChild.classList.add('fa-exclamation-triangle')
        picErr.innerHTML = 'File extension must be either .jpg, .jpeg, .png, .gif'
      }
      else {
        picture.classList.remove('is-danger')
        picture.classList.add('is-success')
        picErr.innerHTML = ''
        span.firstElementChild.classList.remove('fa-exclamation-triangle')
        span.firstElementChild.classList.add('fa-check')
      }
    })
  }

  /*
  * Account Modifications
  */
  const formAccount = document.getElementById('form-account')
  const accountDiv = document.getElementById('account-data')
  const editBtns = document.getElementsByClassName('edit')
  if(formAccount && editBtns) {
  Array.from(editBtns).forEach((editBtn) => {
    editBtn.addEventListener('click', () => {
      accountDiv.classList.add('is-hidden')
      formAccount.classList.remove('is-hidden')
    })
  })
  }

  /*
  * Menu
  */
  const menu = document.getElementById('menu')
  const aside = document.getElementById('aside')
  if(menu && aside) {
    menu.addEventListener('click', () => {
      if(menu.firstElementChild.classList.contains('fa-bars')) {
        menu.firstElementChild.classList.remove('fa-bars')
        menu.firstElementChild.classList.add('fa-times')
        aside.style.left = '0'
      } else {
        menu.firstElementChild.classList.remove('fa-times')
        menu.firstElementChild.classList.add('fa-bars')
        aside.style.left = '-220px'
      }
    })
  }

  /*
  * Delete confirm modal
  */
  const dels = document.querySelectorAll('.del')
  const modals = document.querySelectorAll('.modal')
  const closes = document.querySelectorAll('.delete')
  const cancels = document.querySelectorAll('.cancel')

  if(dels && modals && closes && cancels) {

    Array.from(dels).forEach((del, i) => {
      del.addEventListener('click', (e) => {
        modals[i].classList.add('is-active')
      })
    })

    Array.from(closes).forEach((close, i) => {
      close.addEventListener('click', () => {
        modals[i].classList.remove('is-active')
      })
    })

    Array.from(cancels).forEach((cancel, i) => {
      cancel.addEventListener('click', () => {
        modals[i].classList.remove('is-active')
      })
    })

    Array.from(modals).forEach(modal => {
      modal.querySelector('.modal-background').addEventListener('click', () => {
        modal.classList.remove('is-active')
      })
    })
  }
})