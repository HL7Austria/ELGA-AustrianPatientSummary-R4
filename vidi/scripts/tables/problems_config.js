export const v_current_problems_config = {
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
      title: "Meine aktuellen Diagnosen <br>und Probleme sind:",
      field: "diagnose",
      responsive: 0,
      width: 500,
      minWidth: 100,
      cssClass: "wrap-text",
    },
    {
        title: "Erklärung:",
        field: "erklärung",
        formatter: function (cell) {
            const explanations = cell?.getValue();
            const tags = [];

            if (explanations && explanations.length) {
                explanations.forEach(explanation => tags.push(`<a href="${explanation['url']}" target="_blank" class="a-explanation">${explanation['label']}</a>`));
            }

            return tags.length ? tags.join('') : '';
        },
        responsive: 1,
          minWidth: 300,
          cssClass: "wrap-text",
      },
  ],
};

export const i_current_problems_config = {
  layout: "fitDataStretch",
  responsiveLayout: "collapse",
  rowHeader: {
    formatter: "responsiveCollapse",
    hozAlign: "center",
    resizable: false,
    headerSort: false,
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
      title: "Diagnose",
      field: "diagnose",
      responsive: 0,
      width: 370,
      minWidth: 200,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem",
      field: "codesystem",
        width: 250,
      minWidth: 80,
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type = row_data?.codesystem_type;
        const url = cell.getValue();
        return url == '-' ? '-' : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type || url}</a>`;
      },
        responsive: 2,
    },
    {
      title: "Status",
      field: "status",
      responsive: 3,
      width: 100,
      minWidth: 100,
      cssClass: "wrap-text",
    },
    {
      title: "Verifizierung",
      field: "verifizierung",
      responsive: 4,
      minWidth: 110,
      cssClass: "wrap-text",
    },
  ],
};

export const i_past_problems_config = {
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
      title: "Diagnose",
      field: "diagnose",
      responsive: 0,
      width: 370,
      minWidth: 200,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem",
      field: "codesystem",
      width: 250,
      minWidth: 80,
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type = row_data?.codesystem_type;
        const url = cell.getValue();
        return url == '-' ? '-' : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type || url}</a>`
      },
      cssClass: "wrap-text",
      responsive: 4,
    },
    {
      title: "Status",
      field: "status",
      responsive: 2,
      width: 100,
      minWidth: 100,
      cssClass: "wrap-text",
    },
    {
      title: "Verifizierung",
      field: "verifizierung",
      responsive: 3,
      minWidth: 110,
      cssClass: "wrap-text",
    },
  ],
};

export const v_past_problems_config = {
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
      title: "Meine vergangenen Diagnosen<br> und Probleme sind:",
      field: "diagnose",
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
      minWidth: 300,
      cssClass: "wrap-text",
    },
  ],
};

export const i_family_problems_config = {
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
      title: "Familienanamnese",
      field: "anamnese",
      responsive: 0,
      width: 370,
      minWidth: 200,
      cssClass: "wrap-text",
    },
    {
      title: "Codesystem",
      field: "codesystem",
      width: 250,
      minWidth: 80,
      formatter: function (cell) {
        const row_data = cell.getRow().getData();
        const codesystem_type = row_data?.codesystem_type;
        const url = cell.getValue();
        return url == '-' ? '-' : `<a href="${url}" target="_blank" class="a-explanation">${codesystem_type || url}</a>`
      },
      responsive: 4,
      cssClass: "wrap-text",
    },
    {
      title: "Status",
      field: "status",
      responsive: 2,
      width: 100,
      minWidth: 100,
      cssClass: "wrap-text",
    },
    {
      title: "Verifizierung",
      field: "verifizierung",
      responsive: 3,
      width: 110,
      minWidth: 110,
      cssClass: "wrap-text",
    },
  ],
};

export const v_family_problems_config = {
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
      title: "Familienanamnese",
      field: "anamnese",
      responsive: 0,
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
      minWidth: 300,
      cssClass: "wrap-text",
    },
  ],
};