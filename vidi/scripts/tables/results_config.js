export const i_results_config = {
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
      title: "Zeitpunkt",
      field: "zeitpunkt",
      responsive: 3,
        width: 150,
        minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Gemessener Wert",
      field: "gemessenerWert",
      responsive: 0,
      width: 300,
      minWidth: 200,
      cssClass: "wrap-text",
    },
    {
      title: "Ergebnis",
      field: "ergebnis",
      responsive: 2,
      width: 250,
      minWidth: 200,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem <br>Wert",
      field: "codesystemWert",
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type_wert = row_data?.codesystem_type_wert;
        const url = cell.getValue();
        return url == '-' ? '-' : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type_wert || url}</a>`

      },
      cssClass: "wrap-text",
      responsive: 4,
      width: 250,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem<br>Ergebnis",
      field: "codesystemErgebnis",
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type_ergebnis = row_data?.codesystem_type_ergebnis;
        const url = cell.getValue();
        return url == '-' ? '-' : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type_ergebnis || url}</a>`

      },
      cssClass: "wrap-text",
      responsive: 5,
      width: 250,
      minWidth: 80,
      cssClass: "wrap-text",
    },
    {
      title: "Status",
      field: "status",
      responsive: 6,
      minWidth: 80,
      cssClass: "wrap-text",
    },
  ],
};

export const v_results_config = {
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
      title: "Zeitpunkt",
      field: "zeitpunkt",
      responsive: 2,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Gemessener <br>Wert",
      field: "gemessenerWert",
      responsive: 0,
      width: 500,
      cssClass: "wrap-text",
    },
    {
      title: "Ergebnis",
      field: "ergebnis",
      responsive: 1,
      minWidth: 150,
      cssClass: "wrap-text",
    },
  ],
};
