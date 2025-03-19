// All the configs for every section are beeing loaded

import {v_current_medication_config, i_current_medication_config, v_past_medication_config,
    i_past_medication_config} from './medication_config.js';
import {v_allergies_config, i_allergies_config} from './allergies_config.js';
import {v_current_problems_config, i_current_problems_config, v_past_problems_config,
    i_past_problems_config, v_family_problems_config, i_family_problems_config} from './problems_config.js';
import {v_procedures_config, i_procedures_config} from './procedures_config.js';
// immunizations missing
// medicaldevices missing
import {v_results_config, i_results_config} from './results_config.js';
import {v_vitalsigns_config, i_vitalsigns_config} from './vitalsigns_config.js';
// functionalstatus missing
// planofcare missing
import {v_socialhistory_config, i_socialhistory_config} from './socialhistory_config.js';
// pregnancy missing
// advanceddirectives missing


// This is the one and only file the into vidi schema transformed data comes from
// xxxx
// import example from './_ips_as_vidi_example.json' with {type: 'json'};
// loadFrom(example)

export function loadFrom(data){
    try {
        data = JSON.parse(data)
    }catch (e) {
        console.log('Example loaded.');
    }
    // now the data is beeing splitted into its components, even empty tables have data with at least one line with emtpy values
    const {
        v_current_medication_data, i_current_medication_data, v_past_medication_data, i_past_medication_data,
        v_allergies_data, i_allergies_data,
        v_current_problems_data, i_current_problems_data, v_past_problems_data, i_past_problems_data, v_family_problems_data, i_family_problems_data,
        v_procedures_data, i_procedures_data,
        // immunizations missing
        // medicaldevices missing
        v_results_data, i_results_data,
        v_vitalsigns_data, i_vitalsigns_data,
        // functionalstatus missing
        // planofcare missing
        v_socialhistory_data, i_socialhistory_data,
        // pregnancy missing
        // advanceddirectives missing
    } = data


    // At least the constructor for all the vidi sections are beeing called

    new Tabulator("#v_current_medication", Object.assign({}, v_current_medication_data, v_current_medication_config));
    new Tabulator("#i_current_medication", Object.assign({}, i_current_medication_data, i_current_medication_config));
    new Tabulator("#v_past_medication", Object.assign({}, v_past_medication_data, v_past_medication_config));
    new Tabulator("#i_past_medication", Object.assign({}, i_past_medication_data, i_past_medication_config));

    new Tabulator("#v_allergies", Object.assign({}, v_allergies_data, v_allergies_config));
    new Tabulator("#i_allergies", Object.assign({}, i_allergies_data, i_allergies_config));

    new Tabulator("#v_current_problems", Object.assign({}, v_current_problems_data, v_current_problems_config));
    new Tabulator("#i_current_problems", Object.assign({}, i_current_problems_data, i_current_problems_config));
    new Tabulator("#v_past_problems", Object.assign({}, v_past_problems_data, v_past_problems_config));
    new Tabulator("#i_past_problems", Object.assign({}, i_past_problems_data, i_past_problems_config));
    new Tabulator("#v_family_problems", Object.assign({}, v_family_problems_data, v_family_problems_config));
    new Tabulator("#i_family_problems", Object.assign({}, i_family_problems_data, i_family_problems_config));

    new Tabulator("#v_procedures", Object.assign({}, v_procedures_data, v_procedures_config));
    new Tabulator("#i_procedures", Object.assign({}, i_procedures_data, i_procedures_config));

    // immunizations missing

    // medicaldevices missing

    new Tabulator("#v_results", Object.assign({}, v_results_data, v_results_config));
    new Tabulator("#i_results", Object.assign({}, i_results_data, i_results_config));

    new Tabulator("#v_vitalsigns", Object.assign({}, v_vitalsigns_data, v_vitalsigns_config));
    new Tabulator("#i_vitalsigns", Object.assign({}, i_vitalsigns_data, i_vitalsigns_config));

    // functionalstatus missing

    // planofcare missing

    new Tabulator("#v_socialhistory", Object.assign({}, v_socialhistory_data, v_socialhistory_config));
    new Tabulator("#i_socialhistory", Object.assign({}, i_socialhistory_data, i_socialhistory_config));

    // pregnancy missing

    // advanceddirectives missing

}