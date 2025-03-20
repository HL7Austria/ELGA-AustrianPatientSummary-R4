export const i_procedures_config = {
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
      responsive: 2,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Operation oder Eingriff",
      field: "operation",
      responsive: 0,
        width: 300,
      minWidth: 300,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem",
      field: "codesystem",
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type = row_data?.codesystem_type;
        const url = cell.getValue();
        return url == '-' ? '-' : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type || url}</a>`
      },
      cssClass: "wrap-text",
      responsive: 3,
      width: 250,
      minWidth: 80,
      cssClass: "wrap-text",
    },
    {
      title: "Status",
      field: "status",
      responsive: 1,
      minWidth: 100,
      cssClass: "wrap-text",
    },
  ],
};

export const v_procedures_config = {
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
      responsive: 1,
      minWidth: 150,
      cssClass: "wrap-text",
    },
    {
      title: "Meine Operation oder Eingriff",
      field: "operation",
      responsive: 0,
      width: 500,
      minWidth: 300,
      cssClass: "wrap-text",
    },
    {
      title: "Erklärung:",
      field: "erklärung",
      formatter: function (cell) {
        const explanations = cell?.getValue();
        const tags = [];

        if(explanations && explanations.length) {
          explanations.forEach(explanation => tags.push(`<a href="${explanation['url']}" target="_blank" class="a-explanation">${explanation['label']}</a>`));
        }

        return tags.length ? tags.join('') : '';
      },
      responsive: 1,
      minWidth: 150,
      cssClass: "wrap-text",
    },
  ],
};