export const v_allergies_config = {
  layout: "fitDataStretch",
  responsiveLayout: "collapse",
  rowHeader: {
    formatter: "responsiveCollapse",
    hozAlign: "left",
    resizable: false,
    headerSort: false,
    cssClass: "wrap-text",
  },
  columns: [
    {
      title: "Gegen das bin ich allergisch:",
      field: "allergien",
      responsive: 0,
      width: 500,
      minWidth: 300, 
      hozAlign: "left",
      headerHozAlign: "left",
      cssClass: "wrap-text",
    },
  ],
};

export const i_allergies_config = {
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
      title: "Allergien", 
      field: "allergien", 
      responsive: 0, 
      width: 350,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    { 
      title: "Aktivität", 
      field: "aktivitaet", 
      responsive: 2, 
      width: 120,
      minWidth: 120,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem",
      field: "codesystem",
      cssClass: "wrap-text",
      responsive: 3,
      minWidth: 80,
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type = row_data?.codesystem_type;
        const url = cell.getValue();
        return url == "-"
          ? "-"
          : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type || url}</a>`;
      },
      
    },
  ],
};