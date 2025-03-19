let zoomInPercent = 100;

function toggleZoomScreenAbsoluteTo(percentNumber) {
    zoomInPercent = percentNumber;
    document.querySelector('main').style.zoom  = zoomInPercent + "%";
}

function toggleZoomScreenRelativeChange(percentNumber) {
    toggleZoomScreenAbsoluteTo(+zoomInPercent + +percentNumber);
}