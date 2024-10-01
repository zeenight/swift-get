const btnpopup = document.querySelector('button');
const Wrapping =document.querySelector('.Wrapping')
btnpopup.addEventListener('click', () => {Wrapping.classList.toggle('active-popup');
    console.log('Button clicked!');
});



// document.addEventListener('DOMContentLoaded', function () {
//     // Select all spans within the "navigation" class
//     const navigationSpans = document.querySelectorAll('.navigation span');

//     // Add a click event listener to each span
//     navigationSpans.forEach(function (span) {
//         span.addEventListener('click', function () {
//             // Your click function logic here
//             console.log(`Clicked on: ${span.innerText}`);
//         });
//     });
// });