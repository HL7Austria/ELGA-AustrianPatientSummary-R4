export const v_current_medication_config = {
  layout: "fitDataStretch",
  responsiveLayout: "collapse",
  rowHeader: {
    formatter: "responsiveCollapse",
    hozAlign: "center",
    resizable: false,
    headerSort: false,
    cssClass: "wrap-text",
  },
  responsiveLayoutCollapseStartOpen: false, 
  columns: [
    {
      title: "Name des Medikaments",
      field: "name",
      responsive: 0,
      width: 500,
      minWidth: 300,
      cssClass: "wrap-text",
    },
    {
      title: "Dosis",
      field: "dosis",
      responsive: 1,
      minWidth: 300,
      cssClass: "wrap-text",
    },
  ],
};

export const i_current_medication_config = {
  layout: "fitDataStretch",
  responsiveLayout: "collapse",
  rowHeader: {
    formatter: "responsiveCollapse",
    hozAlign: "center",
    resizable: false,
    headerSort: false,
    cssClass: "wrap-text",
  },
  responsiveLayoutCollapseStartOpen: false, 
  columns: [
    {
      title: "",
      field: "marked",
      width: 55,
      minWidth: 55,
      hozAlign: "center",
      formatter: function (cell) {
        const data = cell.getRow().getData();
        const symbol = data.marked === 1 ? '⚠️' : data.marked === 2 ? '?' : '▢';
        return `
          <span class="status-icon" style="cursor:pointer;">${symbol}</span>
        `;
      },
      cellClick: function (e, cell) {
        const rowData = cell.getRow().getData();
        
        if (rowData.marked === undefined) {
          rowData.marked = 0; 
        }
        rowData.marked = (rowData.marked + 1) % 3;
        cell.getRow().update(rowData);
      },
      responsive: 1,
    },
    {
      title: "Name",
      field: "name",
      responsive: 0,
      width: 220,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Dosis",
      field: "dosis",
      responsive: 2,
      width: 250,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Beginn der<br> Einnahme",
      field: "beginn",
      responsive: 3,
      width: 140,
      minWidth: 140,
      cssClass: "wrap-text",
    },
    {
      title: "Status",
      field: "status",
      responsive: 4,
      width: 100,
      minWidth: 100,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem",
      field: "codesystem",
      responsive: 4,
      minWidth: 100,
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type = row_data?.codesystem_type;
        const url = cell.getValue();
        return url == '-' ? '-' : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type || url}</a>`;
      },
      cssClass: "wrap-text",
    },
  ],
};

export const i_past_medication_config = {
  layout: "fitDataStretch",
  responsiveLayout: "collapse",
  rowHeader: {
    formatter: "responsiveCollapse",
    hozAlign: "center",
    resizable: false,
    headerSort: false,
    cssClass: "wrap-text",
  },
  responsiveLayoutCollapseStartOpen: false, 
  columns: [
    {
      title: "",
      field: "marked",
      width: 55,
      minWidth: 55,
      hozAlign: "center",
      formatter: function (cell) {
        const data = cell.getRow().getData();
        const symbol = data.marked === 1 ? '⚠️' : data.marked === 2 ? '?' : '▢';
        return `
          <span class="status-icon" style="cursor:pointer;">${symbol}</span>
        `;
      },
      cellClick: function (e, cell) {
        const rowData = cell.getRow().getData();
        
        if (rowData.marked === undefined) {
          rowData.marked = 0; 
        }
        rowData.marked = (rowData.marked + 1) % 3;
        cell.getRow().update(rowData);
      },
      responsive: 1,
    },
    {
      title: "Name",
      field: "name",
      responsive: 0,
      width: 220,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Dosis",
      field: "dosis",
      responsive: 2,
      width: 250,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Beginn der<br> Einnahme",
      field: "beginn",
      responsive: 3,
      width: 140,
      minWidth: 140,
      cssClass: "wrap-text",
    },
    {
      title: "Status",
      field: "status",
      responsive: 4,
      width: 100,
      minWidth: 100,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem",
      field: "codesystem",
      responsive: 5,
      minWidth: 100,
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type = row_data?.codesystem_type;
        const url = cell.getValue();
        return url == '-' ? '-' : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type || url}</a>`;
      },
    },
  ],
};


export const v_past_medication_config = {
  layout: "fitDataStretch",
  responsiveLayout: "collapse",
  rowHeader: {
    formatter: "responsiveCollapse",
    hozAlign: "center",
    resizable: false,
    headerSort: false,
    cssClass: "wrap-text",
  },
  responsiveLayoutCollapseStartOpen: false, 
  columns: [
    {
      title: "Name meiner vergangenen <br> Medikamente",
      field: "name",
      responsive: 0,
      width: 500,
      minWidth: 300,
      cssClass: "wrap-text",
    },
    {
      title: "Dosis",
      field: "dosis",
      responsive: 1,
      responsive: 1,
      minWidth: 300,
      cssClass: "wrap-text",
    },
   
  ],
};