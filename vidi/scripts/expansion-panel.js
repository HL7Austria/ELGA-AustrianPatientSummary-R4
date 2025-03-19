const expansion_panels = document.querySelectorAll('.expansion-panel');
const toggle_expansion_panel = document.getElementById('toggle-expansion-panel');

expansion_panels.forEach(initExpansionPanel);

toggle_expansion_panel.addEventListener('change', (event) => {
    event.target.checked ? expandAll() : collapseAll();
});

function initExpansionPanel(expansion_panel) {
    const header = expansion_panel.querySelector('.expansion-panel-header');
    const btn_collapses = expansion_panel.querySelectorAll('.btn-collapse');
    const draggable_element = new Draggable(expansion_panel);

    btn_collapses.forEach(btn_collapse => {
        btn_collapse.addEventListener('click', (event) => {
            expansion_panel.classList.remove('expansion-panel-open');
            event.stopPropagation();
        });
    });

    header.addEventListener('click', () => {
        if (!draggable_element.hasDragged && !expansion_panel.classList.contains('expansion-panel-dynamic')) {
            expansion_panel.classList.add('expansion-panel-open');
        }
        draggable_element.hasDragged = false;
    });

    expansion_panel.addEventListener('mousedown', () => {
        resetZindex();
        expansion_panel.style.zIndex = '10';
    });
}

function expandAll() {
    expansion_panels.forEach(panel => panel.classList.add('expansion-panel-open'));
}

function collapseAll() {
    expansion_panels.forEach(panel => panel.classList.remove('expansion-panel-open'));
}

function resetZindex() {
    expansion_panels.forEach(panel => {
        panel.style.zIndex = panel.classList.contains('expansion-panel-open') ? '2' : '1';
    });
}

function unsetExpansionPanelsPosition() {
    expansion_panels.forEach(panel => {
        panel.style.position = 'unset';
        panel.style.left = 'unset';
        panel.style.top = 'unset';
    });
}

