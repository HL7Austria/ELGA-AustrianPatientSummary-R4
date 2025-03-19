let is_draggable = false;

class Draggable {
    constructor(draggableElement) {
        this.draggableElement = draggableElement;
        this.isDragging = false;
        this.hasDragged = false;
        this.offsetX = 0;
        this.offsetY = 0;

        this.onMouseMove = this.onMouseMove.bind(this);
        this.stopMoving = this.stopMoving.bind(this);
        this.header =  this.draggableElement.querySelector(".expansion-panel-header");

        this.init();
    }

    init() {
        if(this.header) {
            this.header.addEventListener("mousedown", (event) => this.startMoving(event));
        }
    }

    startMoving(event) {
        if(!is_draggable) return;

        event.preventDefault();

        const rect = this.draggableElement.getBoundingClientRect();
        this.offsetX = event.clientX - rect.left;
        this.offsetY = event.clientY - rect.top;
        this.header.style.cursor = 'grabbing'
        this.isDragging = true;
        this.hasDragged = false;

        document.addEventListener("mousemove", this.onMouseMove);
        document.addEventListener("mouseup", this.stopMoving);
    }

    onMouseMove(event) {
        if(!this.isDragging) return;

        this.hasDragged = true;

        const newX = event.clientX - this.offsetX;
        const newY = event.clientY - this.offsetY + window.scrollY;

        this.draggableElement.style.position = "absolute";
        this.draggableElement.style.left = `${newX}px`;
        this.draggableElement.style.top = `${newY}px`;
    }

    stopMoving() {
        this.isDragging = false;
        this.header.style.cursor = 'pointer';
        document.removeEventListener("mousemove", this.onMouseMove);
        document.removeEventListener("mouseup", this.stopMoving);
        this.checkDropContainer();
    }

    checkDropContainer() {
        const cursorX = event.clientX;
        const cursorY = event.clientY;
        const container = document.querySelector('.container-expansion-panels-dynamic');
    
        let droppedInsideContainer = false;
        const containerRect = container.getBoundingClientRect();

        if (
            cursorX >= containerRect.left &&
            cursorX <= containerRect.right &&
            cursorY >= containerRect.top &&
            cursorY <= containerRect.bottom
        ) {
            droppedInsideContainer = true;
            this.draggableElement.style.position = "static";
            this.draggableElement.classList.add('expansion-panel-dynamic');
            this.draggableElement.classList.remove('expansion-panel-open');
        }
    
        if (!droppedInsideContainer) {
            this.draggableElement.classList.remove('expansion-panel-dynamic');
        }
    }
}

document.querySelectorAll(".expansion-panel").forEach((element) => {
    new Draggable(element);
});