const height_description_dynamic = 231;

document.querySelectorAll('input[name="view"]').forEach(radio => {
    radio.addEventListener('change', function() {
        switchView(this.value);
        resetToggleExpansionPanel();
        setIsDraggable(this.value);
        changeToggleExpansionPanelButtonPosition(this.value);
        switchDescriptionImage(this.value);
        unsetExpansionPanelsPosition();
        setLayout(this.value);
        setPrintVisibility(this.value);
    });
});

checkDynamicViewAvailability();

function switchView(view) {
    const containers = {
      simple: document.querySelector('#container-simple'),
      advanced: document.querySelector('#container-advanced'),
      dynamic: document.querySelector('#container-advanced')
    };

    containers.simple.style.display = 'none';
    containers.advanced.style.display = 'none';
    containers[view].style.display = 'flex';
}


function setIsDraggable(view) {
    is_draggable = view == 'dynamic' ? true : false;
}

function switchDescriptionImage(view) {
    document.querySelectorAll('.img-description').forEach(function(el) {
        el.classList.remove('active');
    });

    if (view === 'simple') {
        document.querySelector('[data-view="simple"]').classList.add('active');
    } else if (view === 'advanced') {
        document.querySelector('[data-view="advanced-static"]').classList.add('active');
    } else if (view === 'dynamic') {
        document.querySelector('[data-view="advanced-dynamic"]').classList.add('active');
    }
}

function setPrintVisibility(view) {

    if (view === 'advanced') {
        document.querySelector('.btn-print').style.visibility = 'visible';
    }
    else {
        document.querySelector('.btn-print').style.visibility = 'hidden';
    }
}

function resetToggleExpansionPanel() {
    const toggle_expansion_panel = document.querySelector('#toggle-expansion-panel');
    toggle_expansion_panel.checked = false;
    toggle_expansion_panel.dispatchEvent(new Event('change'));
}

function changeToggleExpansionPanelButtonPosition(view) {
    const div_toggle_expansion_panel = document.querySelector('#div-switch-expansion-panel');

    if(view == 'simple') {
        document.querySelector('#container-simple .div-description').appendChild(div_toggle_expansion_panel);
        div_toggle_expansion_panel.style.display = 'flex';
    }
    else if(view == 'advanced') {
        document.querySelector('#container-advanced .div-description').appendChild(div_toggle_expansion_panel);
        div_toggle_expansion_panel.style.display = 'flex';
    }
    else if(view == 'dynamic') {
        div_toggle_expansion_panel.style.display = 'none';
    }
}

function setLayout(view) {
    if(view == 'dynamic') {
        document.querySelectorAll('.expansion-panel').forEach((el) => el.classList.add('expansion-panel-dynamic'));
        document.querySelector('.container-expansion-panels-advanced').classList.add('container-expansion-panels-dynamic');
        const height_container_expansion_panels_dynamic = height_description_dynamic + document.querySelector('.container-expansion-panels-dynamic').clientHeight;
        console.log(height_container_expansion_panels_dynamic)
        document.querySelector('.container-expansion-panels-dynamic').style.height = `${height_container_expansion_panels_dynamic}px`;
        document.querySelector('#description-dynamic').style.display = 'block';
    }
    else {
        document.querySelectorAll('.expansion-panel').forEach((el) => el.classList.remove('expansion-panel-dynamic'));
        document.querySelector('.container-expansion-panels-advanced').classList.remove('container-expansion-panels-dynamic');
        document.querySelector('.container-expansion-panels-advanced').style.height = 'unset';
        document.querySelector('#description-dynamic').style.display = 'none';
    }
}

function checkDynamicViewAvailability() {
    const radio_btn = document.getElementById("view_dynamic");
    radio_btn.disabled = window.innerWidth < 767;
}

window.addEventListener("resize", checkDynamicViewAvailability);