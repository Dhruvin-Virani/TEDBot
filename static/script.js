function sendOTP() {
  var phoneNumber = document.getElementById('phoneNumber').value;
  axios.post('/send_otp', { phone_number: phoneNumber })
    .then(response => {
      document.getElementById('message').innerText = response.data.message;
    })
    .catch(error => {
      console.error(error);
    });
}

function verifyOTP() {
  var enteredOTP = document.getElementById('otp').value;
  axios.post('/verify_otp', { otp: enteredOTP })
    .then(response => {
      document.getElementById('message').innerText = response.data.message;
    })
    .catch(error => {
      console.error(error);
    });
}
