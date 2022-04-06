$('.my-slickies').slick({
    speed: 500,
    slidesToShow: 6,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1024,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 2,
            }
        },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 2,
            }
        },
    ]
});

function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");

    if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "&#9660; Read more &#9660;";
        moreText.style.display = "none";
    } else {
        dots.style.display = "none";
        btnText.innerHTML = "&#9650; Read less &#9650;";
        moreText.style.display = "inline";
    }
}

function getParamSearch(name, value) {
    var searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has(name) && searchParams.get(name) == value) {
        searchParams.delete(name);
    } else {
        searchParams.set(name, value);
    }
    window.location.search = searchParams.toString();
}
