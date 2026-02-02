const romSelect = document.getElementById("rom")

romSelect.addEventListener("change", function (){
    const valgtSide = this.value;

    if (valgtSide) {
        window.location.href = valgtSide;
    }
});